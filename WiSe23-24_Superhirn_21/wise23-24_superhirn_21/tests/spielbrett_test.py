import unittest
from auswertungs_element import AuswertungsElement
from code_element import CodeElement
from spielbrett.spielbrett import Code, Auswertung, Spielbrett


class TestSpielbrett(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_code(self):
        code_elements = [CodeElement(1), CodeElement(2), CodeElement(3)]
        code_instance = Code(code_elements)
        self.assertEqual(code_instance.get_code(), code_elements)

    def test_get_auswertung(self):
        auswertung_elements = [AuswertungsElement(7), AuswertungsElement(7), AuswertungsElement(8)]
        auswertung_instance = Auswertung(auswertung_elements)
        actual_result = auswertung_instance.get_auswertung()
        print("Actual Result:", actual_result)
        print("Expected Result:", auswertung_elements)
        self.assertEqual(actual_result, auswertung_elements)

    def test_spielbrett_ausgeben(self):
        code_elements_1 = [CodeElement(1), CodeElement(2), CodeElement(3)]
        code_elements_2 = [CodeElement(4), CodeElement(5), CodeElement(6)]
        auswertung_elements_1 = [AuswertungsElement(7), AuswertungsElement(8), AuswertungsElement(7)]
        auswertung_elements_2 = [AuswertungsElement(8), AuswertungsElement(7), AuswertungsElement(8)]

        code_instance_1 = Code(code_elements_1)
        code_instance_2 = Code(code_elements_2)
        auswertung_instance_1 = Auswertung(auswertung_elements_1)
        auswertung_instance_2 = Auswertung(auswertung_elements_2)
        spielzug_1 = (code_instance_1, auswertung_instance_1)
        spielzug_2 = (code_instance_2, auswertung_instance_2)

        spielbrett_instance = Spielbrett([spielzug_1, spielzug_2], code_instance_1)
        print(spielbrett_instance.zielcode_ausgeben())
        expected_output = "Zielcode: 456\nSpielzug 1: 123Auswertung:  123\n"
        spielbrett_instance.spielbrett_ausgeben()
        self.assertEqual(spielbrett_instance.spielbrett_ausgeben(), expected_output)

    def test_spielzug_hinzufuegen(self):
        code_elements = [CodeElement(1), CodeElement(2), CodeElement(3)]
        auswertung_elements = [AuswertungsElement(1), AuswertungsElement(2), AuswertungsElement(3)]
        code_instance = Code(code_elements)
        auswertung_instance = Auswertung(auswertung_elements)
        spielbrett_instance = Spielbrett([], code_instance)

        spielbrett_instance.spielzug_hinzufuegen((code_instance, auswertung_instance))
        self.assertEqual(len(spielbrett_instance.spielbrett), 1)

    def test_zielcode_hinzufuegen(self):
        code_elements = [CodeElement(1), CodeElement(2), CodeElement(3)]
        code_instance = Code(code_elements)
        spielbrett_instance = Spielbrett([], Code([]))

        spielbrett_instance.zielcode_hinzufuegen(code_instance)
        self.assertEqual(spielbrett_instance.zielcode.get_code(), code_elements)

    def test_zielcode_ausgeben(self):
        code_elements = [CodeElement(1), CodeElement(2), CodeElement(3)]
        code_instance = Code(code_elements)
        spielbrett_instance = Spielbrett([], code_instance)
        self.assertEqual(spielbrett_instance.zielcode_ausgeben().get_code(), code_elements)


if __name__ == '__main__':
    unittest.main()
