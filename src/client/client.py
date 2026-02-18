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

    result_one = add_book(book_one)
    result_two = add_book(book_two)
    print('Добавили книги:')
    print_json(result_one)
    print_json(result_two)

    print('Все книги после добавления:')
    print_json(get_all_books())

    # Удаляем книгу с id 8 (измените число, если нужно удалить другую)
    print('Удаляем книгу с id 8:')
    print_json(delete_book(8))

    print('Все книги после удаления:')
    print_json(get_all_books())

    # Получаем книгу с id 13 и выводим результат
    test_result_book_get_id = get_book_by_id(13)
    print('Книга с id 13:')
    print_json(test_result_book_get_id)