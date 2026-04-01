from rag_core import answer_order_query, answer_return_query


def main():
    print("=== DEMO ECOASSIST AI PRO ===")
    print("1. Consultar pedido")
    print("2. Consultar devolución")
    option = input("Selecciona una opción (1/2): ").strip()

    if option == "1":
        query = input("Escribe tu consulta de pedido: ").strip()
        print("\n--- Respuesta ---")
        print(answer_order_query(query))
    elif option == "2":
        producto = input("Producto: ").strip()
        categoria = input("Categoría: ").strip()
        dias = int(input("Días desde la compra: ").strip())
        estado = input("Estado del producto: ").strip()
        print("\n--- Respuesta ---")
        print(answer_return_query(producto, categoria, dias, estado))
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
