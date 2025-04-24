import streamlit as st #type:ignore
from professionnel import Formation
from components.utils import reset_form_fields

ss = st.session_state

def gestion_formations():
    st.subheader("Ajouter une formation")

    with st.form(key="form_formation"):
        diplome = st.text_input("Diplôme", key="form_diplome")

        col1, col2 = st.columns([2,1])

        with col1:
            ecole = st.text_input("École", key="form_ecole")
        
        with col2:
            annee = st.number_input("Année d'obtention", min_value=1950, max_value=2025, value = 2025, step=1)

        description = st.text_area("Desciption (optionnelle)", key="form_description_formation")
        submit = st.form_submit_button("Ajouter cette formation")

        if submit:
            if diplome and ecole and annee :
                formation = Formation(diplome, ecole, annee, description if description else None)
                ss.professionnel.ajouter_formation(formation)
                st.success(f"Formation {diplome} ajoutée avec succès")
            else:
                st.error("Veuillez remplir les champs obligatoires")

    afficher_formation()


def afficher_formation():
    """Afficher la liste des formations déjà ajoutées"""
    if not ss.professionnel or not ss.professionnel.formations:
        st.info("Aucune formation enregistrée")
        return
        
    st.subheader("Formations enregistrées")
    for i, formation in enumerate(ss.professionnel.formations):
        with st.expander(f"{formation.diplome} - {formation.etablissement} ({formation.annee})"):
            st.write(f"**Description:** {formation.description or 'Aucune description'}")