class Rectangle:
  def __init__(self, longeur, largeur) -> None:
    self.longeur = longeur
    self.largeur = largeur
  
  def Perimetre(self):
    return (self.longeur + self.largeur) * 2
  
  def Surface(self):
    return self.longeur * self.largeur

class Parallelepipede(Rectangle):
  def __init__(self, longeur, largeur, hauteur) -> None:
    super().__init__(longeur, largeur)
    self.hauteur = hauteur
  
  def Volume(self):
    return self.Surface() * self.hauteur

def main():
  print('Exercice Classe Rectangle:')
  
  monRectangle = Rectangle(7, 5)
  monParallelepipede = Parallelepipede(7, 5, 2)

  print(f'La surface de mon rectangle est : {monRectangle.Surface()}')
  print(f'La primètre de mon rectangle est : {monRectangle.Perimetre()}')
  print(f'Le volume de mon Parallelepipide est : {monParallelepipede.Volume()}')

if __name__ == '__main__':
  main()
