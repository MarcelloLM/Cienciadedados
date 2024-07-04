import streamlit as st

st.title("Seja bem vindo!")
st.header("Primeiro teste realizado com o streamlit")
st.subheader("Primeiro teste")
st.markdown("----")

st.markdown("# Isso é um texto com markdown e um [#] ")
st.markdown(" ## Isso é um texto com markdown e um [##] ")
st.markdown(" ### Isso é um texto com markdown e um [###] ")

st.markdown("----")

st.markdown("Markdown")
st.markdown("_Markdown Itálico_")
st.markdown("*Markdown Itálico*")
st.markdown("__Markdown negrito__")
st.markdown("**Markdown negrito**")

st.markdown("Esse é um link para o [google](https://google.com.br)")

st.markdown("<h1 style= 'text-align: center; color: red'>Título em vermelho</h1>", unsafe_allow_html=True)

st.markdown("Ola, mundo :sunglasses:")
st.markdown("Ola, mundo :100:")
