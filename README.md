# Budżet osobisty – Instrukcja obsługi

## Opis

Aplikacja pozwala na zarządzanie osobistymi finansami za pomocą przejrzystego **graficznego interfejsu użytkownika (GUI)**. Obsługuje wielu użytkowników, zapisuje dane do plików CSV i umożliwia:

- dodawanie, edytowanie i usuwanie transakcji,
- wizualizację danych na wykresach (saldo miesięczne, suma wg kategorii),
- zapisywanie raportów tekstowych,
- automatyczny zapis i odczyt danych użytkownika.

---

## Uruchomienie aplikacji

1. **Zainstaluj wymagane biblioteki**:

pip install matplotlib

2. **Uruchom aplikację**:

python gui.py

---

## Logowanie i rejestracja

- Przy uruchomieniu aplikacji pojawia się okno logowania.
- Możesz się **zalogować** lub **zarejestrować nowe konto**.
- Dane logowania (SHA-256) są przechowywane w pliku `data/users.csv`.
- Transakcje są zapisywane w osobnych plikach CSV dla każdego użytkownika (`data/<login>_transactions.csv`).

---

## Funkcjonalności po zalogowaniu

1. **Dodaj transakcję** – podaj kwotę, kategorię, datę (`RRRR-MM-DD`) i opis.

2. **Edytuj transakcję** – wybierz istniejący wpis z tabeli i edytuj dane.

3. **Usuń transakcję** – zaznacz wiersz i usuń kliknięciem.

4. **Pokaż saldo miesięczne** – wyświetla wykres słupkowy z miesięcznym bilansem.

5. **Pokaż sumy kategorii** – pokazuje wykres poziomy z podsumowaniem wydatków i przychodów wg kategorii.

6. **Zapis do pliku** – dane zapisywane są automatycznie po wylogowaniu.

7. **Wylogowanie** – zapisuje dane i powraca do ekranu logowania.

---

## Struktura plików

- `gui.py` – główny plik uruchamiający interfejs graficzny
- `logic.py` – klasy: `Transaction`, `Budget` i logika działania
- `data.py` – obsługa CSV: odczyt i zapis transakcji
- `auth.py` – funkcje rejestracji, logowania i walidacji użytkowników
- `utils.py` – zapis raportu tekstowego
- `charts.py` – wykresy matplotlib
- `tests/` – testy jednostkowe w `unittest`

---

## Dane i bezpieczeństwo

- Dane użytkownika zapisywane są lokalnie w `data/`.
- Hasła są szyfrowane przy pomocy algorytmu SHA-256.
- Raport można zapisać do pliku `raport.txt`.

---

## Testowanie

Folder `tests/` zawiera testy jednostkowe m.in. dla:
- logiki finansowej (`Budget`, `Transaction`),
- zapisu i odczytu plików,
- rejestracji i logowania,
- raportu tekstowego (`utils.py`).

---

## Wymagania

- Python 3.9 lub nowszy
- Biblioteki: `tkinter`, `matplotlib`

---

## Wnioski

Projekt zakładał stworzenie graficznej aplikacji do zarządzania budżetem osobistym, umożliwiającej użytkownikom rejestrowanie i analizowanie własnych finansów. Zrealizowano wszystkie główne funkcjonalności, takie jak dodawanie, edycja i usuwanie transakcji, prezentowanie wykresów salda oraz kategorii, a także automatyczne zapisywanie danych do plików CSV. Interfejs graficzny oparty na tkinter znacznie ułatwia korzystanie z programu, a integracja z biblioteką matplotlib pozwala na czytelną wizualizację danych. Projekt został zrealizowany w sposób modułowy, z rozdzieleniem logiki, interfejsu i obsługi danych, co sprzyja jego dalszemu rozwojowi.