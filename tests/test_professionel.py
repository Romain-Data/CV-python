import pytest
from professionnel import Experience, Formation, Professionnel, Projet

@pytest.fixture(scope="function")
def professionnel_standard():
    """Créer une instance standard de Professionnel pour les tests"""
    return Professionnel("nom", "prenom", 25, "titre", "test@test.com")


@pytest.fixture
def formation_standard():
    """Créer une instance standard de Formation pour les tests"""
    return Formation("diplôme", "école", 2025, "description")


@pytest.fixture
def experience_standard():
    """Créer une instance standard de Experience pour les tests"""
    return Experience("Entreprise", "poste", "date debut", "date fin", "description")


@pytest.fixture
def projet_standard():
    """Créer une instance standard de Projet pour les tests"""
    return Projet("nom", "description", ["membre 1", "membre 2"])


def test_professionel_init(professionnel_standard):
    """Test d'initialisation"""
   
    assert professionnel_standard.nom == "nom"
    assert professionnel_standard.prenom == "prenom"
    assert professionnel_standard.age == 25
    assert professionnel_standard.titre == "titre"

    assert professionnel_standard.competences == {
        "techniques": [],
        "soft_skills": [],
        "langues": []
    }
    assert professionnel_standard.experiences == []
    assert professionnel_standard.formations == []
    assert professionnel_standard.certifications == []
    assert professionnel_standard.contacts == {"email": "test@test.com"}
    assert professionnel_standard.disponibilite == True
    assert professionnel_standard.passions == []
    assert professionnel_standard.score_apprentissage == 95


def test_professionnel_ajout_experience(professionnel_standard, experience_standard):
    """Test l'ajout d'une expérience"""
    professionnel_standard.ajouter_experience(experience_standard)

    assert len(professionnel_standard.experiences) == 1
    assert professionnel_standard.experiences == [experience_standard]


def test_professionnel_ajout_formation(professionnel_standard, formation_standard):
    """Test l'ajout d'une formation"""
    professionnel_standard.ajouter_formation(formation_standard)

    assert len(professionnel_standard.formations) == 1
    assert professionnel_standard.formations == [formation_standard]


def test_professionnel_ajout_competence_technique(professionnel_standard):
    """Test l'ajout d'une competence technique basique"""
    professionnel_standard.ajouter_competence("Python", niveau="débutant")

    assert len(professionnel_standard.competences["techniques"]) == 1
    assert professionnel_standard.competences["techniques"][0]["nom"] == "Python"
    assert professionnel_standard.competences["techniques"][0]["niveau"] == "débutant"


def test_professionnel_ajout_competence_specifique_technique(professionnel_standard):
    """Test l'ajout d'une competence specifique technique"""
    professionnel_standard.ajouter_competence("Python", "techniques", niveau="débutant")

    assert len(professionnel_standard.competences["techniques"]) == 1
    assert professionnel_standard.competences["techniques"][0]["nom"] == "Python"
    assert professionnel_standard.competences["techniques"][0]["niveau"] == "débutant"


def test_professionnel_ajout_competence_soft_skills(professionnel_standard):
    """Test l'ajout d'une competence soft skill"""
    professionnel_standard.ajouter_competence("Communication", "soft_skills", niveau="débutant")

    assert len(professionnel_standard.competences["soft_skills"]) == 1
    assert professionnel_standard.competences["soft_skills"][0]["nom"] == "Communication"
    assert professionnel_standard.competences["soft_skills"][0]["niveau"] == "débutant"


def test_professionnel_ajout_competence_langue(professionnel_standard):
    """Test l'ajout d'une competence linguistique"""
    professionnel_standard.ajouter_competence("Français", "langues", niveau="langue maternelle")

    assert len(professionnel_standard.competences["langues"]) == 1
    assert professionnel_standard.competences["langues"][0]["nom"] == "Français"
    assert professionnel_standard.competences["langues"][0]["niveau"] == "langue maternelle"


def test_professionnel_ajout_competence_sans_niveau(professionnel_standard):
    """Test l'ajout d'une competence technique sans niveau"""
    professionnel_standard.ajouter_competence("Python")

    assert len(professionnel_standard.competences["techniques"]) == 1
    assert professionnel_standard.competences["techniques"][0]["nom"] == "Python"
    assert professionnel_standard.competences["techniques"][0]["niveau"] is None


def test_professionnel_ajout_competence_invalide(professionnel_standard):
    """Vérifie que l'ajout d'une compétence avec une catégorie invalide lèce une exception"""
    
    with pytest.raises(ValueError) as excinfo:
        professionnel_standard.ajouter_competence("Python", categorie="categorie_inexistante")

    assert "non reconnue" in str(excinfo.value).lower()


def test_professionnel_ajout_passion(professionnel_standard):
    """Vérifie que l'ajout d'une passion"""
    professionnel_standard.ajouter_passion("Musique", "pratique de la flute")

    assert len(professionnel_standard.passions) == 1
    assert professionnel_standard.passions[0]["nom"] == "Musique"
    assert professionnel_standard.passions[0]["description"] == "pratique de la flute"


