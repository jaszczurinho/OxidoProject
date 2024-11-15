import openai
import os

API_KEY = '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'  # Wstaw swój klucz API tutaj
client = openai.Client(api_key=API_KEY)

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
# Funkcja generująca szablon HTML
def generate_initial_html(article_text):
    prompt = (
        "Przekształć poniższy artykuł w strukturę HTML dodając odpowiednie tagi jak <h2>, <p>. "
        "Zwróć tylko zawartość do umieszczenia pomiędzy tagami <body> i </body>. "
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który generuje HTML."},
            {"role": "user", "content": prompt + "\n\nArtykuł:\n" + article_text}
        ],
        max_tokens=2000,
        temperature=0
    )
    
    return response.choices[0].message.content.strip()

# Funkcja generująca sugestie miejsc do umieszczenia obrazków
def suggest_image_placements(html_content):
    prompt = (
        "Na podstawie poniższej struktury HTML, zasugeruj miejsca, w których warto dodać tagi <img>. "
        "Co myślisz o dodawaniu zdjęć jedynie po nagłówkami? "
        "Dodaj tagi <img> wewnątrz atrybutu <figure>."
        "Umieść w atrybucie alt opisy konkretnych przykłady obrazków, które będą promptami służącymi do generowania treści tych obrazków. Opisy twórz na podstawie nagłówka oraz odpowiadających mu paragrafów. "
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który proponuje treść obrazków, które mają zostać umieszczone w strukturze HTML. "},
            {"role": "user", "content": prompt + "\n\nHTML Content:\n" + html_content}
        ],
        max_tokens=2000,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# Funkcja aplikująca sugestie do szablonu 
def apply_suggestions(html_content):
    prompt = (
        "Na podstawie załączonego pliku tekstowego zawierającego seugestie co do umieszczania tagów <img> w kodzie HTML, zaimplementuj te sugestie zgodnie z poleceniami z pliku. Resztę struktury pozostaw bez zmian. "
        "Dodatkowo każdy tag dodany <img> ma mieć atrybut  src='image_placeholder.jpg'. Dodaj atrybut alt do kżdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki. Wybierz tylko jedną w proponowanych wartości atrybutu alt dla danego zdjęcia. "
        "Umieść podpisy pod grafikami używając odpowiedniego tagu HTML. "
        "Plik ma zawierać jedynie zmodyfikowaną strukturę HTML. "
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który implementuje sugesite co do umieszczenia tagów <img> w strukturze HTML"},
            {"role": "user", "content": prompt + "\n\nSugestie:\n" + html_content}
        ],
        max_tokens=2000,
        temperature=0
    )

    return response.choices[0].message.content.strip()

# Funkcja zapisująca wynikowy HTML do pliku
def save_to_file(content, output_file):
    # Tworzy folder 'result', jeśli nie istnieje
    os.makedirs('result', exist_ok=True)
    file_path = os.path.join('result', output_file)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Plik zapisano w: {file_path}")


def main():

    input_article_file = 'artykulOxido.txt'  
    html_template = 'artykul_template.txt'
    suggestions_file = 'sugestie.txt'
    final_file = 'artykul.html'

    article_text = read_article(input_article_file)
    
    initial_html_content = generate_initial_html(article_text)
    save_to_file(initial_html_content, html_template)

    suggested_html_content = suggest_image_placements(initial_html_content)
    save_to_file(suggested_html_content, suggestions_file)

    final_html_content = apply_suggestions(suggested_html_content)
    save_to_file(final_html_content, final_file)

if __name__ == "__main__":
    main()