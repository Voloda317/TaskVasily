import json
import requests

BASE_URL = "http://127.0.0.1:8000"

def print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))

def get_all_books():
    response = requests.get(f'{BASE_URL}/books')
    response.raise_for_status()
    return response.json()

def add_book(book_data: dict):
    response = requests.post(f'{BASE_URL}/books', json=book_data)
    response.raise_for_status()
    return response.json()

def delete_book(book_id: int):
    response = requests.delete(f'{BASE_URL}/books/{book_id}')
    response.raise_for_status()
    return response.json()

def get_book_by_id(book_id: int):
    response = requests.get(f'{BASE_URL}/books/{book_id}')
    response.raise_for_status()
    return response.json()

def search_books(params: dict):
    """Поиск книг с фильтрами (query parameters)."""
    response = requests.get(f'{BASE_URL}/books/search', params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    book_one = {
        "book": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "year": 1866,
        "publication": "Русский вестник"
    }
    book_two = {
        "book": "Война и мир",
        "author": "Лев Толстой",
        "year": 1869,
        "publication": "Русский вестник"
    }
    book_three = {
        "book": "Анна Каренина",
        "author": "Лев Толстой",
        "year": 1877,
        "publication": "Русский вестник"
    }

    result_one = add_book(book_one)
    result_two = add_book(book_two)
    result_three = add_book(book_three)
    print('Добавили книги:')
    print_json(result_one)
    print_json(result_two)
    print_json(result_three)

    print('\nВсе книги после добавления:')
    all_books = get_all_books()
    print_json(all_books)


    print('\n=== Тестирование поиска ===')

    print('\n1. Поиск по автору "Лев Толстой":')
    found = search_books({"author": "Лев Толстой"})
    print_json(found)

    print('\n2. Поиск по названию "Преступление":')
    found = search_books({"book": "Преступление"})
    print_json(found)

    print('\n3. Поиск по году 1866:')
    found = search_books({"year": 1866})
    print_json(found)

    print('\n4. Поиск по издательству "Русский вестник":')
    found = search_books({"publisher": "Русский вестник"})
    print_json(found)

    print('\n5. Комбинированный поиск (author=Лев Толстой, year=1869):')
    found = search_books({"author": "Лев Толстой", "year": 1869})
    print_json(found)

    print('\n6. Поиск несуществующего автора:')
    found = search_books({"author": "Неизвестный автор"})
    print_json(found)  

    if all_books:
        book_id_to_delete = all_books[0]['id']  
        print(f'\nУдаляем книгу с id {book_id_to_delete}:')
        print_json(delete_book(book_id_to_delete))

        print('\nВсе книги после удаления:')
        print_json(get_all_books())
    else:
        print("Нет книг для удаления")
