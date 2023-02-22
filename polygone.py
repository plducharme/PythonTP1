import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from abc import ABC, abstractmethod


class Polygone(ABC):

    def __init__(self):
        self._liste_vecteurs = []

    @property
    def liste_vecteurs(self):
        return self._liste_vecteurs

    @liste_vecteurs.setter
    def liste_vecteurs(self, nouvelle_liste):
        self._liste_vecteurs = nouvelle_liste

    # doit retourner l'aire du polygone
    @abstractmethod
    def aire(self):
        pass

    # doit retourner le périmètre du polygone
    def perimetre(self):
        # Ajouter l'implémentation de la méthode perimetre(self)
        pass

    def nb_cotes(self):
        # Ajouter l'implémentation de la méthode nb_cotes(self)
        pass

    def afficher_forme(self):
        points = []
        for vecteur in self._liste_vecteurs:
            points.append((vecteur.point_depart.x, vecteur.point_depart.y))
        print("Affichage de " + str(points))
        polygon = Polygon(points)
        fig = plt.figure()
        ax = fig.gca()
        ax.add_patch(polygon)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.show()


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valeur):
        self._x = valeur

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valeur):
        self._y = valeur


class Vecteur:

    def __init__(self, point_depart, point_arrivee):
        self._point_depart = point_depart
        self._point_arrivee = point_arrivee

    @property
    def point_depart(self):
        return self._point_depart

    @point_depart.setter
    def point_depart(self, valeur):
        self._point_depart = valeur

    @property
    def point_arrivee(self):
        return self._point_arrivee

    @point_arrivee.setter
    def point_arrivee(self, valeur):
        self._point_arrivee = valeur

    def longueur(self):
        # Ajouter l'implémentation de la méthode
        pass

