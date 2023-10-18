import main1 as otp
import pytest
import unittest
from main1 import validate_email, generate_otp, send_email


class TestProgramFunctions(unittest.TestCase):

    def test_validate_email(self):

        result = validate_email("ommhatre2003@gmail.com")
        expected = True
        self.assertEqual(result, expected)

        result = validate_email("ryuzakil841@gmail.com")
        expected = True
        self.assertEqual(result, expected)

    def test_generate_otp(self):
        otp = generate_otp()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())


if __name__ == '__main__':
    pytest.main()