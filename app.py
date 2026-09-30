"""Interface simples para demonstrar o g4f em aula.

Iniciar: streamlit run app.py
"""
from __future__ import annotations

import sys

import streamlit as st

from config import get_settings
from verificar_python import mensagem_python_insuficiente, python_suportado

st.set_page_config(page_title="Demo GPT4Free", layout="centered")

if not python_suportado():
    st.title("Demo GPT4Free (g4f)")
    st.error("Versão do Python incompatível")
    st.markdown(mensagem_python_insuficiente())
    st.stop()

from chat import enviar_mensagem
from formatar_erro import dica_docker_markdown, resumir_erro
from formatar_resposta import formatar_resposta, parece_html

settings = get_settings()

st.title("Demo GPT4Free (g4f)")
st.caption(
    "Exemplo educacional sobre o projeto "
    "[GPT4Free](https://github.com/xtekky/gpt4free). "
    "Use apenas em contexto de estudo e respeite os termos dos serviços."
)
st.caption(f"Python {'.'.join(map(str, sys.version_info[:3]))}")

with st.sidebar:
    st.header("Configuração")
    model = st.text_input("Modelo", value=settings.model)
    if settings.api_base:
        st.info(f"API local: `{settings.api_base}` (definida em G4F_API_BASE)")
    elif settings.provider:
        st.info(f"Provedor fixo: `{settings.provider}`")
    else:
        st.warning(
            "Modo automático: vários provedores públicos podem falhar (auth, pagamento). "
            "Para aula, prefira API local via Docker (veja README)."
        )
    st.markdown(
        "[Documentação do cliente](https://g4f.dev/docs/client) · "
        "[Repositório no GitHub](https://github.com/xtekky/gpt4free)"
    )

prompt = st.text_area("Sua pergunta", height=120, placeholder="Explique o que é machine learning em 3 linhas.")
if st.button("Enviar", type="primary", disabled=not prompt.strip()):
    with st.spinner("Aguardando resposta..."):
        try:
            bruta = enviar_mensagem(prompt, model=model)
            exibicao = formatar_resposta(bruta)
            st.success("Resposta recebida")
            st.markdown(exibicao)
            if parece_html(bruta):
                with st.expander("Resposta original (HTML do provedor)"):
                    st.code(bruta, language="html")
        except Exception as exc:
            info = resumir_erro(exc, api_base=settings.api_base)
            st.error(info.titulo)
            st.markdown(info.mensagem)
            if info.falhas:
                st.markdown("**O que aconteceu por provedor:**")
                for f in info.falhas:
                    st.markdown(f"- **{f.provedor}** ({f.tipo}): {f.resumo}")
            with st.expander("Detalhes técnicos completos"):
                st.code(info.tecnico, language=None)
            if info.sugerir_docker:
                st.markdown(dica_docker_markdown())
