# OxidoProject
Rozwiązanie zadania rekrutacyjnego na stanowisko Junior AI Developer.

## Opis projektu
Ten projekt to aplikacja służąca do generowania i modyfikowania kodu HTML na podstawie plików tekstowych oraz sugestii dotyczących formatowania treści. Aplikacja korzysta z OpenAI API w celu:
1. Generowania struktury HTML dla artykułu (funkcja `generate_initial_html`).
2. Proponowania miejsc na umieszczenie obrazków w wygenerowanym HTML (funkcja `suggest_image_placements`).
3. Modyfikacji kodu HTML w celu implementacji sugerowanych obrazków (funkcja `apply_suggestions`).

## Wymagania

1. **Python** w wersji 3.8 lub nowszej.
2. Zainstalowana biblioteka **openai**:
   ```bash
   pip install openai
3. Klucz do API OpenAI.

## Jak używać

1. Umieść plik tekstowy z artykułem w katalogu głównym projektu pod nazwą `artykulOxido.txt`.
2. Upewnij się, że zmienna `API_KEY` zawiera poprawny klucz API OpenAI.
3. Uruchom plik skryptu poleceniem:
     ```bash
     python script.py
     ```
4. Po zakończeniu działania skryptu wyniki zostaną zapisane w folderze `result`:
     - **`artykul_template.txt`**: HTML wygenerowany na podstawie tekstu artykułu.
     - **`sugestie.txt`**: Sugestie dotyczące miejsc dodania obrazków.
     - **`artykul.html`**: Ostateczny plik HTML z zaimplementowanymi obrazkami.