def test_professionnel_ajout_passion_sans_description(professionnel_standard):
    """Vérifie que l'ajout d'une passion sans description"""
    professionnel_standard.ajouter_passion("Musique")

    assert len(professionnel_standard.passions) == 1
    assert professionnel_standard.passions[0]["nom"] == "Musique"
    assert professionnel_standard.passions[0]["description"] is None


def test_professionnel_apprendre_ajoute_competence(professionnel_standard):
    """Vérifie que la méthode apprendre ajoute la compétence"""
    professionnel_standard.apprendre("Python", 10)

    assert len(professionnel_standard.competences["techniques"]) == 1
    assert professionnel_standard.competences["techniques"][0]["nom"] == "Python"
    assert professionnel_standard.competences["techniques"][0]["niveau"] is None


def test_professionnel_apprendre_modification_score_apprentissage(professionnel_standard):
    """Vérifie que la méthode apprendre modifie le score d'apprentissage"""
    professionnel_standard.score_apprentissage == 95

    professionnel_standard.apprendre("Python", 10)
    professionnel_standard.score_apprentissage == 95.5


def test_professionnel_apprendre_modification_temps_apprentissage(professionnel_standard, capsys):
    """Vérifie que le temps d'apprentissage est bien fonction du score d'apprentissage"""
    professionnel_standard.apprendre("Python", 10)
    
    # Capture du print de sortie
    message_sortie = capsys.readouterr()

    assert f"Temps d'apprentissage estimé : 9.5h" in message_sortie.out


def test_professionnel_apprendre_limite_score_apprentissage(professionnel_standard, capsys):
    """Vérifie la limite du score d'apprentissage"""
    professionnel_standard.score_apprentissage = 100
    professionnel_standard.apprendre("Python", 10)
    
    assert professionnel_standard.score_apprentissage == 100


def test_professionnel_contacter(professionnel_standard):
    """Vérifie le retour de la méthode contacter"""

    assert professionnel_standard.contacter("email") == "Vous pouvez me contacter via email: test@test.com"


def test_professionnel_contacter_canal_invalide(professionnel_standard):
    """Vérifie le retour de la méthode contacter pour un canal invalide"""

    assert professionnel_standard.contacter("canal invalide") == "Cette méthode n'est pas disponible. Je suis joignable par email: test@test.com"


def test_professionnel_contacter_aucun_contact(professionnel_standard):
    """Vérifie le retour de la méthode contacter si aucun contact n'est renseigné"""
    professionnel_standard.contacts["email"] = ""
    
    assert professionnel_standard.contacter("email") == "Je n'ai pas renseigné de coordonnées"


def test_professionnel_ajouter_projet(professionnel_standard, projet_standard, capsys):
    """Vérifie si la méthode ajouter_projet ajoute correctement le projet à la liste des projets"""
    professionnel_standard.ajouter_projet(projet_standard)

    message_sortie = capsys.readouterr()

    assert len(professionnel_standard.projets) == 1
    assert professionnel_standard.projets[0].nom == projet_standard.nom
    assert professionnel_standard.projets[0].description == projet_standard.description
    assert professionnel_standard.projets[0].equipe == projet_standard.equipe
    assert "Équipe" in message_sortie.out


def test_professionnel_ajouter_projet_sans_equipe(professionnel_standard, capsys):
    """Vérifie le comportement de la méthode ajouter_projet pour un projet solo"""
    projet = Projet("Projet 1", "description du projet")
    professionnel_standard.ajouter_projet(projet)

    message_sortie = capsys.readouterr()
    assert len(professionnel_standard.projets) == 1
    assert professionnel_standard.projets[0].nom == projet.nom
    assert professionnel_standard.projets[0].description == projet.description
    assert professionnel_standard.projets[0].equipe == []
    assert not "Équipe" in message_sortie.out


def test_professionnel_disponibilite_non_disponible(professionnel_standard):
    """Test si la méthode mettre_à_jour_disponibilite permet de se rendre indisponible"""
    status = professionnel_standard.mettre_a_jour_disponibilite(False)

    assert professionnel_standard.disponibilite == False
    assert status == "Statut mis à jour : non disponible pour de nouvelles opportunités"


def test_professionnel_disponibilite_disponible(professionnel_standard):
    """Test si la méthode mettre_à_jour_disponibilite permet de se rendre disponible"""
    professionnel_standard.mettre_a_jour_disponibilite(False)
    status = professionnel_standard.mettre_a_jour_disponibilite(True)

    assert professionnel_standard.disponibilite == True
    assert status == "Statut mis à jour : disponible pour de nouvelles opportunités"


def test_professionnel_str(professionnel_standard):
    """Test que la méthode __str__ retourne la chaîne de caractères attendue"""

    nom = professionnel_standard.nom
    prenom = professionnel_standard.prenom
    age = professionnel_standard.age
    titre = professionnel_standard.titre

    chaine_attendue = f"{prenom} {nom}, {age} ans - {titre}"

    assert str(professionnel_standard) == chaine_attendue