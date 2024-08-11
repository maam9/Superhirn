import json

import requests
from requests import Timeout
import socket

from auswertungs_element import AuswertungsElement
from code_element import CodeElement
from coder.coder import Coder
from spielbrett.spielbrett import Code, Auswertung


class SuperhirnDTO:
    def __init__(self, gameid, gamerid, positions, colors, value):
        self.gameid = gameid
        self.gamerid = gamerid
        self.positions = positions
        self.colors = colors
        self.value = value

    def to_dict(self):
        return {
            "gameid": self.gameid,
            "gamerid": self.gamerid,
            "positions": self.positions,
            "colors": self.colors,
            "value": self.value
        }


class NetzwerkCoder(Coder):

    def code_erstellen(self, code_laenge: int, code_auswahl: int) -> Code:
        # hier wird 0 auf tatsächliche codeaushwahl geändert
        self.code_auswahl = code_auswahl
        # at the moment a pointless objekt the intent is to give a empty Code
        return Code([CodeElement(1)])

    def code_auswerten(self, code: Code, zielcode: Code) -> Auswertung:
        payload = SuperhirnDTO(self.game_id, self.gamer_id, len(code.code), self.code_auswahl,
                               code.get_code_to_string())
        response = self.helper_sendrequest(json.dumps(payload.to_dict()))
        response_objekt = self.helper_response_converter(response)
        self.game_id = response_objekt.gameid
        auswertungs_elemente_liste = []
        for e in response_objekt.value:
            auswertungs_elemente_liste.append(AuswertungsElement(int(e)))
        return Auswertung(auswertungs_elemente_liste)

    def helper_sendrequest(self, payload, timeout=10):
        url = f"http://{self.ip_address}:{self.port}/"

        try:

            response = requests.post(url, json=payload, timeout=timeout)

            # Check the HTTP status code
            if response.status_code == 200:
                print("Anfrage war erfolgreich!")
                return response.text
            else:
                print(f"Anfrage misserfolgte mit dem Code Status {response.status_code}.")
                return f"Fehler: {response.status_code}"

        except Timeout:
            print(f"Die Anfrage wurde nach {Timeout}-Sekunden abgebrochen.")
            return "Timeout Fehler"

    @staticmethod
    def helper_response_converter(response) -> SuperhirnDTO:
        tmp_dic = json.loads(response)
        response_objekt = SuperhirnDTO(**tmp_dic)
        return response_objekt



    def __init__(self, ip_address, port):
        super().__init__()
        self.ip_address = ip_address
        self.port = port
        self.gamer_id = "2_1"
        self.game_id = ""
        self.code_auswahl = 0


