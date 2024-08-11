import random

from auswertungs_element import AuswertungsElement
from code_element import CodeElement
from coder.coder import Coder
from spielbrett.spielbrett import Code, Auswertung


class ComputerCoder(Coder):

    def code_erstellen(self, code_laenge: int, code_auswahl: int) -> Code:
        # insgesamt Farbe
        max_range = code_auswahl
        print("Der Zielcode wurde vom Codierer erstellt!")
        mastermind_list = []  # erstellt eine liste für code

        for i in range(code_laenge):
            mastermind_list.append(random.randint(1, max_range))  # addiert random nummer in der liste

        result = []
        for e in mastermind_list:
            result.append(CodeElement(e))

        return Code(result)

    def code_auswerten(self, code: Code, ziel_code: Code) -> Auswertung:
        auswertung_list = code.code
        ziel_code_liste_kopie = ziel_code.code.copy()
        ergebniss_liste = []

        for i in auswertung_list:
            if i in ziel_code.code:

                if i.value == ziel_code_liste_kopie[0].value:

                    ergebniss_liste.append(AuswertungsElement(8))
                else:
                    ergebniss_liste.append(AuswertungsElement(7))

            ziel_code_liste_kopie.pop(0)
        result = Auswertung(ergebniss_liste)

        return result

    def __init__(self):
        super().__init__()
