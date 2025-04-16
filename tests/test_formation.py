import pytest 
from professionnel import Formation

def test_formation_init_tous_parametres():
    """Test d'initialisation avec tous les paramètres"""
    formation = Formation("Test diplôme", "Test école", 2025, "Test description")

    assert formation.diplome == "Test diplôme"
    assert formation.etablissement == "Test école"
    assert formation.annee == "2025"
    assert formation.description == "Test description"


def test_formation_init_sans_description():
    """Test d'initialisation sans description (paramètre optionnel)"""
    formation = Formation("Test diplôme", "Test école", 2025)
    
    assert formation.diplome == "Test diplôme"
    assert formation.etablissement == "Test école"
    assert formation.annee == "2025"
    assert formation.description is None


def test_formation_annee_conversion():
    """Test que l'année est bien convertie en string"""
    formation = Formation("Test", "Test", 2025)
    assert isinstance(formation.annee, str)
    
    formation2 = Formation("Test", "Test", "2025")
    assert isinstance(formation2.annee, str)