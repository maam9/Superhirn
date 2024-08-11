import unittest
from code_element import CodeElement
from coder.computer_coder import ComputerCoder
from coder.mensch_coder import MenschCoder
from rater.computer_rater import ComputerRater
from rater.mensch_rater import MenschRater
from spielbrett.spielbrett import Code, Spielbrett

from unittest.mock import MagicMock, patch


class TestComputerCoder(unittest.TestCase):
    # Computer

    def test_einfacherBanalertestMitEnumUndListen(self):
        list1 = [CodeElement.Blau, CodeElement.Gelb]
        list2 = [CodeElement.Blau, CodeElement.Gelb]
        list3 = [CodeElement.Blau, CodeElement.Braun]

        self.assertListEqual(list1, list2)

    # Test1: Erstellt der Comp ein Random Code die erstellten Code dürfen nicht gleich sein
    def test_code_erstellen(self):
        computer_coder = ComputerCoder()

        code1 = computer_coder.code_erstellen(4, 3)
        self.assertEqual(len(code1.get_code()), 4)

        code2 = computer_coder.code_erstellen(4, 3)
        self.assertEqual(len(code2.get_code()), 4)

        # Überprüfe, ob die generierten Codes unterschiedlich sind (random)
        self.assertNotEqual(code1.get_code(), code2.get_code())

        # Überprüfung wirklich CodeElemente
        for codeElem in code1.get_code():
            self.assertTrue(isinstance(codeElem, CodeElement))
        for codeElem in code2.get_code():
            self.assertTrue(isinstance(codeElem, CodeElement))

        codeenumenthalten = [CodeElement.Rot, CodeElement.Gruen, CodeElement.Gelb, CodeElement.Blau]
        self.assertListEqual(code1.get_code(), codeenumenthalten)
        self.assertListEqual(code2.get_code(), codeenumenthalten)

    # Test2: Wird die Codelänge nicht eingehalten (entweder 4 oder 5)
    def test_codelaengeFalsch(self):
        computer_coder = ComputerCoder()

        with self.assertRaises(ValueError):
            computer_coder.code_erstellen(0, 4)

    def test_codelaengeFalsch2(self):
        computer_coder = ComputerCoder()

        with self.assertRaises(ValueError):
            computer_coder.code_erstellen(3, 4)

    def test_codelaengeFalsch3(self):
        computer_coder = ComputerCoder()

        with self.assertRaises(ValueError):
            computer_coder.code_erstellen(6, 4)

    # Test3: Wird die Codeauswahl nicht eingehalten (entweder 2-8)
    def test_codeauswahlFalsch(self):
        computer_coder = ComputerCoder()

        with self.assertRaises(ValueError):
            computer_coder.code_erstellen(5, 9)

    def test_codeauswahlFalsch2(self):
        computer_coder = ComputerCoder()

        with self.assertRaises(ValueError):
            computer_coder.code_erstellen(4, 100)

    def test_codeauswahlFalsch3(self):
        computer_coder = ComputerCoder()

        with self.assertRaises(ValueError):
            computer_coder.code_erstellen(4, 0)

    # Test4: Mit richtigen Parametern und sollte deswegen keine ValueERror werfen
    def test_codeMitRichtigenParam(self):
        computer_coder = ComputerCoder()
        try:
            code = computer_coder.code_erstellen(4, 3)
        except ValueError:
            self.fail("Die code_erstellen-Methode sollte keine ValueError mit gültigen Parametern werfen.")

    def test_codeMitRichtigenParam2(self):
        computer_coder = ComputerCoder()
        try:
            code = computer_coder.code_erstellen(5, 8)
        except ValueError:
            self.fail("Die code_erstellen-Methode sollte keine ValueError mit gültigen Parametern werfen.")

    # Test5: ZielCode, parameter Auswertung
    # TODO: Mit Max Gemacht, BZW IDEEN
    def test_zielCodeAuswerten(self):
        computer_coder = ComputerCoder()
        code = computer_coder.code_erstellen(4, 3)
        self.assertEqual(len(code.get_code()), 4)

        # Get_code in Spielbrett gibt eine Liste zurück wenn ich mich nicht täusche
        # ist es dann nicht überflüssig eine Neue Liste zuerstellen
        # Todo: Einmal bestätigen
        # Durch iterieren mit der for schleife (Ob ale Vom Typ CodeElement sind)
        for codeElem in code.get_code():
            self.assertTrue(isinstance(codeElem, CodeElement))

        # Hier ist die überprüfung der ListenElemente
        code_enum_enthalten = [CodeElement.Rot, CodeElement.Gruen, CodeElement.Gelb, CodeElement.Blau]
        self.assertListEqual(code.get_code(), code_enum_enthalten)


