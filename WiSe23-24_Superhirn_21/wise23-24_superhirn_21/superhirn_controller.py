from typing import Tuple

from coder.computer_coder import ComputerCoder
from coder.mensch_coder import MenschCoder
from coder.netzwerk_coder import NetzwerkCoder
from rater.computer_rater import ComputerRater
from rater.mensch_rater import MenschRater
from superhirn.superhirn import Superhirn
from coder.coder import Coder
from rater.rater import Rater


class SuperhirnController:
    """
    erstellt Superhirn kontrolliert Spielfluss
    """

    STANDART_GAME_LAENGE = 42
    CODE_AUSWAHL_INTERVALL = (2, 8)
    MINIMAL_CODELAENGE = 4
    MAXIMALE_CODELEANGE = 5
    NICHTZULAESSIGER_INPUT = -1
    MENSCHCODER_COMPUTERRATER = 0
    MAXIMIMALE_RUNDNEANZAHL = 10
    COMPUTERCODER_MENSCHRATER = 1
    COMPUTERCODERNETZWERK_MENSCHRATER = 2
    PORTLAENGE = 5

    __superhirn: Superhirn = None

    def __init__(self, ):
        pass

    def superhirn_spielen(self):
        self.print_regeln()
        self.__superhirn = self.superhirn_erstellen()

        self.__superhirn.spielbrett = self.__superhirn.spielbrett_erstellen([], self.__superhirn.zielcode_erstellen())

        while True:
            self.__superhirn.spielzug()

            if self.__superhirn.spiel_status_ueberpruefen():
                break

            print("Die Nächste Runde beginnt: gib 0 ein "
                  "um das Spiel abzubrechen oder mache eine beliebige Eingabe um Fortzufahren")
            user_input = input()
            if user_input == "0":
                break

        self.spiel_neustarten()

    # clean up method ersetzt durch helper_getplayer_roll
    # def spieler_erstellen(self, coder: Coder, rater: Rater):
    #   raise NotImplementedError("Method not implemented yet")

    def superhirn_erstellen(self) -> Superhirn:
        player = self.helper_getplayer_roll()
        code_elemente_auswahl = self.get_code_auswahl()
        code_laenge = self.get_codeleange()
        return Superhirn(player, self.MAXIMIMALE_RUNDNEANZAHL, code_laenge, code_elemente_auswahl)

    def helper_getplayer_roll(self) -> Tuple[Coder, Rater]:

        print(
            f"Spielmodi wählen: \n Tippe '{self.MENSCHCODER_COMPUTERRATER}' um als Coder gegen den Computer zu spielen"
            f" \n Tippe '{self.COMPUTERCODER_MENSCHRATER}' um als Rater gegen den Computer zu spielen"
            f" \n Tippe '{self.COMPUTERCODERNETZWERK_MENSCHRATER}' um als Rater gegen einen Coder im Netz zu spielen")

        user_input = input()

        if not user_input.isdigit():
            print("Bitte gib eine zulässige Zahl ein")
            return self.helper_getplayer_roll()

        user_input = int(user_input)

        if user_input == self.MENSCHCODER_COMPUTERRATER:
            x = MenschCoder()
            y = ComputerRater()
            print("\nDu bist Codierer \n")
            return x, y
        elif user_input == self.COMPUTERCODER_MENSCHRATER:
            x = MenschRater()
            y = ComputerCoder()
            print("\nDu bist Rater \n")
            return y, x
        elif user_input == self.COMPUTERCODERNETZWERK_MENSCHRATER:
            x = MenschRater()
            y = self.helper_create_netzwerkcoder()
            print("\nDu bist Rater \n")
            return y, x
        else:
            return self.helper_getplayer_roll()

    def helper_get_code_auswahl(self) -> int:
        """

        :return:
        """
        print("Bitte wähle eine Zahl zwischen %s - %s aus, um anzugeben, "
              "wie viele Farben du verwenden möchtest. \n" % (
                  int(self.CODE_AUSWAHL_INTERVALL[0]), int(self.CODE_AUSWAHL_INTERVALL[1])))

        user_input = input()

        if not user_input.isdigit():
            print("\nBitte gib eine Zahl ein, keine anderen Symbole! ")
            return self.NICHTZULAESSIGER_INPUT

        user_input = int(user_input)

        if int(self.CODE_AUSWAHL_INTERVALL[1]) >= user_input >= int(self.CODE_AUSWAHL_INTERVALL[0]):
            return user_input
        else:
            return self.NICHTZULAESSIGER_INPUT

    def get_code_auswahl(self) -> int:
        result = self.helper_get_code_auswahl()
        if result == -1:
            return self.get_code_auswahl()
        else:
            return result

    def helper_create_netzwerkcoder(self) -> NetzwerkCoder:
        print("bitte gib die ip Adresse ein")
        ip = input()
        print("bitte gib den port ein")
        port = input()

        if all((char.isdigit() or (char == '.') for char in ip)) and port.isdigit():
            return NetzwerkCoder(ip, port)
        else:
            print("nur zahlen erlaubt")
            return self.helper_create_netzwerkcoder()

    def helper_get_codeleange(self) -> int:
        """
        fordert input auf informiert über erfolg und misserfolg
        :return: Maximum<= Zahl =<Minimum misserfolg = -1
        """

        print("Bitte gib %s oder %s um zu bestimmen mit was für einer Codelänge du Spielen möchtest" % (
            self.MINIMAL_CODELAENGE, self.MAXIMALE_CODELEANGE))
        user_input = input()
        print("\nDie Länge des Codes lautet: %s\n" % user_input)

        if not user_input.isdigit():
            print("Bitte gib eine Zahl ein, keine anderen Symbole! ")
            return self.NICHTZULAESSIGER_INPUT

        user_input_als_int = int(user_input)

        if self.MAXIMALE_CODELEANGE >= user_input_als_int >= self.MINIMAL_CODELAENGE:
            return user_input_als_int
        else:
            return self.NICHTZULAESSIGER_INPUT

    def get_codeleange(self) -> int:
        result = self.helper_get_codeleange()
        if result == -1:
            return self.get_codeleange()
        else:
            return result

    def spiel_neustarten(self):
        print("um das Spiel neu zu starten drücke 1")
        user_input = input()
        if user_input == "1" or user_input == 1:
            self.superhirn_spielen()

    def print_regeln(self):
        print('''
            Wilkommen bei Superhirn, bei diesem Spiel geht es darum, dass der Rater
            den Geheimen Code des Codierer errät.
            
            Dazu hat der Rater {} Runden Zeit.
            In jeder dieser Runden kann er einen Rateversuch machen der dann vom Codierer ausgewertet wird
            der Code kann aus bis zu 8 Farben bestehen
            [Rot = 1, Gruen = 2, Gelb = 3, Blau = 4, Orange = 5, Braun = 6, Weiss = 7, Schwarz = 8]
            und eine Länge von {} bis {}.
            
            Der Codierer vergibt Auswertungspins für jedes Codeelement 
            7 = Weiß für richtige Farbe aber falsche Position und 8 = Schwarz für richtige Farbe und richtige
            Position.
            und Enter um die Auswertung leer zu lassen. 
            
            Drücke eine Buchstaben oder eine Zahl um loszulegen, Viel Spaß.
        '''.format(self.MAXIMIMALE_RUNDNEANZAHL, self.MINIMAL_CODELAENGE, self.MAXIMALE_CODELEANGE))

        input()
