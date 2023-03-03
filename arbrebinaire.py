import csv
# Arbre binaire de recherche
class Noeud:

    def __init__(self, equipe):
        self._equipe = equipe
        self._gauche = None
        self._droite = None

    @property
    def gauche(self):
        return self._gauche

    @gauche.setter
    def gauche(self, valeur):
        self._gauche = valeur

    @property
    def droite(self):
        return self._droite

    @droite.setter
    def droite(self, valeur):
        self._droite = valeur


    def insertion(self, equipe):
        # Ajouter l'implémentation d'insertion(self, equipe)
        pass


    # Afficher l'arbre
    def afficher_arbre(self):
        if self._gauche:
            self._gauche.afficher_arbre()
        self._equipe.afficher(),
        if self._droite:
            self._droite.afficher_arbre()


class EquipeLNH:

    def __init__(self, nom, data):
        self.__nom = nom
        self.__data = data

    @property
    def equipe(self):
        return self._equipe

    @equipe.setter
    def equipe(self, valeur):
        self._equipe = valeur

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valeur):
        self.__data = valeur

    def total_points(self):
        # Ajouter l'implémentation, doit retourner le nombre total de points
        pass

    def moyenne_but_par_match(self):
        # Ajouter l'ìmplémentation
        pass

    def afficher(self):
        print(self.nom + '\t\t\tPts: ' + str(self.total_points()) + '\tBP/MJ: ' + str(self.moyenne_but_par_match()))


class DataUtils:

    @staticmethod
    def load_data(filename):
        liste_equipes = []
        with open(filename, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            lignes = 0
            for ligne in reader:
                if lignes == 0:
                    print("Ignorer l'entete")
                    lignes += 1
                else:
                    equipe = EquipeLNH(ligne[0], {'MJ': ligne[2], 'V': ligne[3], 'DP': ligne[6], 'BP': ligne[12]})
                    liste_equipes.append(equipe)
                    lignes += 1
            return liste_equipes

    @staticmethod
    def moyenne_haut_bas(liste_equipes):
        # Implémenter la méthode
        bas = ()
        haut = ()
        return bas, haut

# Code pour tester
racine = None
liste_equipes = DataUtils.load_data('./data/nhl.csv')
for equipe in liste_equipes:
    if racine is None:
        racine = Noeud(equipe)
    else:
        racine.insertion(equipe)

racine.afficher_arbre()

bas, haut = DataUtils.moyenne_haut_bas(liste_equipes)

print('En dessous de la moyenne BP/MJ')
for equipe in bas:
    equipe.afficher()
print('Au dessus de la moyenne BP/MJ')
for equipe in haut:
    equipe.afficher()

