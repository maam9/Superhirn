from auswertungs_element import AuswertungsElement
from code_element import CodeElement
from coder.coder import Coder
from spielbrett.spielbrett import Code, Auswertung


class MenschCoder(Coder):

    def code_erstellen(self, code_laenge: int, code_auswahl: int) -> Code:
        # nimmt eine String input zwischen (1-8)
        user_input_string = input(f"Bitte gib den Zielcode mit der Länge {code_laenge} und den Farben (1-{code_auswahl}) ein\n")

        while len(user_input_string) != code_laenge or not all(
                1 <= int(char) <= code_auswahl for char in user_input_string):
            print(f"Die länge darf nicht mehr als {code_laenge} sein."f" Die "
                  f"Zeichen müssen zwischen 1 und {code_auswahl} sein. Versuche es nochmal.")
            user_input_string = input(f"Bitte gib den Zielcode mit der Länge {code_laenge} und den Farben (1-{code_auswahl}) ein\n")

            # Convertiere alle char zu einem integer und eine Liste erstellen.
        nutzer_mastermind_list = [int(char) for char in user_input_string]
        result = []

        for e in nutzer_mastermind_list:
            result.append(CodeElement(e))

        return Code(result)

    def code_auswerten(self, code: Code, ziel_code: Code) -> Auswertung:

        while True:
            # print("Zielcode:", ziel_code.get_code_to_string())
            print("Geratener Code:", code.get_code_to_string())

            feedback_input = input(
                "\nWerte den geratenen Code aus:\n '7' - richtige Farbe\n '8' - richtige Farbe und Position\n"
                "oder drücke Enter um die Auswertung leer zu lassen")
            if not feedback_input:
                return Auswertung([])
            else:
                print(feedback_input)
                if self.pruefer(feedback_input, len(ziel_code.code)):
                    break

        feedback_input_als_int = [int(char) for char in feedback_input]
        feedback_auswertungs_als_code_element = []
        for elm in feedback_input_als_int:
            feedback_auswertungs_als_code_element.append(AuswertungsElement(elm))

        return Auswertung(feedback_auswertungs_als_code_element)

    @staticmethod
    def pruefer(user_inpu: str, zielcode_leange: int) -> bool:
        valid_feedback_characters = {'7', '8'}
        for char in user_inpu:
            if char not in valid_feedback_characters:
                print("\nNur eine Zahl aus 7 und 8 ist erlaubt")
                return False
            elif len(user_inpu) > zielcode_leange:
                print("\nDer Code darf nur %s lang sein" % zielcode_leange)
                return False
            else:
                return True


def __init__():
    super().__init__()
