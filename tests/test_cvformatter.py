from cv_formatter import CVFormatter
import pytest #type: ignore
from professionnel import Experience, Formation, Professionnel, Projet


@pytest.fixture
def profil_minimal():
    """Créer une instance minimale de Professionnel pour les tests"""
    return Professionnel("nom", "prenom", 25, "titre", "test@test.com")

@pytest.fixture
def profil_complet():
    """Créer une instance complet de Professionnel pour les tests"""
    profil = Professionnel("Collery", "Romain", 32, "Développeur Python", "romain.collery@protonmail.com")
    profil.ajouter_contact("linkedin", "https://www.linkedin.com/in/romain-collery-4178b1130/")
    profil.ajouter_contact("github", "https://github.com/Romain-Data")
    profil.ajouter_competence("Python", niveau="Intermédiaire")
    profil.ajouter_competence("SQL", niveau="Intermédiaire")
    profil.ajouter_competence("Résolution de problème", categorie="soft_skills")
    profil.ajouter_competence("Français", categorie="langues", niveau="Natif")
    profil.ajouter_formation(Formation("Data Analyst", "Wild Code School", 2025))
    profil.ajouter_formation(Formation("BTS Audiovisuel", "Lycée des Arènes", 2013))
    profil.ajouter_projet(Projet(
    "Production d'un tableau de bord de vente",
    """- extraction / nettoyage de données *(SQL)*
- création d’insights significatifs *(SQL/DAX)*
- création d’un dashboard clair *(Power BI)*"""))
    profil.ajouter_experience(Experience("Auto-entreprise","Consultant Notion","2020",
        description="""- développement de solutions personnalisées de gestion de données
- création de dashboards et d'outils d'analyse automatisés"""))
    profil.ajouter_passion(
    "Tennis",
    "15 ans de pratique en compétition et ancien président de club")

    return profil


@pytest.fixture
def formatter_minimal(profil_minimal):
    """Créer une instance de CVFormatter avec un profil minimal pour les tests"""
    return CVFormatter(profil_minimal)


def test_cvformatter_init(profil_minimal):
    """Test d'initialisation"""
    formatter = CVFormatter(profil_minimal)

    assert formatter.pro == profil_minimal


def test_cvformatter_init_avec_mauvais_parametre():
    """Test que le formatter rejette les objets non-Professionnel"""

    objets_invalides = [
        "une string",
        123,
        {"type" : "dictionnaire"},
        None
    ]

    for objet in objets_invalides:
        with pytest.raises(TypeError):
            CVFormatter(objet)

        
def test_cvformatter_generer_markdown_non_vide(formatter_minimal):
    """Test que la generer_markdown() ne renvoit pas une chaîne vide"""

    assert formatter_minimal.generer_markdown()


def test_cvformatter_generer_markdown_toutes_sections_presentes(profil_complet):
    formatter = CVFormatter(profil_complet)

    contenu = formatter.generer_markdown()

    assert "### À propos" in contenu
    assert "### Projets" in contenu
    assert "### Formations" in contenu
    assert "### Compétences" in contenu
    assert "### Expériences" in contenu
    assert "### Passions" in contenu


def test_cvformatter_afficher_differents_mode(formatter_minimal, capsys):
    modes = ['auto', 'texte']
    for mode in modes:
        formatter_minimal.afficher(mode)
        capture = capsys.readouterr()

        assert "# prenom nom" in capture.out
        assert "## titre" in capture.out
        assert "### À propos" in capture.out
        assert "Professionnel passionné avec une expertise en " in capture.out
        assert "### Compétences" in capture.out

        assert len(capture.out) > 0


def test_cvformatter_afficher_sans_ipython(formatter_minimal, monkeypatch, capsys):
    """Test le fonctionnement de afficher() sans la présence de IPython"""

    # Simule l'absence de IPython et renvoie une ImportError
    def mock_import(name, *args, **kwargs):
        if name == "IPython.display":
            raise ImportError
        return __import__(name, *args, **kwargs)

    monkeypatch.setattr("builtins.__import__", mock_import)
    
    formatter_minimal.afficher('auto')

    capture = capsys.readouterr()

    assert "# prenom nom" in capture.out
    assert "## titre" in capture.out


def test_cvformatter_afficher_avec_ipython(formatter_minimal, monkeypatch, mocker):
    """Test le fonctionnement de afficher() avec la présence de IPython"""

    # Crée un mock pour IPython et ses fonctions
    mock_display = mocker.MagicMock()
    mock_markdown = mocker.MagicMock()

    mock_ipython_display = mocker.MagicMock()
    mock_ipython_display.display = mock_display
    mock_ipython_display.Markdown = mock_markdown

    # Simule l'absence de IPython et renvoie une ImportError
    def mock_import(name, *args, **kwargs):
        if name == "IPython.display":
            return mock_ipython_display
        return __import__(name, *args, **kwargs)

    monkeypatch.setattr("builtins.__import__", mock_import)
    
    formatter_minimal.afficher('jupyter')

    mock_markdown.assert_called_once()

    mock_content = mock_markdown.call_args[0][0]
    assert "# prenom nom" in mock_content
    mock_display.assert_called_once_with(mock_markdown.return_value)