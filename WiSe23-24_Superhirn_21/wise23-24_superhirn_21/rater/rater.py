from abc import ABC, abstractmethod

from spielbrett.spielbrett import Spielbrett, Code


class Rater(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def code_raten(self, spielbrett: Spielbrett, codelaenge: int, code_auswahl: int) -> Code:
        """in methoden kopf hinzufügen, codeLänge und CodeAuswahl vom Controller Muss in der Abstrakten Klasse """
        raise NotImplementedError("Method not implemented yet")
