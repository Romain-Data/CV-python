from professionnel import Professionnel
from typing import List


class CVFormatter:
    def __init__(self, professionnel: Professionnel):
        self.pro = professionnel


    def generer_markdown(self):
        """Générer un cv complet"""

        competences_principales: List[str] = [
            competence['nom'] for competence in self.pro.competences['techniques'][:3]
            if isinstance(competence, dict) and "nom" in competence
        ]
        
        experience_recente = self.pro.experiences[:2] if self.pro.experiences else []

        cv = f"# {self.pro.prenom} {self.pro.nom}\n"
        cv += f"## {self.pro.titre}\n\n"
        cv += "### À propos\n"
        cv += f"Professionnel passionné avec une expertise en {', '.join(competences_principales)}\n\n"

        # Ajouter projets
        if self.pro.projets:
            cv += f"### Projets"
            for projet in self.pro.projets:
                cv += f"\n**{projet.nom}**\n"
                if projet.equipe:
                    cv += f"*avec {', '.join(projet.equipe)}*\n"
                if projet.description:
                    cv += f"{projet.description}\n"

        # Ajouter formations
        if self.pro.formations:
            cv += "\n### Formations \n\n"
            for formation in self.pro.formations:
                cv += f"{formation.diplome} délivré par {formation.etablissement} en {formation.annee} \n\n"
                if formation.description:
                    cv += f"*{formation.description}*\n"
        
        
        # Ajouter certification si présente
        if self.pro.certifications:
            cv += "\n### Certifications\n"
            for certif in self.pro.certifications:
                cv += f"- {certif['nom']} - {certif['organisme']} {certif['date_obtention']}\n"

        # Ajouter compétences par catégorie
        cv += "\n### Compétences\n"
        for categorie, comps in self.pro.competences.items():
            if comps:
                cv += f"\n**{categorie.capitalize()}**: \n"
                competence = [
                    f"- {comp['nom']}  {'- ' + comp['niveau'] if comp['niveau'] else ''}\n"
                    for comp in comps
                    ]
    
                cv += "".join(competence)

        # Ajouter expériences récentes
        if experience_recente:
                cv += "### Expériences récentes\n\n"
                for exp in experience_recente:
                    cv += f"**{exp.poste}** chez {exp.entreprise} ({exp.debut} - {exp.fin})\n"
                    if exp.description:
                        cv += f"{exp.description.strip()}\n\n"

        # Ajouter passions
        if self.pro.passions:
            cv += f"### Passions\n"
            for passion in self.pro.passions:
                cv += f"{passion['nom']} {'- ' + passion['description'] if passion['description'] else ''}"

        return cv
    

    def afficher(self, mode: str = 'auto') -> None:
        """
        Afficher le CV :
        - auto : affiche via IPython si dispo, sinon print
        - texte : print brut
        - jupyter : force IPython Markdown"""

        md = self.generer_markdown()

        if mode == 'texte':
            print(md)
        elif mode == 'jupyter':
            from IPython.display import display, Markdown
            display(Markdown(md))
        else:
            try:
                from IPython.display import display, Markdown
                display(Markdown(md))

            except ImportError:
                print(md)