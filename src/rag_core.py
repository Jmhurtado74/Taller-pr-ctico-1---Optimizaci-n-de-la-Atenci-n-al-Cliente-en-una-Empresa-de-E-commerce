import json
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


def load_json(filename: str):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


PEDIDOS = load_json("pedidos.json")
POLITICAS = load_json("politicas.json")
FAQ = load_json("faq.json")


def normalize(text: str) -> str:
    return text.lower().strip()


def retrieve_order(query: str) -> List[Dict]:
    q = normalize(query)
    hits = []
    for pedido in PEDIDOS:
        if pedido["id"] in q or normalize(pedido["cliente"]) in q:
            hits.append(pedido)
    return hits


def retrieve_faq(query: str) -> List[Dict]:
    q = normalize(query)
    hits = []
    for item in FAQ:
        if any(token in normalize(item["pregunta"]) for token in q.split()):
            hits.append(item)
    return hits[:3]


def evaluate_return(categoria: str, dias_desde_compra: int, estado_producto: str) -> Tuple[bool, str, List[str]]:
    categoria = normalize(categoria)
    estado_producto = normalize(estado_producto)
    rules = POLITICAS["devoluciones"]

    if categoria in rules["categorias_no_permitidas"]:
        return False, f"La categoría '{categoria}' no admite devoluciones según la política.", []

    if dias_desde_compra > rules["dias_maximos"]:
        return False, f"La solicitud supera el límite de {rules['dias_maximos']} días permitido por la política.", []

    if estado_producto not in [normalize(x) for x in rules["estado_requerido"]]:
        return False, "El estado reportado del producto no cumple las condiciones requeridas para devolución.", []

    return True, "La devolución es elegible según la política vigente.", rules["pasos"]


def answer_order_query(query: str) -> str:
    pedidos = retrieve_order(query)
    if pedidos:
        pedido = pedidos[0]
        estado = pedido["estado"]
        fecha = pedido["fecha_estimada"]
        tracking = pedido["tracking_url"]
        extra = ""
        if estado.lower() == "retrasado":
            extra = "Lamentamos el retraso. Estamos revisando la novedad logística para entregarlo lo antes posible."
        elif estado.lower() == "cancelado":
            extra = "El pedido fue cancelado. Si necesitas más ayuda, podemos escalar el caso a un asesor."
        else:
            extra = "Tu pedido sigue el flujo normal del proceso logístico."
        return (
            f"Estado del pedido: {estado}\n"
            f"Fecha estimada: {fecha}\n"
            f"Seguimiento: {tracking}\n"
            f"Mensaje adicional: {extra}"
        )

    faqs = retrieve_faq(query)
    if faqs:
        lines = [f"- {item['pregunta']}: {item['respuesta']}" for item in faqs]
        return "No se encontró un pedido específico, pero encontré información relacionada:\n" + "\n".join(lines)

    return "No encontré información suficiente para responder con seguridad. Recomiendo escalar el caso a un agente humano."


def answer_return_query(producto: str, categoria: str, dias_desde_compra: int, estado_producto: str) -> str:
    ok, explanation, steps = evaluate_return(categoria, dias_desde_compra, estado_producto)
    if ok:
        steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)])
        return (
            "Resultado: Aprobado\n"
            f"Explicación: {explanation}\n"
            f"Pasos a seguir:\n{steps_text}"
        )
    return (
        "Resultado: No aprobado\n"
        f"Explicación: {explanation}\n"
        "Pasos a seguir: Puedes solicitar revisión manual si consideras que tu caso requiere validación adicional."
    )
