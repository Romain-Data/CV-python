from typing import Dict, Literal, List, Optional
# Je fais un import localisé ligne 176 pour éviter un import circulaire


class Experience:
    def __init__(
            self,  
            entreprise: str,
            poste:str,
            debut:str,
            fin: Optional[str] = None,
            description: Optional[str] = None
            ) -> None:
        self.entreprise = entreprise
        self.poste = poste
        self.debut = debut
        self.fin = fin or "Présent"
        self.description = description


class Formation:
    def __init__(
            self,
            diplome: str,
            etablissement: str,
            annee: str | int,
            description: Optional[str] = None
            ) -> None:
        self.diplome = diplome
        self.etablissement = etablissement
        self.annee = str(annee)
        self.description = description


class Projet:
    def __init__(
            self,
            nom: str,
            description: str,
            equipe: List[str] = []
            ):
        self.nom = nom
        self.description = description
        self.equipe = equipe


class Professionnel:
    def __init__(self, nom:str, prenom:str, age:int, titre:str, email: str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.titre = titre
        self.experiences: List[Experience] = []
        self.competences: Dict[str, List[Dict[str, Optional[str]]]] = {
            "techniques": [],
            "soft_skills": [],
            "langues": []
        }
        self.formations: List[Formation] = []
        self.projets: List[Projet] = []
        self.certifications: List[Dict[str, str]] = []
        self.contacts: Dict[str, str] = {"email": email}
        self.disponibilite: bool = True
        self.passions: List[Dict[str, str|None]] = []
        self.score_apprentissage: float = 95  

    def ajouter_contact(self, canal, contact):
        self.contacts[canal] = contact
        print(f"Votre contact {canal} a bien été ajouté")


    def ajouter_experience(self, experience: Experience)-> None:
        """
        Ajouter une expérience professionnelle
        """
        self.experiences.append(experience)
        print(f"Expérience ajoutée : {experience.poste} chez {experience.entreprise}")


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
            raise ValueError(f"Catégorie {categorie} non reconnue")
        

    def ajouter_formation(self, formation: Formation) -> None:
        """Ajouter une nouvelle formation académique"""
        self.formations.append(formation)
        print(f"Nouvelles formation ajoutée : {formation.diplome} délivré par {formation.etablissement}")


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
        temps_effectif = round(temps_apprentissage * efficacite, 1)

        print(f"Apprentissage de {nouvelle_competence}...")
        print(f"Temps d'apprentissage estimé : {temps_effectif}h")
        self.ajouter_competence(nouvelle_competence)

        # Augmentation du score d'apprentissage avec l'expérience
        self.score_apprentissage = min(100, self.score_apprentissage + 0.5)
        return f"✅ {nouvelle_competence} maitrisé en {temps_effectif}h !"
    

    def contacter(self, canal: str) -> str:

        """Obtenir les informations de contact"""
        if self.contacts["email"]:
            try:
                return f"Vous pouvez me contacter via {canal}: {self.contacts[canal]}"
            except KeyError:
                return f"Cette méthode n'est pas disponible. Je suis joignable par email: {self.contacts["email"]}"
        else:
            return "Je n'ai pas renseigné de coordonnées"
    

    def ajouter_projet(
            self,
            projet: Projet
        ) -> str:
        """
        Simuler la collaboration sur un projet
        Ajouter le projet au portfolio
        """
        print(f"Collaboration initié sur le projet : {projet.nom}")
        if projet.equipe:
            print(f"Équipe : {', '.join(projet.equipe)}")
        self.projets.append(projet)
        return(f"Projet {projet.nom} ajouté au portfolio")


    def mettre_a_jour_disponibilite(self, disponible: bool = True) -> str:
        self.disponibilite = disponible
        status = "disponible" if disponible else "non disponible"
        return f"Statut mis à jour : {status} pour de nouvelles opportunités"
    

    def voir_cv(self, mode = 'auto', return_content=False) -> None:
        """Générer un cv complet
        mode :
        - auto : affiche via IPython si dispo, sinon print
        - texte : print brut
        - jupyter : force IPython Markdown
        Args:
            mode (str): Mode d'affichage
            return_content (bool): Si True, retourne le contenu au lieu de l'afficher
        
        Returns:
            str or None: Le contenu du CV si return_content=True, sinon None
        """
        from cv_formatter import CVFormatter
        formatter = CVFormatter(self)

        if return_content:
            return formatter.generer_markdown()
        else:
            formatter.afficher(mode)
            return None

    
    def sauvegarder_cv(self, chemin: str = 'README.md') -> None:
        from cv_formatter import CVFormatter
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(CVFormatter(self).generer_markdown())
        
    
    def __str__(self) -> str:
        """Représentation textuelle de la classe"""
        return f"{self.prenom} {self.nom}, {self.age} ans - {self.titre}"

    