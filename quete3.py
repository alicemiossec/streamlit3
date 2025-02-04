import streamlit as st
import pandas as pd
from datetime import date
import  streamlit_authenticator  as  stauth

import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

st.write("pour visiter ma page: login: utilisateur, mdp: utilisateurMDP")

authenticator.login()

def accueil():
      st.title("Bienvenue sur ma page d'Alice")

if st.session_state["authentication_status"]:
  accueil()


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu


# Using "with" notation
with st.sidebar:
    if st.session_state['authentication_status']:
        add_radio = st.radio(
        "vous souhaitez vous déconnecter",
        authenticator.logout()
    )
# Création du menu qui va afficher les choix qui se trouvent dans la variable options
    selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"])
if selection == "Accueil" and st.session_state['authentication_status']:
    st.write("Bienvenue dans mon univers")
elif selection == "Photos" and st.session_state['authentication_status']:
    st.write("Bienvenue sur mon album photo")
    col1, col2, col3,col4 = st.columns(4)

    with col1:
        st.header("Un chien")
        st.image("https://www.rustica.fr/images/chien-bouledogue-anglais-l790-h526.png.webp")

    with col2:
        st.header("Un autre chien")
        st.image("https://images.ctfassets.net/denf86kkcx7r/34xqsOLARAnleIEyMre3CQ/97da0341c99a05fbaa2592f951ea0102/chien_le_plus_laid_du_monde")

    with col3:
        st.header("encore un chien")
        st.image("https://img.buzzfeed.com/buzzfeed-static/static/2024-10/23/18/asset/c621d899ac03/sub-buzz-448-1729708553-3.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto")

    with col4:
        st.header("toujours un chien")
        st.image("https://seriescheries.com/wp-content/uploads/2016/12/divorce3.jpg?w=584")


