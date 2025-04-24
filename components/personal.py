import streamlit as st #type: ignore
from components.utils import validate_filed
from professionnel import Professionnel

def informations_personnelles():
    st.header("Informations personnelles")

    col1, col2 = st.columns(2)

    with col1:
        prenom = st.text_input("Prenom", key="prenom")

    with col2:
        nom = st.text_input("Nom", key="nom")

    col1, col2 = st.columns([2,1])

    with col1:
        titre = st.text_input("Titre", key="titre")

    with col2:
        age = st.number_input("Âge", min_value=16, max_value=100, step=1, key="age")
    
    email = st.text_input("Email", key="email")
    email_valide = validate_filed(
        "email",
        r"^[a-zA-Z0-9._%±]+@[a-zA-Z0-9._%±]+.[a-z]{2,}$",
        "Format d'email invalide"
    )
    
    if st.button("Enregistrer les informations personnelles"):
        if nom and prenom and titre and age and email_valide:
            st.session_state.professionnel = Professionnel(nom, prenom, age, titre, email)
            st.success("Informations personnelles enregistrées")
        else:
            st.error("Veuillez remplir tous les champs")