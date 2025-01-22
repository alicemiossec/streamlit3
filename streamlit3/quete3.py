import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# Définir la configuration directement dans le code
config = {
    'credentials': {
        'usernames': {
            'alice': {
                'username': 'alice',
                'password': 'bigornot05',  # Mot de passe en clair (attention dans un vrai projet, il faut le hasher)
                'name': 'Alice',  # Ajouter un champ 'name'
                'email': 'alice@example.com'  # Ajouter un champ 'email' (optionnel mais souvent utile)
            }
        }
    },
    'cookie': {
        'name': 'streamlit_auth_cookie',
        'key': 'a_very_secret_key',  # À remplacer par une vraie clé secrète
        'expiry_days': 7
    }
}

# Initialiser l'authentification
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

st.write("Pour visiter ma page: login: alice, mdp: bigornot05")

# Tenter la connexion
authenticator.login()

# Fonction d'accueil
def accueil():
    st.title("Bienvenue sur ma page d'Alice")

# Vérifier l'état de l'authentification
if st.session_state.get("authentication_status"):
    accueil()  # Si authentifié, afficher la page d'accueil

    # Menu de navigation
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"],
        orientation="horizontal"
    )

    if selection == "Accueil":
        st.write("Bienvenue dans mon univers")
    
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
        # Affichage des photos
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Un chien")
            st.image("https://www.rustica.fr/images/chien-bouledogue-anglais-l790-h526.png.webp")
        
        with col2:
            st.header("Un autre chien")
            st.image("https://images.ctfassets.net/denf86kkcx7r/34xqsOLARAnleIEyMre3CQ/97da0341c99a05fbaa2592f951ea0102/chien_le_plus_laid_du_monde")
        
        with col3:
            st.header("Encore un chien")
            st.image("https://img.buzzfeed.com/buzzfeed-static/static/2024-10/23/18/asset/c621d899ac03/sub-buzz-448-1729708553-3.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto")
        
        with col4:
            st.header("Et un nouveau chien")
            st.image("https://seriescheries.com/wp-content/uploads/2016/12/divorce3.jpg?w=584")

    # Menu de déconnexion
    with st.sidebar:
        if st.session_state['authentication_status']:
            st.radio("Vous souhaitez vous déconnecter", options=["Oui", "Non"], index=1)
            if st.radio == "Oui":
                authenticator.logout()

elif st.session_state.get("authentication_status") is False:
    st.error("L'username ou le mot de passe est incorrect.")
elif st.session_state.get("authentication_status") is None:
    st.warning("Les champs username et mot de passe doivent être remplis.")


