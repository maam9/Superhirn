import unittest
from unittest import mock
from unittest.mock import patch

from coder.computer_coder import ComputerCoder
from coder.mensch_coder import MenschCoder
from rater.computer_rater import ComputerRater
from rater.mensch_rater import MenschRater
from superhirn_controller import SuperhirnController


class MyTestCase(unittest.TestCase):

    def test_creationofController(self):
        self.assertEqual(True, True)  # add assertion here

    # ---helper_get_codeleange
    def _helper_test_get_codeleange(self, input_value, expected_result):
        with mock.patch("builtins.input", return_value=input_value):
            superhirn_c = SuperhirnController()
            result = superhirn_c.helper_get_codeleange()
            self.assertEqual(result, expected_result)

    def test_get_codeleange_zulaessiger_input(self):
        self._helper_test_get_codeleange("4", 4)

    def test_get_codeleange_zulaessiger_input_5(self):
        self._helper_test_get_codeleange("5", 5)

    def test_get_codeleange_maximum_fail(self):
        self._helper_test_get_codeleange("3", -1)

    def test_get_codeleange_minimum_fail(self):
        self._helper_test_get_codeleange("3", -1)

    def test_get_codeleange_minimum_fail_buchstaben(self):
        self._helper_test_get_codeleange("asdfasd", -1)

    # ---helper_get_code_auswahl
    def _helper_test_get_code_auswahl(self, input_value, expected_result):
        with mock.patch("builtins.input", return_value=input_value):
            superhirn_c = SuperhirnController()
            result = superhirn_c.helper_get_code_auswahl()
            self.assertEqual(result, expected_result)

    def test_get_code_auswahl_zulaessiger_input(self):
        self._helper_test_get_code_auswahl("7", 7)

    def test_get_code_auswahl_maximum_fail(self):
        self._helper_test_get_code_auswahl("9", -1)

    def test_get_code_auswahl_minimum_fail(self):
        self._helper_test_get_code_auswahl("1", -1)

    def test_get_code_auswahl_minimum_fail_buchstaben(self):
        self._helper_test_get_code_auswahl("asdfasd", -1)

        # ---helper_getplayer_roll

    def _helper_helper_getplayer_roll(self, input_value, expected_result):
        with mock.patch("builtins.input", return_value=input_value):
            superhirn_c = SuperhirnController()
            result = superhirn_c.helper_getplayer_roll()
            self.assertTrue(isinstance(result[0], expected_result[0]))
            self.assertTrue(isinstance(result[1], expected_result[1]))

    def test_getplayer_roll_mensch_coder(self):
        self._helper_helper_getplayer_roll("0", (MenschCoder, ComputerRater))

    def test_getplayer_roll_computer_coder(self):
        self._helper_helper_getplayer_roll("1", (ComputerCoder, MenschRater))

    def test_getplayer_roll_minimum_fail(self):
        self._helper_helper_getplayer_roll("1", (ComputerCoder, MenschRater))

    def _helper_helper_getplayer_roll_error(self, input_value):
        with self.assertRaises(ValueError):
            with mock.patch("builtins.input", return_value=input_value):
                superhirn_c = SuperhirnController()
                superhirn_c.helper_getplayer_roll()

    def test_getplayer_roll_maximum_fail(self):
        self._helper_helper_getplayer_roll_error("2")

    def test_getplayer_roll_minimum_fail_buchstaben(self):
        self._helper_helper_getplayer_roll_error("asdfasd")

    @patch("builtins.input", side_effect=["7", "sadasd", "5"])
    def test_get_codeleangeSucces(self):
        superhirn_c = SuperhirnController()
        self.assertEqual(5, superhirn_c.get_codeleange())

    @patch("builtins.input", side_effect=["10", "sadasd", "-1", "5"])
    def test_get_code_auswahl_Succes(self):
        superhirn_c = SuperhirnController()
        self.assertEqual(5, superhirn_c.get_code_auswahl())


if __name__ == '__main__':
    unittest.main()
