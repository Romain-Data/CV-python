import pytest
from professionnel import Experience

def test_experience_init_tous_parametres():
    """Test d'initialisation avec tous les paramètres"""
    experience = Experience("Entreprise", "poste", "date debut", "date fin", "description")

    assert experience.entreprise == "Entreprise"
    assert experience.poste == "poste"
    assert experience.debut == "date debut"
    assert experience.fin == "date fin"
    assert experience.description == "description"


def test_experience_init_sans_parametres_optionnels():
    """Test d'initialisation sans les paramètres optionnels"""
    experience = Experience("Entreprise", "poste", "date debut")

    assert experience.entreprise == "Entreprise"
    assert experience.poste == "poste"
    assert experience.debut == "date debut"
    assert experience.fin == "Présent"
    assert experience.description is None