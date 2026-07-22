class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier

    def afficher(self):
        super().afficher()
        print("Casier :", self.casier)


class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach_personnel):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach_personnel = coach_personnel

    def afficher(self):
        super().afficher()
        print("Coach personnel :", self.coach_personnel)

membre1 = MembreStandard(
    101, "Ali", "Montreal", 12, 50, "Oui", "Oui"
)

membre2 = MembrePremium(102, "Sara", "Laval", 24, 100, "Oui", "Non"
)

membre1.afficher()
print("----------------")
membre2.afficher()
