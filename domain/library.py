from typing import List, Optional
from .book import Book
from abc import ABC, abstractmethod

class LibraryRepository(ABC):
    """Абстрактный класс для работы с хранилищем книг."""

    @abstractmethod
    def load_books(self) -> List[Book]:
        pass

    @abstractmethod
    def save_books(self, books: List[Book]) -> None:
        pass

class Library:
    """Класс, управляющий библиотекой."""

    def __init__(self, repository: LibraryRepository):
        self.repository = repository
        self.books = self.repository.load_books()

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет новую книгу."""
        try:
            Book.validate_year(year)
            book_id = max([book.book_id for book in self.books], default=0) + 1
            new_book = Book(book_id, title, author, year, "в наличии")
            self.books.append(new_book)
            self.repository.save_books(self.books)
            print("Книга успешно добавлена.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу по ID."""
        book = self._find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.repository.save_books(self.books)
            print("Книга успешно удалена.")
        else:
            print("Ошибка: Книга с таким ID не найдена.")

    def _find_book_by_id(self, book_id: int) -> Optional[Book]:
        """Находит книгу по ID."""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def search_books(self, query: str) -> None:
        """Ищет книги по названию или автору."""
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        self._display_books(results)

    def display_books(self) -> None:
        """Выводит все книги."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            self._display_books(self.books)

    def _display_books(self, books: List[Book]) -> None:
        """Выводит список книг."""
        for book in books:
            print(f"ID: {book.book_id} | Название: {book.title} | Автор: {book.author} | Год: {book.year} | Статус: {book.status}")

    def change_status(self, book_id: int, status: str) -> None:
        """Изменяет статус книги."""
        if status not in ["в наличии", "выдана"]:
            print("Ошибка: Некорректный статус.")
            return
        book = self._find_book_by_id(book_id)
        if book:
            book.status = status
            self.repository.save_books(self.books)
            print("Статус книги успешно изменен.")
        else:
            print("Ошибка: Книга с таким ID не найдена.")

