from typing import Tuple

from auswertungs_element import AuswertungsElement
from coder.coder import Coder
from coder.mensch_coder import MenschCoder
from rater.mensch_rater import MenschRater
from rater.rater import Rater
from spielbrett.spielbrett import Spielbrett, Code, Auswertung


# test
class Superhirn:
    def __init__(self,
                 spieler: Tuple[Coder, Rater],
                 max_runden: int,
                 codelaenge: int, code_auswahl: int):
        self.spielbrett = None
        self.spieler = spieler
        self.max_runden = max_runden
        self.code_laenge = codelaenge
        self.code_auswahl = code_auswahl

    def spielzug(self):
        code = self._rater_zug()
        auswertung = self._coder_zug(code)
        self.spielbrett.spielzug_hinzufuegen((code, auswertung))

    def spiel_status_ueberpruefen(self) -> bool:
        """
        checked beide Spielenden möglichkeiten
        :return: true
        """
        if self.helper_rater_sieg():
            self.spielbrett.spielbrett_ausgeben()
            self.spielbrett.zielcode_ausgeben()
            print("Zielcode richtig erraten! Der Rater ist der Sieger.")
            print("Herzlichen Glückwunsch!")
            print("")
            return True

        if self.helper_coder_sieg():
            self.spielbrett.spielbrett_ausgeben()
            self.spielbrett.zielcode_ausgeben()
            print("Rundenlimit erreicht! Der Coder ist der Sieger.")
            print("Herzlichen Glückwunsch!")
            print("")
            return True

        else:
            return False

    def helper_coder_sieg(self) -> bool:
        if len(self.spielbrett.spielbrett) < self.max_runden:
            return False
        else:
            return True

    def helper_rater_sieg(self) -> bool:
        """

        :return: true wenn ein tuple in codelaenge mit nur schwarze pins (Wert8)
        """
        erstes_spielzug_tupel = self.spielbrett.spielbrett[len(self.spielbrett.spielbrett) - 1]
        auswertungs_element = erstes_spielzug_tupel[1]
        schwarzer_pin_counter = 0

        for element in auswertungs_element.auswertung:
            if element == AuswertungsElement.schwarzer_pin:
                schwarzer_pin_counter = schwarzer_pin_counter + 1

        # print(schwarzer_pin_counter)

        if schwarzer_pin_counter == self.code_laenge:
            return True
        else:
            return False

    def zielcode_erstellen(self) -> Code:

        zielcode = self.spieler[0].code_erstellen(self.code_laenge, self.code_auswahl)
        return zielcode

    # Zug des Codierers
    def _coder_zug(self, aktueller_code: Code) -> Auswertung:
        if isinstance(self.spieler[0], MenschCoder):
            self.spielbrett.spielbrett_ausgeben()
            self.spielbrett.zielcode_ausgeben()
        # habe hier die zielcode_ausgeben methode weggemeacht_Waindja
        # self.spielbrett.zielcode_ausgeben()
        return self.spieler[0].code_auswerten(aktueller_code, self.spielbrett.zielcode)

    # Zug des Raters
    def _rater_zug(self) -> Code:
        if isinstance(self.spieler[1], MenschRater):
            self.spielbrett.spielbrett_ausgeben()

        # Rater rät Code und gibt sein Code zurück
        return self.spieler[1].code_raten(self.spielbrett, self.code_laenge, self.code_auswahl)

    @staticmethod
    def spielbrett_erstellen(leere_spielbrett_liste, zielcode: Code, ) -> Spielbrett:
        spielbrett = Spielbrett(leere_spielbrett_liste, zielcode)
        return spielbrett
