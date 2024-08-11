from code_element import CodeElement
from rater.rater import Rater
from spielbrett.spielbrett import Code, Spielbrett


class MenschRater(Rater):

    def code_raten(self, spielbrett: Spielbrett, codelaenge: int, code_auswahl: int) -> Code:
        print(
            f"\nGebe ein Farbencode der Länge {codelaenge} ein, die Codeauswahl ist auf Farbe 1 bis {code_auswahl} "
            f"eingestellt. Rate den "
            f"Zielcode!")
        eingabe = input()

        if self.eingabe_korrekt(codelaenge, code_auswahl, eingabe):
            rater_code = int(eingabe)
            zahlen_liste = [int(ziffer) for ziffer in str(rater_code)]
            code_farben = []

            for element in zahlen_liste:
                code_farben.append(CodeElement(element))

            code_farben = [CodeElement(zahl) for zahl in zahlen_liste]

            # print(f"Deine Eingabe entspricht: {[farbe.name for farbe in code_farben]}")
            rater_code = Code(code_farben)
            return rater_code
        else:
            return self.code_raten(spielbrett, codelaenge, code_auswahl)

    @staticmethod
    def eingabe_korrekt(codelaenge: int, code_auswahl: int, eingabe: str) -> bool:

        # Parameter Error
        if codelaenge not in range(4, 6) or code_auswahl not in range(2, 9):
            raise ValueError("Codelänge oder Code Auswahl nicht gültig.")

        # Eingabe hat falsche Länge
        if len(eingabe) != codelaenge:
            print("Falsche Codelänge. Bitte erneut eingeben.")
            return False

        # Buchstaben sollen angedeutet werden
        if not eingabe.isdigit():
            print("Keine Buchstaben verwenden.")
            return False

        rater_code = int(eingabe)
        # Eingabe als Liste von Zahlen gespeichert
        zahlen_liste = [int(ziffer) for ziffer in str(rater_code)]


        for element in zahlen_liste:
            if element not in range(1, code_auswahl + 1):
                print(f"Eine der Zahlen liegt nicht im gültigen Bereich von 1 bis {code_auswahl}.")
                return False

        # Wenn If Statements nicht erfüllt, kommt True
        return True

    def __init__(self):
        super().__init__()
