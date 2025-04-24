from cv_formatter import CVFormatter
from professionnel import Professionnel
from components.competences import gestion_competences
from components.experiences import gestion_experiences
from components.formations import gestion_formations
from components.passions import gestion_passions
from components.personal import informations_personnelles
from components.projets import gestion_projets
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
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Compétences", "Formations", "Expériences", "Projets", "Centres d'intérêt"])

        with tab1: 
            gestion_competences()
        
        with tab2:      
            gestion_formations()

        with tab3:
            gestion_experiences()
            
        with tab4:
            gestion_projets()

        with tab5:
            gestion_passions()

if __name__=="__main__":
    main()
    st.write(ss)

    st.write(ss.professionnel.voir_cv(return_content=True))