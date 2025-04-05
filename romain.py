from IPython.display import display, Markdown
from typing import Dict, Literal, List, Optional
import os

clear = lambda: os.system('clear')

def printmd(text):
    display(Markdown(text))


class Professionnel:
    def __init__(self, nom:str, prenom:str, age:int, titre:str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.titre = titre
        self.experiences: List[Dict[str, str | None]] = []
        self.competences: Dict[str, List[Dict[str, str]]] = {
            "techniques": [],
            "soft_skills": [],
            "langues": []
        }
        self.formations: list[dict] = []
        self.projets: list[dict] = []
        self.certifications: List[Dict[str, str]] = []
        self.contacts = {
            "email": "",
            "linkedin": "",
            "github": ""
        }
        self.disponibilite: bool = True
        self.objectifs_carriere: list[str] = []
        self.passions: List[Dict[str, str | None]]= []
        self.score_apprentissage: float = 95  


    def ajouter_une_experience(
            self,
            entreprise: str,
            poste:str,
            debut:str,
            fin: Optional[str] = None,
            description: Optional[str] = None
        ) -> None:
        """
        Ajouter une expérience professionnelle
        """
        self.experiences.append({
            "entreprise": entreprise,
            "poste": poste,
            "début": debut,
            "fin": fin if fin else "Présent",
            "description": description
        })
        print(f"Expérience ajoutée : {poste} chez {entreprise}")


    def ajouter_competence(
            self,
            competence:str,
            categorie: str = "techniques",
            niveau: Optional[str] = None
            ) -> None:
        
        """Ajouter une nouvelle compétence avec un niveau optionnel"""

        if categorie in self.competences:
            self.competences[categorie].append({
                "nom": competence,
                "niveau": niveau
            })
            print(f"Nouvelle compétence ajoutée : {competence}")
        else:
            print(f"Catégorie {categorie} non reconnue")
        

    def ajouter_formation(
            self,
            etablissement: str,
            diplome: str,
            annee: str | int,
            description: Optional[str] = None
        ) -> None:

        """Ajouter une nouvelle formation académique"""

        self.formations.append({
            "etablissement": etablissement,
            "diplome": diplome,
            "annee": str(annee),
            "description": description
        })
        print(f"Nouvelles formation ajoutée : {diplome} délivré par {etablissement}")


    def ajouter_passion(
            self,
            nom: str,
            description: Optional[str] = None
        ) -> None:

        """Ajouter une nouvelle passion"""

        self.passions.append({
            "nom": nom,
            "description": description
        })
        print(f"Nouvelle passion ajoutée : {nom}")


    def apprendre(
            self,
            nouvelle_competence: str, 
            temps_apprentissage: float
        ) -> str:

        """
        Simuler l'apprentissage d'une nouvelle compétence
        et estime le temps d'apprentissage en fonction de l'attribut 'score_apprentissage'
        """

        efficacite = self.score_apprentissage / 100
        temps_effectif = temps_apprentissage * efficacite

        print(f"Apprentissage de {nouvelle_competence}...")
        print(f"Temps d'apprentissage estimé : {temps_effectif}h")
        self.ajouter_competence(nouvelle_competence)

        # Augmentation du score d'apprentissage avec l'expérience
        self.score_apprentissage = min(100, self.score_apprentissage) + 0.5
        return f"✅ {nouvelle_competence} maitrisé en {temps_effectif}h !"
    

    def contacter(self, canal: Literal['Linkedin', 'email', 'github']) -> str:

        """Obtenir les informations de contact"""
        
        try:
            return f"Vous pouvez me contacter vie {canal}: {self.contacts[canal.lower()]}"
        except KeyError:
            return f" Cette méthode n'est pas disponible. Je suis joignable par email: {self.contacts["email"]}"
    

    def collaborer(
            self,
            projet: str,
            equipe: Optional[List[str]] = [],
            description: Optional[str] = None
        ) -> str:
        """
        Simuler la collaboration sur un projet
        Ajouter le projet au portfolio
        """
        print(f"Collaboration initié sur le projet : {projet}")
        print(f"Équipe : {", ".join(equipe)}")

        self.projets.append({"nom": projet, "equipe": equipe, "description": description})
        return(f"Projet {projet} ajouté au portfolio")


    def mettre_a_jour_disponibilite(self, disponible: bool = True) -> str:
        self.disponibilite = disponible
        status = "disponible" if disponible else "non disponible"
        return f"Statut mis à jour : {status} pour de nouvelles opportunités"
    

    def voir_cv(self) -> str:

        """Générer un cv complet"""

        clear()

        competences_principales: List[str] = [
            competence['nom'] for competence in self.competences["techniques"][:3]
            if isinstance(competence, dict) and "nom" in competence
        ]
        
        experience_recente = self.experiences[:2] if self.experiences else []

        cv = f"# {self.prenom} {self.nom}\n"
        cv += f"## {self.titre}\n\n"
        cv += "### À propos\n"
        cv += f"Professionnel passionné avec une expertise en {", ".join(competences_principales)}\n\n"

        # Ajouter projets
        if self.projets:
            cv += f"### Projets"
            for projet in self.projets:
                cv += f"\n**{projet['nom']}**\n"
                if projet['equipe']:
                    cv += f"*avec {projet['equipe']}*\n"
                if projet['description']:
                    cv += f"{projet['description']}\n"

        # Ajouter formations
        if self.formations:
            cv += "\n### Formations \n\n"
            for formation in self.formations:
                cv += f"{formation['diplome']} délivré par {formation['etablissement']} en {formation['annee']}"
                if formation['description']:
                    cv += f"\n   *{formation['description']}*\n"
        
        
        # Ajouter certification si présente
        if self.certifications:
            cv += "\n### Certifications\n"
            for certif in self.certifications:
                cv += f"- {certif["nom"]} - {certif["organisme"]} {certif["date_d'obtention"]}\n"

        # Ajouter compétences par catégorie
        cv += "\n### Compétences\n"
        for categorie, comps in self.competences.items():
            if comps:
                cv += f"\n**{categorie.capitalize()}**: \n"
                competence = [
                    f"- {comp["nom"]}  {"- " + comp["niveau"] if comp["niveau"] else ""}\n"
                    for comp in comps
                    ]
    
                cv += "".join(competence)

        # Ajouter expériences récentes
        if experience_recente:
                cv += "### Expériences récentes\n\n"
                for exp in experience_recente:
                    cv += f"- {exp['poste']} chez {exp['entreprise']} {exp['début']} - {exp['fin']}\n"

        # Ajouter passions
        if self.passions:
            cv += f"### Passions\n"
            for passion in self.passions:
                cv += f"{passion['nom']} {"- " + passion["description"] if passion["description"] else ""}"

        return printmd(cv)
    
    def __str__(self) -> str:
        """Représentation textuelle de la classe"""
        return f"{self.prenom} {self.nom}, {self.age} ans - {self.titre}"

    

if __name__ == "__main__":
    moi = Professionnel("Collery", "Romain", 32, "Développeur Python")

    moi.contacts = {
        "email": "romain.collery@protonmail.com",
        "LinkedIn": "https://www.linkedin.com/in/romain-collery-4178b1130/",
        "github": "https://github.com/Romain-Data"
    }

    moi.ajouter_competence("Python", niveau="Intermédiaire")
    moi.ajouter_competence("SQL", niveau="Intermédiaire")
    moi.ajouter_competence("PowerBI", niveau="Intermédiaire")
    moi.ajouter_competence("Machine learning", niveau="Intermédiaire")
    moi.ajouter_competence("Cloud", niveau="Débutant")
    moi.ajouter_competence("Capacité d'apprentissage", categorie="soft_skills")
    moi.ajouter_competence("Résolution de problème", categorie="soft_skills")
    moi.ajouter_competence("Français", categorie="langues", niveau="Natif")
    moi.ajouter_competence("Anglais", categorie="langues", niveau="Courant")

    moi.ajouter_formation("Wild Code School", "Data Analyst", 2025)
    moi.ajouter_formation("Lycée des Arènes", "BTS Audiovisuel", 2013)

    moi.collaborer(
        "Production d'un tableau de bord de vente",
        description="""- extraction / nettoyage de données *(SQL)*
- création d’insights significatifs *(SQL/DAX)*
- création d’un dashboard clair *(Power BI)*"""
    )
    moi.collaborer(
        "Création d'un bot d'aide à la correction",
        description=("""- automatisation de la navigation web *(Helium)*
- webscraping *(BeautifulSoup)*
- utilisation de l'API Gemini
- Programmation Orientée objet""")
    )

    moi.ajouter_une_experience(
        "Auto-entreprise",
        "Consultant Notion",
        "2020",
        description="""- développement de solutions personnalisées de gestion de données
        - création de dashboards et d'outils d'analyse automatisés"""
    )
    moi.ajouter_une_experience(
        "Équipage and Co",
        "Responsable Logistique et Digital",
        "mai 2022",
        "février 2024",
        """- suivi de stock
- organisation des équipes opérationnelles
- mise en place de process pour réduire les erreurs de 10%"""
)
    
    moi.ajouter_passion(
        "Tennis",
        "15 ans de pratique en compétition et ancien président de club"
    )

    moi.voir_cv()