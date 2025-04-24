from components.utils import increment_form_counter, get_form_id
import streamlit as st #type:ignore

ss = st.session_state

def gestion_passions():
    st.subheader("Ajouter un centre d'intérêt")

    form_id = get_form_id("passions")

    with st.form(key=form_id):
        nom = st.text_input("Nom", key="form_passion_nom")

        description = st.text_area("Desciption (optionnelle)", key="form_passion_description")
        submit = st.form_submit_button("Ajouter ce centre d'intérêt")

        if submit:
            if nom :
                ss.professionnel.ajouter_passion(nom, description if description else None)
                st.success(f"Centre d'intérêt {nom} ajouté avec succès")
                increment_form_counter("passion")
                st.rerun()
            else:
                st.error("Veuillez remplir les champs obligatoires")

    afficher_passions()


def afficher_passions():
    """Afficher la liste des centres d'intérêt déjà ajoutés"""
    if not ss.professionnel or not ss.professionnel.passions:
        st.info("Aucun centre d'intérêt enregistré")
        return
        
    st.subheader("Centres d'intérêt enregistrés")
    for passion in ss.professionnel.passions:
        with st.expander(passion['nom']):
            st.write(f"**Description:** {passion['description'] or 'Aucune description'}")