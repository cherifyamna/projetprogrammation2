class membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.numero = numero
        self.nom = nom
        self.succursale = succursale
        self.duree = duree
        self.prix = prix
        self.actif = actif

    def afficher (self):
        print(f"numero : {self.numero}") 
        print(f"nom : {self.nom}")  
        print(f"succursale : {self.succursale}")
        print(f"duree : {self.duree} mois")
        print(f"prix : {self.prix} $") 
        print(f"actif : {self.actif}")
        print("-" * 30)


membre1 = membre(1, "ali", "toronto", 12, 45, "oui")
membre2 = membre(2, "Sara", "Ottawa", 6, 35, "Non")

membre1.afficher()
membre2.afficher()
