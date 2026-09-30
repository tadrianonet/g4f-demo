"""Interface simples para demonstrar o g4f em aula.

Iniciar: streamlit run app.py
"""
from __future__ import annotations

from verificar_python import exigir_python_minimo

exigir_python_minimo()

import streamlit as st

from chat import enviar_mensagem
from config import get_settings

st.set_page_config(page_title="Demo GPT4Free", layout="centered")
settings = get_settings()

st.title("Demo GPT4Free (g4f)")
st.caption(
    "Exemplo educacional sobre o projeto "
    "[GPT4Free](https://github.com/xtekky/gpt4free). "
    "Use apenas em contexto de estudo e respeite os termos dos serviços."
)

with st.sidebar:
    st.header("Configuração")
    model = st.text_input("Modelo", value=settings.model)
    if settings.api_base:
        st.info(f"API local: `{settings.api_base}` (definida em G4F_API_BASE)")
    elif settings.provider:
        st.info(f"Provedor fixo: `{settings.provider}`")
    else:
        st.info("Modo padrão: o g4f escolhe o provedor (como no README oficial).")
    st.markdown(
        "[Documentação do cliente](https://g4f.dev/docs/client) · "
        "[Repositório no GitHub](https://github.com/xtekky/gpt4free)"
    )

prompt = st.text_area("Sua pergunta", height=120, placeholder="Explique o que é machine learning em 3 linhas.")
if st.button("Enviar", type="primary", disabled=not prompt.strip()):
    with st.spinner("Aguardando resposta..."):
        try:
            resposta = enviar_mensagem(prompt, model=model)
            st.success("Resposta recebida")
            st.markdown(resposta)
        except Exception as exc:
            st.error(f"{type(exc).__name__}: {exc}")
            st.markdown(
                "**Se falhar na sala de aula:** suba o Docker oficial (`docker compose up -d`) "
                "e defina `G4F_API_BASE=http://127.0.0.1:8080/v1` no arquivo `.env`."
            )
