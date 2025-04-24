<<<<<<< Updated upstream

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
=======
from cv_formatter import CVFormatter
from professionnel import Professionnel
from components.formations import gestion_formations
from components.experiences import gestion_experiences
from components.personal import informations_personnelles
from components.utils import initialiser_session
import streamlit as st # type: ignore


ss = st.session_state

def main():
    st.title("Créateur de CV")
    st.subheader("Créer facilement votre CV au format Markdown")

    # Initialisation
    initialiser_session()

    # Interface principale
    informations_personnelles()

    if ss.professionnel:
        tab1, tab2, tab3 = st.tabs(["Formations", "Expériences", "Projets"])

        with tab1:
            gestion_formations()
        
        with tab2:
            gestion_experiences()

if __name__=="__main__":
    main()
    st.write(ss)
>>>>>>> Stashed changes
