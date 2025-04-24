import re
import streamlit as st #type:ignore

ss = st.session_state

def initialiser_session():
    """Initialise les variables de session si nécessaire"""
    if 'professionnel' not in st.session_state:
        st.session_state.professionnel = None


def validate_filed(field_key, pattern, error_message):
    """
    Valide un champ selon un pattern regex
    
    Args:
        field_key (str): Clé du champ dans la session_state
        pattern (str): Expression régulière pour la validation
        error_message (str): Message à afficher en cas d'erreur
    
    Returns:
        bool: True si valide, False sinon
    """

    if field_key not in ss or not ss[field_key]:
        return True
    
    value = ss[field_key]
    is_valid = bool(re.match(pattern, value))

    if not is_valid:
        st.error(error_message)
    
    return is_valid


def reset_form_fields(prefix):
    """Réinitialise les champs de formulaire avec un préfixe commun"""
    for key in list(st.session_state.keys()):
        if key.startswith(prefix):
            st.session_state[key] = ""