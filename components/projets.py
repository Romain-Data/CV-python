import streamlit as st #type:ignore
from professionnel import Projet
from components.utils import increment_form_counter, get_form_id

ss = st.session_state

def gestion_projets():
    st.subheader("Ajouter une projet")

    form_id = get_form_id("projet")

    with st.form(key=form_id):
        nom = st.text_input("Nom", key="form_projet_nom")
        equipe = st.text_input("Equipe (optionnelle)", placeholder="Pierre, Paul", key="form_projet_equipe")
        equipe = equipe.split(', ')

        description = st.text_area("Desciption", key="form_projet_description")
        submit_projet = st.form_submit_button("Ajouter ce projet")

        if submit_projet:
            if nom and description :
                projet = Projet(nom, description, equipe if equipe else [])
                ss.professionnel.ajouter_projet(projet)
                st.success(f"Projet {nom} ajouté avec succès")
                increment_form_counter("projet")
            else:
                st.error("Veuillez remplir les champs obligatoires")

    afficher_projets()


def afficher_projets():
    """Afficher la liste des projets déjà ajoutés"""
    if not ss.professionnel or not ss.professionnel.projets:
        st.info("Aucun projet enregistré")
        return
        
    st.subheader("Projets enregistrées")
    for projet in ss.professionnel.projets:
        with st.expander(f"{projet.nom}"):
            if projet.equipe:
                st.write(f"Avec {', '.join(projet.equipe)}")
            st.write(f"**Description:** {projet.description or 'Aucune description'}")