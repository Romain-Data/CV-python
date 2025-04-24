import streamlit as st #type:ignore
from professionnel import Experience
from components.utils import reset_form_fields

ss = st.session_state

def gestion_experiences():
    st.subheader("Ajouter une expérience")

    with st.form(key="form_experience"):
        poste = st.text_input("Poste", key="form_poste")
        entreprise = st.text_input("Entreprise", key="form_entreprise")

        col1, col2 = st.columns(2)

        with col1:
            debut = st.date_input("Début", key="form_debut", format="DD/MM/YYYY")
        
        with col2:
            fin = st.date_input("Fin (optionnelle)", key="form_fin", format="DD/MM/YYYY")

        description = st.text_area("Desciption (optionnelle)", key="form_description_experience")
        submit_xp = st.form_submit_button("Ajouter cette expérience")

        if submit_xp:
            if poste and entreprise and debut :
                experience = Experience(entreprise, poste, debut, fin if fin else None)
                ss.professionnel.ajouter_experience(experience)
                st.success(f"Experience {poste} chez {entreprise} ajoutée avec succès")
            else:
                st.error("Veuillez remplir les champs obligatoires")

    afficher_experiences()


def afficher_experiences():
    """Afficher la liste des experiences déjà ajoutées"""
    if not ss.professionnel or not ss.professionnel.experiences:
        st.info("Aucune expérience enregistrée")
        return
        
    st.subheader("Expériences enregistrées")
    for experience in ss.professionnel.experiences:
        with st.expander(f"{experience.poste} - {experience.entreprise} ({experience.debut} - {experience.fin})"):
            st.write(f"**Description:** {experience.description or 'Aucune description'}")