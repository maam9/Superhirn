from typing import List, Tuple

from auswertungs_element import AuswertungsElement
from code_element import CodeElement


class Code:
    def __init__(self, code: List[CodeElement]):
        self.code = code

    def get_code(self) -> List[CodeElement]:
        return self.code

    def get_code_to_string(self) -> str:
        result = ""
        for e in self.code:
            result = result + str(e.value)

        return result


class Auswertung:
    def __init__(self, auswertung: List[AuswertungsElement]):
        self.auswertung = auswertung

    def get_auswertung(self) -> List[AuswertungsElement]:
        return self.auswertung


class Spielbrett:
    def __init__(self, spielbrett: List[Tuple[Code, Auswertung]], zielcode: Code):
        self.spielbrett = spielbrett
        self.zielcode = zielcode

    def spielbrett_ausgeben(self) -> str:
        """Gibt das Spielbrett aus, die Rundenanzahl und die Auswertungselemente """

        output = ""
        print("╔════════════════════════════╗")
        print("║         Spielbrett         ║")
        print("╠════════════════════════════╣")
        for i, (spielzug, auswertung) in enumerate(self.spielbrett, start=1):
            spielzug_values = [element.value for element in spielzug.get_code()]
            auswertung_values = [element.value for element in auswertung.get_auswertung()]

            colored_spielzug = [self.colorize_code(value) for value in spielzug_values]
            colored_auswertung = [self.colorize_auswertung(value) for value in auswertung_values]

            print(f"\t{i}. RUNDE:{''.join(map(str, colored_spielzug))} || {''.join(map(str, colored_auswertung))}\t")
        print("╚════════════════════════════╝\n")
        return output

    def spielzug_hinzufuegen(self, spielzug: Tuple[Code, Auswertung]):
        """
        Fügt dem Spielbrett einen Spielzug hinzu.
        """
        self.spielbrett.append(spielzug)



    def zielcode_hinzufuegen(self, code: Code):
        """
        Fügt dem Spielbrett einen Zielcode hinzu.
        """
        self.zielcode = code


    def zielcode_ausgeben(self):
        """
        druckt zielcode auf der Konsole aus
        """

        ergebnis = "Der Zielcode lautete: "
        colored_zielcode = [self.colorize_code(element.value) for element in self.zielcode.code]
        print(ergebnis + ''.join(map(str, colored_zielcode)))

    def colorize_code(self, value: int) -> str:
        """Returns the ANSI escape code for colorizing the code."""
        color_mapping = {
            1: '\033[91m',  # Red
            2: '\033[92m',  # Green
            3: '\033[93m',  # Yellow
            4: '\033[94m',  # Blue
            5: '\033[95m',  # Magenta (there is no orange ANSI code)
            6: '\033[33m',  # Brown (Yellow in ANSI)
            7: '\033[97m',  # White
            8: '\033[37m'  # Black
        }
        return f"{color_mapping.get(value, '')}{value}\033[0m"

    def colorize_auswertung(self, value: int) -> str:
        """Returns the ANSI escape code for colorizing the AuswertungsElement."""
        color_mapping = {
            7: '\033[97m',  # White
            8: '\033[37m'  # Black
        }
        return f"{color_mapping.get(value, '')}{value}\033[0m"

