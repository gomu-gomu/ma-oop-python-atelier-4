class Calculatrice:
  def __init__(self, a, b) -> None:
    self.a = a
    self.b = b
  
  def verifier_numerique(self):
    return isinstance(self.a, float) and isinstance(self.b, float)
  
  def calculer_somme(self):
    if self.verifier_numerique():
      return self.a + self.b
    else:
      return 'Erreur : Les valeurs doivent être numériques'
  
  def calculer_soustraction(self):
    if self.verifier_numerique():
      return self.a - self.b
    else:
      return 'Erreur : Les valeurs doivent être numériques'
  
  def calculer_multiplication(self):
    if self.verifier_numerique():
      return self.a * self.b
    else:
      return 'Erreur : Les valeurs doivent être numériques'
  
  def calculer_division(self):
    if self.verifier_numerique():
      try:
        return self.a / self.b
      except ZeroDivisionError:
        return 'Erreur : Division par zéro'
    else:
      return 'Erreur : Les valeurs doivent être numériques'

def main():
  print('Exercice 2:')

  # 8 - Après la définition de la classe Calculatrice, demander à l’utilisateur de saisir deux nombres depuis son clavier.
  a = float(input('> Entrer la valeur a : '))
  b = float(input('> Entrer la valeur b : '))

  # 9 - Créer un nouvel objet joli_calculatrice à partir de la classe Calculatrice, qui prend en paramètre les deux valeurs saisis dans la question 8.
  joli_calculatrice = Calculatrice(a, b)

  # 10 - Afficher le résultat de la somme, soustraction, multiplication, division des deux de l’objet créer via objet joli_calculatrice de la question 9, en se basant successivement des méthodes calculer_somme, calculer_soustraction, calculer_multiplication, calculer_division.
  print(f'10 - {a} + {b} = {joli_calculatrice.calculer_somme()}.')
  print(f'10 - {a} - {b} = {joli_calculatrice.calculer_soustraction()}.')
  print(f'10 - {a} * {b} = {joli_calculatrice.calculer_multiplication()}.')
  print(f'10 - {a} / {b} = {joli_calculatrice.calculer_division()}.')

if __name__ == '__main__':
  main()
