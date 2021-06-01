class Compte:
    instance_list = []
    
    def __init__(self):
        Compte.instance_list.append(self)
        
    def compte():
        return len(instance_list)
        
class Carre(Compte):
    instance_list = []
    
    def __init__(self, largeur):
        self.largeur = largeur
        Carre.instance_list

    def aire(self):
        return largeur*largeur
    
    def perimetre(self):
        return largeur * 4
        
class Rectangle(Compte):
    def __init__(self, largeur, longeur):
        self.largeur = largeur
        self.longeur = longeur

    def aire(self):
        return largeur*longeur
    
    def perimetre(self):
        return largeur*2 + longeur*2