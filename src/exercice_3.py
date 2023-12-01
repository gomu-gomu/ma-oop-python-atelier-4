class Véhicle:
  def __init__(self, nbr_kilomètre) -> None:
    self.nbr_kilomètre = nbr_kilomètre
  
  def rouler_kilomètre(self, kilometre_parcourus):
    return self.nbr_kilomètre + kilometre_parcourus

  def calculer_roue(self):
    return 'le nombre des roues est indéfini'

class Camion(Véhicle):
  def calculer_roue(self):
    return 6


def main():
  print('Exercice 3:')

  # 7 - Ajouter un objet petit_véhicule qui instancie la classe Véhicule avec le nbr_kilomètre 30000.
  petit_véhicule = Véhicle(30000)

  # 8 - Afficher le résultat de la méthode rouler_kilomètre de l’objet petit_véhicule avec le paramètre 1000.
  print(f'8 - Nombre des kilomètres de petit_véhicule est : {petit_véhicule.rouler_kilomètre(1000)}')

  # 9 - Afficher le résultat de la méthode calculer_roue de l’objet petit_véhicule.
  print(f'9 - Nombre des roues de petit_véhicule est : {petit_véhicule.calculer_roue()}')

  # 10 - Ajouter un objet petit_camion qui instancie la classe Camion avec le nbr_kilomètre 900000.
  petit_camion = Camion(900000)

  # 11 - Afficher le résultat de la méthode kilometre_parcourus de l’objet petit_camion avec le paramètre 20000.
  print(f'11 - Nombre des kilomètres de petit_camion est : {petit_camion.rouler_kilomètre(20000)}')
  
  # 12 - Afficher le résultat de la méthode calculer_roue de l’objet petit_camion.
  print(f'12 - Nombre des roues de petit_camion est : {petit_camion.calculer_roue()}')

if __name__ == '__main__':
  main()
