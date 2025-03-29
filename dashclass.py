import os
import streamlit as st
from streamlit.runtime.scriptrunner import RerunException, get_script_run_ctx

st.set_page_config(page_title="DashClass Launcher", layout="centered")
st.markdown("<h2 style='text-align: center;'>DashClass - Identificação do Professor</h2>", unsafe_allow_html=True)

st.write("Bem-vindo ao DashClass! Para começar, informe seu nome abaixo. Isso nos ajudará a personalizar seu ambiente de trabalho e manter seus dados separados dos demais professores.")

nome = st.text_input("Digite seu nome completo:")

if nome:
    # Normalizar o nome para pasta (sem espaços, acentos, etc.)
    nome_folder = nome.strip().lower().replace(" ", "_").replace("ç", "c").replace("ã", "a").replace("á", "a").replace("é", "e")

    destino = os.path.join("usuarios", nome_folder)
    if not os.path.exists(destino):
        os.makedirs(destino)
        origem = "modelo_dashclass"
        os.system(f"xcopy /E /I /Y \"{origem}\" \"{destino}\"")

    st.success(f"Ambiente de trabalho criado para {nome}.")
    st.session_state['usuario'] = nome

    # Redirecionar para o DashClass do usuário
    raise RerunException(get_script_run_ctx())

if 'usuario' in st.session_state:
    nome_folder = st.session_state['usuario'].strip().lower().replace(" ", "_").replace("ç", "c").replace("ã", "a").replace("á", "a").replace("é", "e")
    destino = os.path.join("usuarios", nome_folder)
    dash_path = os.path.join(destino, "dashclass.py")

    if os.path.exists(dash_path):
        st.success(f"Abrindo seu DashClass, {st.session_state['usuario']}...")
        exec(open(dash_path, encoding="utf-8").read(), globals())
    else:
        st.error("Erro ao localizar seu ambiente personalizado. Tente novamente ou contate o suporte.")
