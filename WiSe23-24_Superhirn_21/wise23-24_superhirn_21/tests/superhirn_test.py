import unittest
from unittest.mock import patch

from auswertungs_element import AuswertungsElement
from code_element import CodeElement
from coder.computer_coder import ComputerCoder
from coder.mensch_coder import MenschCoder
from rater.computer_rater import ComputerRater
from spielbrett.spielbrett import Spielbrett, Code
from superhirn.superhirn import Superhirn


class TestSuperhirn(unittest.TestCase):
    def test_creation_of_superhirn(self):
        self.assertEqual(True, True)  # add assertion here

    "Set Up"

    def setUp(self):
        # Beispiel-Spieler für Tests
        self.spieler = (ComputerCoder(), ComputerRater())  # 4
        self.superhirn = Superhirn(self.spieler, 10, 8, 5)

    # Testet die Initialisierung der Klasse Superhirn
    def test_initialisierung(self):
        self.assertIsNone(self.superhirn.spielbrett)
        self.assertEqual(self.superhirn.spieler, self.spieler)
        self.assertEqual(self.superhirn.code_laenge, 4)
        self.assertEqual(self.superhirn.code_auswahl, CodeElement)
        self.assertEqual(self.superhirn.max_runden, 10)

    # Testet den Spielstatus
    def test_spielstatus_ueberpruefen_sieg(self):
        zielcode2 = Code([CodeElement.Rot, CodeElement.Gelb, CodeElement.Blau, CodeElement.Blau])
        spielbretliste = list()
        spielbrett = Spielbrett(spielbretliste, zielcode2)
        with patch.object(spielbrett, "runden_zaehler", return_value=10):
            superhirn = Superhirn((MenschCoder(), ComputerRater()), 10, 5, 8)
            superhirn.spielbrett = spielbrett
            self.assertTrue(superhirn.helper_coder_sieg())

    def test_spielstatus_ueberpruefen_false(self):
        zielcode2 = Code([CodeElement.Rot, CodeElement.Gelb, CodeElement.Blau, CodeElement.Blau])
        spielbretliste = list()
        spielbrett = Spielbrett(spielbretliste, zielcode2)
        with patch.object(spielbrett, "runden_zaehler", return_value=0):
            superhirn = Superhirn((MenschCoder(), ComputerRater()), 10, 5, 8)
            superhirn.spielbrett = spielbrett
            self.assertTrue(superhirn.helper_coder_sieg())

    def test_spielstatus_ueberpruefen_false_minus(self):
        zielcode2 = Code([CodeElement.Rot, CodeElement.Gelb, CodeElement.Blau, CodeElement.Blau])
        spielbretliste = list()
        spielbrett = Spielbrett(spielbretliste, zielcode2)
        with patch.object(spielbrett, "runden_zaehler", return_value=-1):
            superhirn = Superhirn((MenschCoder(), ComputerRater()), 10, 5, 8)
            superhirn.spielbrett = spielbrett
            self.assertTrue(superhirn.helper_coder_sieg())

    def test_helper_rater_sieg_yes(self):
        zielcode2 = Code([CodeElement.Rot, CodeElement.Gelb, CodeElement.Blau, CodeElement.Blau])
        spielbretliste = list()
        spielbrett = Spielbrett(spielbretliste, zielcode2)
        auswertung2 = [AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.schwarzer_pin]
        list_element = (list(), auswertung2)
        with patch.object(spielbrett, "spielbrett", new=[list_element, list_element]):
            superhirn = Superhirn((MenschCoder(), ComputerRater()), 10, 4, 8)
            superhirn.spielbrett = spielbrett
            self.assertTrue(superhirn.helper_rater_sieg())

    def test_helper_rater_sieg_false_notonlyblack(self):
        zielcode2 = Code([CodeElement.Rot, CodeElement.Gelb, CodeElement.Blau, CodeElement.Blau])
        spielbretliste = list()
        spielbrett = Spielbrett(spielbretliste, zielcode2)
        auswertung2 = [AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.weißer_pin]
        list_element = (list(), auswertung2)
        with patch.object(spielbrett, "spielbrett", new=[list_element, list_element]):
            superhirn = Superhirn((MenschCoder(), ComputerRater()), 10, 4, 8)
            superhirn.spielbrett = spielbrett
            self.assertFalse(superhirn.helper_rater_sieg())

    def test_helper_rater_sieg_false_with_empty(self):
        zielcode2 = Code([CodeElement.Rot, CodeElement.Gelb, CodeElement.Blau, CodeElement.Blau])
        spielbretliste = list()
        spielbrett = Spielbrett(spielbretliste, zielcode2)
        auswertung2 = [AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.schwarzer_pin,
                       AuswertungsElement.schwarzer_pin]
        list_element = (list(), auswertung2)
        with patch.object(spielbrett, "spielbrett", new=[list_element, list_element]):
            superhirn = Superhirn((MenschCoder(), ComputerRater()), 10, 4, 8)
            superhirn.spielbrett = spielbrett
            self.assertFalse(superhirn.helper_rater_sieg())

    # Testet, dass Rundenanzahl erhöht wird, wenn ein Zug getätigt wurde
    def test_max_runden_erreicht(self):
        self.superhirn.rundenanzahl = self.superhirn.max_runden - 1  # Rundenanzahl auf kurz vor Maximum setzen
        self.superhirn.spielzug()  # Einen Zug durchführen

        # Überprüfen, dass die Rundenanzahl auf das Maximum erhöht wurde
        self.assertEqual(self.superhirn.rundenanzahl, self.superhirn.max_runden)
