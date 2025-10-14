import unittest
from unittest.mock import patch
import Andy_zadania


class TestZadania(unittest.TestCase):

    @patch('builtins.input', side_effect=['Piotr'])
    @patch('builtins.print')
    def test_zadanie1(self, mock_print, mock_input):
        Andy_zadania.zadanie1()
        mock_print.assert_called_with('Cześć', 'Piotr')

    @patch('builtins.input', side_effect=['3', '4'])
    @patch('builtins.print')
    def test_zadanie2(self, mock_print, mock_input):
        Andy_zadania.zadanie2()
        mock_print.assert_called_with('Suma to:', 7.0)

    @patch('builtins.input', return_value='8')
    @patch('builtins.print')git remote add origin https://github.com/Excellent-English/my_python_scripts.git

    def test_zadanie3_even(self, mock_print, mock_input):
        Andy_zadania.zadanie3()
        mock_print.assert_called_with('Liczba jest parzysta')

    @patch('builtins.input', side_effect=['1', '2', '3'])
    @patch('builtins.print')
    def test_zadanie4(self, mock_print, mock_input):
        Andy_zadania.zadanie4()
        mock_print.assert_called_with('Największa to:', 3)

    @patch('builtins.input', return_value='abc')
    @patch('builtins.print')
    def test_zadanie5(self, mock_print, mock_input):
        Andy_zadania.zadanie5()
        mock_print.assert_called_with('Odwrócony tekst:', 'cba')

    @patch('builtins.print')
    def test_zadanie6(self, mock_print):
        Andy_zadania.zadanie6()
        self.assertEqual(mock_print.call_count, 10)
        mock_print.assert_any_call(1)
        mock_print.assert_any_call(10)

    @patch('builtins.print')
    def test_zadanie7(self, mock_print):
        Andy_zadania.zadanie7()
        mock_print.assert_called_with('Średnia:', 6.0)

    @patch('builtins.input', side_effect=['10', '5', '+'])
    @patch('builtins.print')
    def test_zadanie8_add(self, mock_print, mock_input):
        Andy_zadania.zadanie8()
        mock_print.assert_called_with('Wynik: 15.0')


if __name__ == '__main__':
    unittest.main()