class TestMenschCoder(unittest.TestCase):
    # Test1: Ungültige Parameter eingabe(für codelaenge und auswahl)
    def test_ungueltigeParameter(self):
        mensch_coder = MenschCoder()

        with self.assertRaises(ValueError):
            mensch_coder.code_erstellen(9, 9)

    def test_ungueltigeParameter2(self):
        mensch_coder = MenschCoder()

        with self.assertRaises(ValueError):
            mensch_coder.code_erstellen(0, 0)

    def test_ungueltigeParameter3(self):
        mensch_coder = MenschCoder()

        with self.assertRaises(ValueError):
            mensch_coder.code_erstellen(100, 100)

    # Test2: richtige Auswertung mit richtigen Parametern
    # def test_codelaengeFalsch(self):

    # Test3: Ungültige Parameter ein gabe(für codelaenge und richtige auwahl)
    # Test4: Ungültige Parameter eingabe(für richtige codelaenge und auwahl)
    # Test5: String eingabe_statt Int"


"=========================================================="
"================= CODER KLASSE TEST======================="
"=========================================================="

"-------------------Computer RATERR--------------------------"


class TestComputerRater(unittest.TestCase):
    # Test1: random Codes mit Laenge 4 und richtige Code Auswahl
    def test_code_raten_laenge_vier(self):
        # Erstelle ein Mock-Objekt für das Spielbrett
        mock_spielbrett = MagicMock(spec=Spielbrett)
        codelaenge = 4
        code_auswahl = 7

        # Erstelle ein Mock-Objekt für den Zielcode
        mock_zielcode = MagicMock(spec=Code)
        mock_spielbrett.zielcode = mock_zielcode

        dummy_zielcode = Code([CodeElement.Rot, CodeElement.Gruen, CodeElement.Gelb, CodeElement.Blau])
        mock_zielcode.get_code.return_value = dummy_zielcode.get_code()

        computer_rater = ComputerRater()

        rateversuch = computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        # Ausgabe der generierten Codes
        print("Generierter Code:")
        print([element.name for element in rateversuch.get_code()])

    # Test2: random Code erstellt mit Laenge 5 und richtige Code Auswahl
    def test_code_raten_laenge_fuenf(self):
        # Erstelle ein Mock-Objekt für das Spielbrett
        mock_spielbrett = MagicMock(spec=Spielbrett)
        codelaenge = 5
        code_auswahl = 2

        # Erstelle ein Mock-Objekt für den Zielcode
        mock_zielcode = MagicMock(spec=Code)
        mock_spielbrett.zielcode = mock_zielcode

        dummy_zielcode = Code(
            [CodeElement.Rot, CodeElement.Gruen, CodeElement.Gelb, CodeElement.Blau, CodeElement.Blau])
        mock_zielcode.get_code.return_value = dummy_zielcode.get_code()

        computer_rater = ComputerRater()
        rateversuch = computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        # Ausgabe der generierten Codes
        print("Generierter Code:")
        print([element.name for element in rateversuch.get_code()])

        # mock_zielcode.get_code.assert_called_once()

    # Test3: Gültige Enum:Parameter
    def test_code_raten_ungueltige_Enum(self):
        mock_spielbrett = MagicMock(spec=Spielbrett)

        codelaenge = 5
        code_auswahl = 10
        computer_rater = ComputerRater()

        try:
            # Erstelle ein Mock-Objekt für den Zielcode
            mock_zielcode = MagicMock(spec=Code)
            mock_spielbrett.zielcode = mock_zielcode
            computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        except ValueError:
            print("Nicht in der Enum enthaltene Code Auswahl")

    # Test4: Ungültige Codelänge
    def test_code_raten_ungueltige_codelaenge(self):
        mock_spielbrett = MagicMock(spec=Spielbrett)

        codelaenge = 6
        code_auswahl = 7
        computer_rater = ComputerRater()

        try:
            # pass = Platzhalter, ohne Code funktioniert es trotzdem
            # Erstelle ein Mock-Objekt für den Zielcode
            mock_zielcode = MagicMock(spec=Code)
            mock_spielbrett.zielcode = mock_zielcode
            computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        except ValueError:
            print("Ungültige Codelänge")

    # Test5: Negative Codelänge
    def test_code_raten_negative_codelaenge(self):
        mock_spielbrett = MagicMock(spec=Spielbrett)

        codelaenge = -4
        code_auswahl = 7
        computer_rater = ComputerRater()

        try:
            # pass = Platzhalter, ohne Code funktioniert es trotzdem
            # Erstelle ein Mock-Objekt für den Zielcode
            mock_zielcode = MagicMock(spec=Code)
            mock_spielbrett.zielcode = mock_zielcode
            computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        except ValueError:
            print("Negative Codelänge")

    # Test6: Negative Code Auswahl
    def test_code_raten_negative_code_auswahl(self):
        mock_spielbrett = MagicMock(spec=Spielbrett)

        codelaenge = 4
        code_auswahl = -7
        computer_rater = ComputerRater()

        try:
            # pass = Platzhalter, ohne Code funktioniert es trotzdem
            # Erstelle ein Mock-Objekt für den Zielcode
            mock_zielcode = MagicMock(spec=Code)
            mock_spielbrett.zielcode = mock_zielcode
            computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        except ValueError:
            print("Negative Code Auswahl")

    # Test7: Zu große Codelänge
    def test_code_raten_zu_grosse_codelaenge(self):
        mock_spielbrett = MagicMock(spec=Spielbrett)

        codelaenge = 12431
        code_auswahl = 7
        computer_rater = ComputerRater()

        try:
            # pass = Platzhalter, ohne Code funktioniert es trotzdem
            # Erstelle ein Mock-Objekt für den Zielcode
            mock_zielcode = MagicMock(spec=Code)
            mock_spielbrett.zielcode = mock_zielcode
            computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        except ValueError:
            print("Zu große Codelänge")

    # Test8: Zu große Code Auswahl
    def test_code_raten_zu_grosse_code_auswahl(self):
        mock_spielbrett = MagicMock(spec=Spielbrett)

        codelaenge = 4
        code_auswahl = 243312
        computer_rater = ComputerRater()

        try:
            # pass = Platzhalter, ohne Code funktioniert es trotzdem
            # Erstelle ein Mock-Objekt für den Zielcode
            mock_zielcode = MagicMock(spec=Code)
            mock_spielbrett.zielcode = mock_zielcode
            computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        except ValueError:
            print("Zu große Code Auswahl")

    # Test9 : ungueltige eingaben
    def test_code_ungueltige_parametern(self):
        mock_spielbrett = MagicMock(spec=Spielbrett)
        mock_zielcode = MagicMock(spec=Code)
        mock_spielbrett.zielcode = mock_zielcode
        codelaenge = 4  # Sobald du Codelänge änderst, musst du dummy_zielcode anpassen
        code_auswahl = 8

        dummy_zielcode = Code([CodeElement.Rot, CodeElement.Gruen, CodeElement.Gelb, CodeElement.Blau])
        mock_zielcode.get_code.return_value = dummy_zielcode.get_code()

        computer_rater = ComputerRater()
        rateversuch = computer_rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        # Ausgabe der generierten Codes
        print("Generierter Code:")
        print([element.name for element in rateversuch.get_code()])

        # mock_zielcode.get_code.assert_called_once()

        # Zusätzliche Überprüfungen
        self.assertEqual(len(rateversuch.get_code()), len(dummy_zielcode.get_code()),
                         "Die Länge des generierten Codes stimmt nicht mit dem Zielcode überein.")

        valid_enum_values = [enum_value.value for enum_value in CodeElement]
        for element in rateversuch.get_code():
            self.assertIn(element.value, valid_enum_values, f"Ungültiger Enum-Wert im generierten Code: {element}")


