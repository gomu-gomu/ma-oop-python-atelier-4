from exercice_1 import ADN

class ARN(ADN):

  @property
  def arn_chaine(self):
    return super().chaine

  @arn_chaine.setter
  def arn_chaine(self, valeur):
    super().chaine = valeur

  def __init__(self, chaine):
    super().__init__(chaine)
  
  def ARN__2__ADN(self):
    adn = ''

    for base in self.chaine:
        if base == 'U':
            adn += 'A'
        elif base == 'A':
            adn += 'T'
        elif base == 'G':
            adn += 'C'
        elif base == 'C':
            adn += 'G'

    return adn

def main():
  print('Exercice 5:')

  arn_partie = ARN('UAGCCGAAUCUGCUACUUCGGCAGGGCCUUU')

  print(f'La longeur de l\'ARN est {arn_partie.calculer_chaine_ADN()}.')
  print(f'L\'ADN de "{arn_partie.chaine}" est "{arn_partie.ARN__2__ADN()}".')

if __name__ == '__main__':
  main()
