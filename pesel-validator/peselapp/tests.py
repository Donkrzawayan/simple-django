from django.test import SimpleTestCase

from .utils import validate_pesel


class ValidatePeselTests(SimpleTestCase):
    def test_invalid_length_returns_none(self):
        self.assertIsNone(validate_pesel("123"))

    def test_non_digit_returns_none(self):
        self.assertIsNone(validate_pesel("abcdefghijk"))

    def test_invalid_checksum_returns_none(self):
        self.assertIsNone(validate_pesel("44051401459")) # invalid checksum

    def _test_valid_pesel_returns_details(self, pesel, birthday, sex):
        details = validate_pesel(pesel)
        self.assertIsNotNone(details)
        self.assertIsInstance(details, dict)
        self.assertEqual(details["birthday"], birthday)
        self.assertEqual(details["sex"], sex)

    def test_valid_pesel_1800s(self):
        pesel = '88922400201'  # 1888-12-24, female
        birthday = '1888-12-24'
        self._test_valid_pesel_returns_details(pesel, birthday, 'Kobieta')

    def test_valid_pesel_1900s(self):
        pesel = '44051401458'  # valid PESEL (1944-05-14, male)
        birthday = '1944-05-14'
        self._test_valid_pesel_returns_details(pesel, birthday, 'Mężczyzna')

    def test_valid_pesel_2000s(self):
        pesel = '01210200114'  # 2001-01-02, male
        birthday = '2001-01-02'
        self._test_valid_pesel_returns_details(pesel, birthday, 'Mężczyzna')
