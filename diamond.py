"""Kata du diamant: afficher un diamant en ASCII."""


class Diamant:
    def __init__(self, carat):
        self.carat = carat
        self.carat_maximum = ord('A')

    def tailler(self):
        taille = ord(self.carat) - self.carat_maximum
        diamant = ''
        diamant += self.tailler_couronne(taille)
        diamant += self.tailler_rondiste(taille)
        diamant += self.tailler_cullasse(taille)
        return diamant

    def _tailler_une_tranche(self, hauteur, largeur=0):
        arête = chr(self.carat_maximum + hauteur)
        tranche = ''.ljust(largeur)
        tranche += arête
        tranche += ''.ljust(hauteur * 2 - 1)
        if hauteur > 0:
            tranche += arête
        tranche += ''.ljust(largeur)
        tranche += '\n'
        return tranche

    def _façonner_diamant(self, hauteur, retourné=False):
        tranches = list(range(hauteur)) if retourné else list(reversed(range(hauteur)))
        diamant = ''
        for i in tranches:
            diamant += self._tailler_une_tranche(hauteur=hauteur - i - 1, largeur=i + 1)
        return diamant

    def tailler_couronne(self, taille):
        return self._façonner_diamant(taille)

    def tailler_rondiste(self, taille):
        return self._tailler_une_tranche(taille)

    def tailler_cullasse(self, taille):
        return self._façonner_diamant(taille, retourné=True)


assert Diamant('A').tailler() == 'A\n'
assert Diamant('B').tailler() == ' A \nB B\n A \n'
assert Diamant('C').tailler() == '  A  \n B B \nC   C\n B B \n  A  \n'
assert Diamant('D').tailler() == '   A   \n  B B  \n C   C \nD     D\n C   C \n  B B  \n   A   \n'
