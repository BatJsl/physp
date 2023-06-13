import streamlit as st
from affichage import disp_app
from traces import trace_sans_frott
from traces import trace_avec_frottements
from traces import trajectoire_reelle

# Chemin d'accès à l'image
image_path = "Desktop/physp/image_rugby.jpg"

disp_app()

# trace_avec_frottements()


trajectoire_reelle()
