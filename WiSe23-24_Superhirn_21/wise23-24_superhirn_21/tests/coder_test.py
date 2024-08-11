import unittest
from unittest.mock import patch

from auswertungs_element import AuswertungsElement
from code_element import CodeElement
from coder import mensch_coder
from coder.coder import Coder
from coder.computer_coder import ComputerCoder
from coder.mensch_coder import MenschCoder
from spielbrett.spielbrett import Code, Auswertung


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.mensch_coder = MenschCoder()
        self.computer_coder = ComputerCoder()

    def test_get_color_names(self):
        list_of_ints = [1, 2, 3, 4]
        list_of_code_elements = [CodeElement(1), CodeElement(2),
                                 CodeElement(3), CodeElement(4)]
        code = Code(list_of_code_elements)
        result = Coder._get_color_names(list_of_ints)

        self.assertEqual(code.code, result.code)

    # -----------------------Computer_coder------------------------------------------
    def test_code_erstellen(self):
        computer_coder_test = ComputerCoder()
        code_laenge = 4
        code_auswahl = 5
        result = computer_coder_test.code_erstellen(code_laenge, code_auswahl)
        self.assertIsInstance(result, Code)
        self.assertEqual(len(result.code), code_laenge)
        for color_value in result.code:
            self.assertTrue(1 <= color_value.value <= code_auswahl)

    def test_code_auswerten_all_correct(self):
        ziel_code = Code([CodeElement(1), CodeElement(2), CodeElement(3), CodeElement(4)])
        code = Code([CodeElement(1), CodeElement(2), CodeElement(3), CodeElement(4)])
        result = self.computer_coder.code_auswerten(code, ziel_code)
        expected = [8, 8, 8, 8]
        self.assertEqual(result.auswertung, expected)

    def test_code_auswerten_correct_numbers_wrong_positions(self):
        ziel_code = Code([CodeElement(1), CodeElement(2), CodeElement(3), CodeElement(4)])
        code = Code([CodeElement(4), CodeElement(3), CodeElement(2), CodeElement(1)])
        result = self.computer_coder.code_auswerten(code, ziel_code)
        expected = [7, 7, 7, 7]
        self.assertEqual(result.code, expected)

    def test_code_auswerten_no_correct_numbers(self):
        ziel_code = Code([CodeElement(1), CodeElement(2), CodeElement(3), CodeElement(4)])
        code = Code([CodeElement(5), CodeElement(6), CodeElement(7), CodeElement(8)])
        result = self.computer_coder.code_auswerten(code, ziel_code)
        expected = []
        print(result.auswertung)

        self.assertEqual(result.auswertung, expected)
        self.assertEqual(result.auswertung, expected)

    def test_code_auswerten_all_correct2(self):
        ziel_code = Code([CodeElement(1), CodeElement(2), CodeElement(3), CodeElement(4)])
        code = Code([CodeElement(1), CodeElement(2), CodeElement(3), CodeElement(4)])
        result = self.computer_coder.code_auswerten(code, ziel_code)
        expected = Auswertung(
            [AuswertungsElement(8), AuswertungsElement(8), AuswertungsElement(8), AuswertungsElement(8)])
        self.assertEqual(result.auswertung, expected.auswertung)

    def test_code_auswerten_correct_numbers_wrong_positions2(self):
        ziel_code = Code([CodeElement(1), CodeElement(2), CodeElement(3), CodeElement(4)])
        code = Code([CodeElement(4), CodeElement(3), CodeElement(2), CodeElement(1)])
        result = self.computer_coder.code_auswerten(code, ziel_code)
        expected = Auswertung(
            [AuswertungsElement(7), AuswertungsElement(7), AuswertungsElement(7), AuswertungsElement(7)])
        self.assertEqual(result.get_auswertung(), expected.get_auswertung())

    # -------------------------------menschen_code-------------------------------
    def test_mensch_code_erstellen(self):
        mensch_coder_test = MenschCoder()
        code_laenge = 4
        code_auswahl = 7
        result = mensch_coder_test.code_erstellen(code_laenge, code_auswahl)
        self.assertIsInstance(result, Code)
        self.assertEqual(len(result.code), code_laenge)
        for color_value in result.code:
            self.assertTrue(1 <= color_value.value <= code_auswahl)

    def test_pruefer_valid_input(self):
        valid_input = '78'
        zielcode_laenge = 2
        result = self.mensch_coder.pruefer(valid_input, zielcode_laenge)
        self.assertTrue(result)

    def test_pruefer_invalid_characters(self):
        invalid_input = 'abc'
        zielcode_laenge = 3
        result = self.mensch_coder.pruefer(invalid_input, zielcode_laenge)
        self.assertFalse(result)

    def test_pruefer_invalid_length(self):
        invalid_input = '78'
        zielcode_laenge = 1
        result = self.mensch_coder.pruefer(invalid_input, zielcode_laenge)
        self.assertFalse(result)

    def test_pruefer_invalid_feedback_characters(self):
        invalid_input = 'abc'
        zielcode_laenge = 3
        result = self.mensch_coder.pruefer(invalid_input, zielcode_laenge)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
