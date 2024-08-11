from abc import ABC, abstractmethod

from spielbrett.spielbrett import Code, Auswertung


class Coder(ABC):
    """
    Coder setzt Zielcode fest und Wertet Code aus
    """

    def __init__(self):
        pass

    @abstractmethod
    def code_erstellen(self, code_laenge: int, code_auswahl: int) -> Code:
        """
        :param code_auswahl:
        :param code_laenge: länge des Zielcodes
        :return: Zielcode fürs spielbrett
        """
        raise NotImplementedError("Method not implemented yet")

    @abstractmethod
    def code_auswerten(self, code: Code, zielcode: Code) -> Auswertung:
        raise NotImplementedError("Method not implemented yet")
