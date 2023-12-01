class ListeUtilitaire:

  @property
  def liste(self) -> list:
    return self.__liste

  @liste.setter
  def liste(self, valeur):
    self.__liste = valeur

  def __init__(self, liste) -> None:
    self.liste = liste
  
  def calculer_longeur(self):
    return len(self.liste)
  
  def afficher(self):
    for i, element in enumerate(self.liste):
      print(f'* Element {i} => {element}.')
    
  def trier(self):
    self.liste.sort()
    
  def vider(self):
    self.liste = []

def main():
  print('Exercice 4:')

  # 9 - Ajouter l’objet ma_liste qui initialise la liste ayant les éléments : ‘ADN’, ‘ARN’, ‘Covid’, ‘Protéine E’, ‘Anzime’.
  ma_liste = ListeUtilitaire(['ADN', 'ARN', 'Covid', 'Protéine E', 'Anzime'])

  # 10 - Appeler l’ensemble des méthodes créés.
  print(f'10 - Longeur de la liste : {ma_liste.calculer_longeur()}.')
  print(f'10 - Affichage de la liste :')
  ma_liste.afficher()
  print(f'10 - Le tri de la liste :')
  ma_liste.trier()
  ma_liste.afficher()
  print(f'10 - La remise à zéro de la liste :')
  ma_liste.vider()
  ma_liste.afficher()

if __name__ == '__main__':
  main()
