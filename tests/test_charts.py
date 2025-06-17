import unittest
from charts import pokaz_saldo_miesieczne, pokaz_podsumowanie_kategorii

class TestCharts(unittest.TestCase):
    def test_pokaz_saldo_miesieczne_z_danymi(self):
        data = {
            "2025-06": 1000,
            "2025-07": -300
        }
        try:
            pokaz_saldo_miesieczne(data)
        except Exception as e:
            self.fail(f"pokaz_saldo_miesieczne zgłosiło wyjątek: {e}")

    def test_pokaz_saldo_miesieczne_brak_danych(self):
        try:
            pokaz_saldo_miesieczne({})
        except Exception as e:
            self.fail(f"pokaz_saldo_miesieczne (brak danych) zgłosiło wyjątek: {e}")

    def test_pokaz_podsumowanie_kategorii_z_danymi(self):
        data = {
            "Jedzenie": -200,
            "Transport": -100
        }
        try:
            pokaz_podsumowanie_kategorii(data)
        except Exception as e:
            self.fail(f"pokaz_podsumowanie_kategorii zgłosiło wyjątek: {e}")

    def test_pokaz_podsumowanie_kategorii_brak_danych(self):
        try:
            pokaz_podsumowanie_kategorii({})
        except Exception as e:
            self.fail(f"pokaz_podsumowanie_kategorii (brak danych) zgłosiło wyjątek: {e}")

if __name__ == "__main__":
    unittest.main()
