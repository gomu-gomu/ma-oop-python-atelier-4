class ADN:
  def __init__(self, chaine) -> None:
    self.chaine = chaine

  def calculer_chaine_ADN(self):
    return len(self.chaine)
  
  def ADN__2__ARN(self):
    arn = ''

    for base in self.chaine:
        if base == 'A':
            arn += 'U'
        elif base == 'T':
            arn += 'A'
        elif base == 'C':
            arn += 'G'
        elif base == 'G':
            arn += 'C'

    return arn

def load_fichier():
  contenu = ''

  with open('s_protein_sars-covid2_ref.txt', 'r') as file:
    contenu = file.read()

  return contenu

def enregistrer_arn(arn):
  with open('arn_s_protein_sars-covid2_ref.txt', 'w') as file:
    file.write(arn)

def main():
  print('Exercice 1:')

  # 5 - Ajouter un objet adn_partie qui instancie la classe ADN et ayant la chaine suivante "ATCGATCGTTGGC".
  adn_partie = ADN('ATCGATCGTTGGC')

  # 6 - Afficher le résultat de la méthode calculer_chaine_ADN de l’objet créer adn_partie.
  print(f'6 - La longeur de l\'ADN est {adn_partie.calculer_chaine_ADN()}.')
  
  # 7 - Afficher le résultat de la méthode ADN_2_ARN de l’objet créer adn_partie.
  print(f'7 - L\'ARN de "{adn_partie.chaine}" est "{adn_partie.ADN__2__ARN()}".')

  # 9 - Ajouter un objet adn_file qui instancie la classe ADN et qui récupère la valeur de la chaine depuis un fichier texte s_protein_sars-covid2_ref.txt.
  contenu_de_fichier = load_fichier()
  adn_file = ADN(contenu_de_fichier)
  print('9 - ADN récupèré du fichier "s_protein_sars-covid2_ref.txt".')
  
  # 10 - Enregistrer le résultat de la méthode ADN_2_ARN de l’objet créer adn_file, dans un nouveau fichier avec le nom arn_s_protein_sars-covid2_ref.txt.
  arn_a_enregistrer = adn_file.ADN__2__ARN()
  enregistrer_arn(arn_a_enregistrer)
  print('10 - ARN enregistré dans le fichier "arn_s_protein_sars-covid2_ref.txt".')

if __name__ == '__main__':
  main()
