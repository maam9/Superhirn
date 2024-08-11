from random import choice

from code_element import CodeElement
from rater.rater import Rater
from spielbrett.spielbrett import Code, Spielbrett


class ComputerRater(Rater):
    def code_raten(self, spielbrett: Spielbrett, codelaenge: int, code_auswahl: int) -> Code:

        if code_auswahl not in range(2, 9) or codelaenge not in range(4, 6):
            # Die Range ist 2,9, weil bei 2,8, die 8 nicht eingeschlossen ist
            # Range = (start,stop-1)
            raise ValueError("Falsche Code-Auswahl. Nur 2-8 Farben benutzen")
        else:
            # püft ob die eingabe und in der Enum enthalten ist und wählt diese Farben aus
            valid_colors = list(CodeElement)[:code_auswahl]
            code_elements = [choice(list(valid_colors)) for _ in range(codelaenge)]
            # code_elements = [choice(list(CodeElement)) for _ in range(len(spielbrett.zielcode.get_code()))]
            random_code = Code(code_elements)
            return random_code

    def __init__(self):
        super().__init__()
