import streamlit as st #type:ignore

ss = st.session_state

def gestion_competences():
    st.subheader("Ajouter une compétence")

    # Initialiser la session state
    if "comp_submitted" not in st.session_state:
        st.session_state.comp_submitted = False
    
    # Réinitialiser les champs si une soumission a été faite
    if st.session_state.comp_submitted:
        st.session_state.comp_nom = ""
        st.session_state.comp_niveau = None
        st.session_state.comp_submitted = False
    
    # Initialiser les valeurs si nécessaire
    if "comp_type" not in st.session_state:
        st.session_state.comp_type = "Technique"
    if "comp_nom" not in st.session_state:
        st.session_state.comp_nom = ""
    if "comp_niveau" not in st.session_state:
        st.session_state.comp_niveau = None
    
    col1, col2 = st.columns(2)
    
    with col1:
        categories = ['Technique', "Soft skill", "Langue"]
        type_competence = st.radio("Type", options=categories, key=f"comp_type")
    
    with col2:
        nom = st.text_input("Compétence", value=ss.comp_nom, key=f"comp_nom")
        
        # Options qui changent en fonction du type
        if type_competence == "Langue":
            niveau_options = ["Maternelle", "Courant", "Débutant"]
        else:
            niveau_options = ["Expert", "Confirmé", "Débutant"]
        
        niveau = st.selectbox(
            "Niveau", 
            options=niveau_options, 
            index=None, 
            key=f"comp_niveau", 
            placeholder="Sélectionnez un niveau"
        )
    
    if st.button("Ajouter cette compétence", key=f"comp_submit"):
        if nom and type_competence and niveau:
            type_format = {
                "Technique": "techniques",
                "Soft skill": "soft_skills",
                "Langue": "langues"}
            ss.professionnel.ajouter_competence(nom, type_format[type_competence], niveau)
            ss.comp_submitted = True
            st.success(f"Compétence {nom} ajoutée avec succès!")
            st.rerun()
        else:
            st.error("Veuillez remplir tous les champs obligatoires")

    afficher_competences()


def afficher_competences():
    """Afficher la liste des compétences déjà ajoutées"""
    if not ss.professionnel or not any(ss.professionnel.competences.values()):
        st.info("Aucune compétence enregistrée")
        return

    else:   
        st.subheader("Compétences enregistrées")
        for categorie, competences in ss.professionnel.competences.items():
            categorie_format = categorie.replace('_', ' ').capitalize()
            with st.expander(f"**{categorie_format}**"):
                for competence in competences:
                    st.write(f"{competence['nom']} - niveau {competence['niveau']}")