import streamlit as st
from rag_core import answer_order_query, answer_return_query

st.set_page_config(page_title="EcoAssist AI Pro", layout="centered")
st.title("EcoAssist AI Pro")
st.caption("Demo académica de atención al cliente con enfoque RAG")

mode = st.radio("Selecciona el tipo de consulta", ["Estado de pedido", "Devolución de producto"])

if mode == "Estado de pedido":
    query = st.text_input("Escribe tu consulta", placeholder="Ej: ¿Cuál es el estado del pedido 12347?")
    if st.button("Consultar") and query:
        st.text_area("Respuesta", answer_order_query(query), height=180)
else:
    producto = st.text_input("Producto", placeholder="Ej: Cepillo ecológico")
    categoria = st.selectbox("Categoría", ["hogar", "higiene", "perecederos", "tecnología", "moda"])
    dias = st.number_input("Días desde la compra", min_value=0, max_value=365, value=10)
    estado = st.selectbox("Estado del producto", ["sin uso", "cerrado", "en buen estado", "usado", "dañado"])
    if st.button("Evaluar devolución"):
        st.text_area("Respuesta", answer_return_query(producto, categoria, int(dias), estado), height=220)
