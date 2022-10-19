import unittest
from unittest.mock import MagicMock

from tap_adyen.adyen import Adyen


class TestAdyen(unittest.TestCase):
    def test_retrieve_csv(self):
        # Provide adyen credentials to run this test
        adyen: Adyen = Adyen(
            "report_user",
            "company_account",
            "user_password",
            "merchant_account",
            "False",
        )

        csv_url = "https://ca-live.adyen.com/reports/download/Company/Dualtech/dispute_report_2022_05_01.csv"
        rows = adyen.retrieve_csv(csv_url, None)
        self.assertTrue(len(rows > 0))
