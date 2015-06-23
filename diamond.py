"""Kata du diamant: afficher un diamant en ASCII."""


class Diamant:
    def __init__(self, carat):
        self.carat = carat
        self.carat_maximal = ord('A')

    def tailler(self):
        taille = ord(self.carat) - self.carat_maximal
        diamant = self._façonner_diamant(taille, taille)
        return diamant

    def _tailler_une_tranche(self, hauteur, largeur=0):
        tranche = ''.ljust(largeur)
        arête = chr(self.carat_maximal + hauteur)
        tranche += arête
        tranche += ''.ljust(hauteur * 2 - 1)
        if hauteur > 0:
            tranche += arête
        tranche += ''.ljust(largeur)
        tranche += '\n'
        return tranche

    def _façonner_diamant(self, hauteur, hauteur_origine):
        diamant = ''
        nouvelle_hauteur = hauteur_origine - hauteur
        if hauteur > 0:
            diamant += self._tailler_une_tranche(nouvelle_hauteur, hauteur)
            diamant += self._façonner_diamant(hauteur - 1, hauteur_origine)
        diamant += self._tailler_une_tranche(nouvelle_hauteur, hauteur)
        return diamant


assert Diamant('A').tailler() == 'A\n'
assert Diamant('B').tailler() == ' A \nB B\n A \n'
assert Diamant('C').tailler() == '  A  \n B B \nC   C\n B B \n  A  \n'
assert Diamant('D').tailler() == '   A   \n  B B  \n C   C \nD     D\n C   C \n  B B  \n   A   \n'

print(Diamant('D').tailler())
