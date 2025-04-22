
from cv_formatter import CVFormatter
from professionnel import Experience, Formation, Projet, Professionnel
import streamlit as st

ss = st.session_state

# Initialisation du session state
if "professionnel" not in ss:
    ss.professionnel = Professionnel("","",0,"","")
    ss.experiences = []
    ss.formations = []
    ss.projets = []
    ss.competences = []

# Main
st.title("Créateur de CV")
st.subheader("Créer rapidement votre CV au format Markdown")

with st.form(
        "Info_base",
        clear_on_submit= False,
        enter_to_submit = True,
        border = True):
    st.markdown("**Votre identité**")
        
    col_1, col_2 = st.columns(2)

    with col_1 :
        name = st.text_input("Nom", "Dujardin")
        titre = st.text_input("Métier")

    with col_2:
        prenom = st.text_input("Prénom", "Jean")
        age = st.number_input("Âge", step=1)
    


    valider = st.form_submit_button("Valider")
    if valider:
        st.write('Données envoyées')