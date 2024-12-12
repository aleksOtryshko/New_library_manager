import unittest
from unittest.mock import MagicMock, patch
from domain.library import Library
from domain.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.repository = MagicMock()
        self.repository.load_books.return_value = []
        self.library = Library(self.repository)

    def test_add_book(self):
        self.repository.load_books.return_value = []  # Загружаем пустую библиотеку
        with patch.object(self.library, '_display_books', return_value=None):  # Замокировать _display_books
            self.library.add_book("Название", "Автор", 2000)  # Добавляем книгу
            self.repository.save_books.assert_called_once()  # Проверяем вызов save_books
            self.assertEqual(len(self.library.books), 1)  # Убедимся, что книга добавлена
            self.assertEqual(self.library.books[0].book_id, 1)  # Проверяем правильность ID книги

    def test_remove_book(self):
        book = Book(1, "Название", "Автор", 2000, "в наличии")
        self.repository.load_books.return_value = [book]
        self.library.books = self.repository.load_books()  # Обновляем состояние библиотеки
        with patch.object(self.library, '_display_books', return_value=None):
            self.library.remove_book(1)
            self.repository.save_books.assert_called_once()
            self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        book = Book(1, "Название", "Автор", 2000, "в наличии")
        self.repository.load_books.return_value = [book]
        with patch.object(self.library, '_display_books', return_value=None) as mock_display:
            self.library.search_books("Название")
            mock_display.assert_called_once()

    def test_display_books(self):
        book = Book(1, "Название", "Автор", 2000, "в наличии")
        self.repository.load_books.return_value = [book]
        self.library.books = self.repository.load_books()  # Обновляем состояние библиотеки
        with patch.object(self.library, '_display_books') as mock_display:
            self.library.display_books()
            mock_display.assert_called_once_with(self.library.books)

    def test_change_status(self):
        # Создаем книгу с подходящим ID
        existing_book = Book(1, "Название", "Автор", 2000, "в наличии")
        # Загружаем существующую книгу в библиотеку
        self.repository.load_books.return_value = [existing_book]
    
        # Обновляем состояние библиотеки на основе загруженных данных
        self.library.books = self.repository.load_books()

        # Замокируем `_display_books`, чтобы исключить его влияние на тест
        with patch.object(self.library, '_display_books', return_value=None):
            # Меняем статус книги с ID 1
            self.library.change_status(1, "выдана")
        
            # Проверяем, что `save_books` был вызван
            self.repository.save_books.assert_called_once()

            # Проверяем, что статус книги обновлен
            self.assertEqual(self.library.books[0].status, "выдана")

if __name__ == "__main__":
    unittest.main()