"""-------------------MENSCH RATERR--------------------------"""


class TestMenschRater(unittest.TestCase):

    # Test1: Code mit Länge 4 und Auswahl 6
    @patch('builtins.input', side_effect=["2345"])  # Simuliere eine Eingabe mit der richtigen Länge
    def test_code_raten_richtig(self, mock_input):
        # Testfall 1: Gültige Eingabe
        mensch_rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)

        code = mensch_rater.code_raten(mock_spielbrett, 4, 6)  # Beispiel für eine gültige Eingabe
        self.assertEqual(len(code.code), 4)

    # Test2: Code mit einer einzigen Enum
    @patch('builtins.input', side_effect=["1111"])  # Simuliere eine Eingabe mit der richtigen Länge
    def test_code_raten_mit_einem_Enum(self, mock_input):
        # Testfall 1: Gültige Eingabe
        mensch_rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)
        list1 = [CodeElement.Rot, CodeElement.Rot, CodeElement.Rot, CodeElement.Rot]

        code = mensch_rater.code_raten(mock_spielbrett, 4, 6)  # Beispiel für eine gültige Eingabe
        self.assertListEqual(code.code, list1)

    """def test_code_raten_zwei_Eingaben(self):
        mensch_rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)

        mensch_rater.code_raten(mock_spielbrett,4,5)
        self.assertTrue(False)"""

    # zwei mal hintereinander, erst falsch und dann richtig

    # Test3: Code entspricht nicht der Code Auswahl
    @patch('builtins.input', side_effect=["1151", "1112"])  # Simuliere eine Eingabe mit der richtigen Länge
    def test_code_raten_mit_einem_Enum_in_code_auswahl(self, mock_input):
        # Testfall 1: Gültige Eingabe
        mensch_rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)
        erwartet = [CodeElement(1), CodeElement(1), CodeElement(1), CodeElement(2)]

        try:
            code = mensch_rater.code_raten(mock_spielbrett, 4, 2)  # Beispiel für eine gültige Eingabe
        except ValueError:
            print("Zahlen entsprechen nicht der Code Auswahl")
        finally:
            self.assertEqual(code.code, erwartet)

    # Test4: Code ist negativ
    @patch('builtins.input', side_effect=["-2345", "dbbbr", "5555"])  # Simuliere eine Eingabe mit der richtigen Länge
    def test_code_raten_negative_code(self, mock_input):
        # Testfall 1: Gültige Eingabe
        mensch_rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)

        try:
            mensch_rater.code_raten(mock_spielbrett, 4, 6)  # Beispiel für eine gültige Eingabe
        except ValueError:
            print("Negativer Code")

    # Test5: Zu langer Code
    @patch('builtins.input', side_effect=["12345", "1231"])  # Simuliere eine Eingabe mit der richtigen Länge
    def test_mensch_zu_langer_codelaenge(self, mock_input):
        rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)
        codelaenge = 4
        code_auswahl = 8

        try:
            rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)  # Beispiel für eine gültige Eingabe
        except ValueError:
            print("Falsche Codelänge")

    # Test6: ob Code_raten von MenschRater ein Code ausgibt
    @patch('builtins.input', side_effect=["12345", "8888"])  # Simuliere eine Eingabe mit der richtigen Länge
    def test_mensch_code_existiert(self, mock_input):
        rater = MenschRater()  # Annahme: Es gibt eine Klasse MenschRater mit der Methode code_raten
        mock_spielbrett = MagicMock(spec=Spielbrett)
        codelaenge = 4  # Werte können angepasst werden
        code_auswahl = 8

        try:
            result = rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)
            self.assertIsNotNone(result)
            self.assertTrue(isinstance(result, Code))
        except ValueError:
            print("Ungültige Codelänge")

    # Test7: ein kurze eingabe und wirft Exception
    @patch('builtins.input', side_effect=["12", "12121"])  # Simuliere eine Eingabe mit falscher Länge
    def test_zu_kurze__eingabe(self, mock_input):
        rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)
        codelaenge = 5
        code_auswahl = 8  # Wenn die Codelänge 4 ist, kann man eine Code Auswahl > 4

        try:
            rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)
        except ValueError:
            print("Falsche Codelänge")

    # Test8: zwei Eingaben hintereinander
    @patch('builtins.input', side_effect=["1234", "6790"])  # Simuliere zwei Eingaben, die zweite ist korrekt
    def test_rekursion(self, mock_input):
        rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)
        codelaenge = 4
        code_auswahl = 4

        result = rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, Code))

    # Test9: zu große laenge
    @patch('builtins.input', side_effect=["1" * 10000])  # Simuliere eine extrem lange Eingabe
    def test_extrem_lange_eingabe(self, mock_input):
        rater = MenschRater()
        mock_spielbrett = MagicMock(spec=Spielbrett)
        codelaenge = 10000
        code_auswahl = 8

        try:
            result = rater.code_raten(mock_spielbrett, codelaenge, code_auswahl)
            self.assertTrue(isinstance(result, Code))

        except ValueError:
            print("Zu große Coelänge")
