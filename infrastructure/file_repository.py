from typing import List
from domain.book import Book
from domain.library import LibraryRepository

class FileRepository(LibraryRepository):
    """Класс для работы с файловым хранилищем книг."""

    def __init__(self, storage_file: str):
        self.storage_file = storage_file

    def load_books(self) -> List[Book]:
        """Загружает книги из файла."""
        try:
            with open(self.storage_file, "r") as file:
                return [Book.from_text(line) for line in file if line.strip()]
        except FileNotFoundError:
            return []

    def save_books(self, books: List[Book]) -> None:
        """Сохраняет книги в файл."""
        with open(self.storage_file, "w") as file:
            for book in books:
                file.write(book.to_text() + "\n")

