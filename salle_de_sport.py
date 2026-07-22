
class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.__duree = None
        self.__prix = None
        self.__actif = None
        self.duree = duree
        self.prix = prix
        self.actif = actif
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, valeur):
        self.__numero = valeur
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur
    @property
    def succursale(self):
        return self.__succursale
    @succursale.setter
    def succursale(self, valeur):
        self.__succursale = valeur  
    @property
    def duree(self):
        return self.__duree 
    @duree.setter
    def duree(self, valeur):
        if valeur > 0:
            self.__duree = valeur
        else:
            print("Durée invalide.")
    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, valeur):
        if valeur > 0:
            self.__prix = valeur
        else:
            print("Prix invalide.")
    @property
    def actif(self):
        return self.__actif

    @actif.setter
    def actif(self, valeur):
        if valeur.lower() == "oui":
            self.__actif = "Oui"
        elif valeur.lower() == "non":
            self.__actif = "Non"
        else:
            print("État actif invalide.")
    def afficher(self):
            print("Numéro :", self.numero)
            print("Nom :", self.nom)
            print("Succursale :", self.succursale)
            print("Durée :", self.duree, "mois")
            print("Prix mensuel :", self.prix, "$")
            print("Actif :", self.actif)
            print("--------------------------")
membre1 = Membre(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui")
membre2 = Membre(2, "Marc Bouchard", "Est", 6, 40, "Non")

membre1.afficher()
membre2.afficher()
