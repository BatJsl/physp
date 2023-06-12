import streamlit as st
from affichage import disp_app
from traces import trace_sans_frott
from traces import trace_avec_frottements
from traces import trajectoire_reelle

# Chemin d'accès à l'image
image_path = "Desktop/physp/image_rugby.jpg"

# Code HTML/CSS pour l'image de fond
html_code = f'''
<style>
body {{
    background-image: url("{image_path}");
    background-size: cover;
}}
</style>
'''

# Affichage de l'image de fond
st.markdown(html_code, unsafe_allow_html=True)

disp_app()

# trace_avec_frottements()


trajectoire_reelle()
