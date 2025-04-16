import pytest
from professionnel import Projet

@pytest.fixture
def projet_standard():
    """Créer une instance standard de Projet pour les tests"""
    return Projet("nom", "description", ["membre 1", "membre 2"])


def test_projet_init_tous_parametres():
    """Test d'initialisation avec tous les paramètres"""

    assert projet_standard.nom == "nom"
    assert projet_standard.description == "description"
    assert projet_standard.equipe == ["membre 1", "membre 2"]

    
def test_projet_equipe_contient_que_des_string():
    """Test que chaque élément de la liste équipe soit une string"""

    non_string = [membre for membre in projet_standard.equipe if not isinstance(membre, str)]
    assert len(non_string) == 0, f"Ces éléments ne sont pas des strings : {non_string}"

