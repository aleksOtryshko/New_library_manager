from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Book:
    """Класс, представляющий книгу."""
    book_id: int
    title: str
    author: str
    year: int
    status: str

    ALLOWED_CHARS: ClassVar[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789 .,!?-"

    def __post_init__(self):
        self.title = self._sanitize_input(self.title)
        self.author = self._sanitize_input(self.author)
        self.validate_year(self.year)

    @staticmethod
    def _sanitize_input(input_string: str) -> str:
        """Удаляет спецсимволы и проверяет пустой ввод."""
        input_string = input_string.strip()
        sanitized = ''.join(char for char in input_string if char in Book.ALLOWED_CHARS)
        if not sanitized:
            raise ValueError("Пустые значения и спец символы вводить нельзя.")
        return sanitized

    @staticmethod
    def validate_year(year: int) -> None:
        """Проверяет корректность года издания."""
        if not (868 <= year <= 2024):
            raise ValueError("Год издания должен быть в диапазоне от 868 до 2024.")

    def to_text(self) -> str:
        """Преобразует книгу в строку для записи в файл."""
        return f"{self.book_id}|{self.title}|{self.author}|{self.year}|{self.status}"

    @staticmethod
    def from_text(text: str) -> 'Book':
        """Создает объект книги из строки."""
        parts = text.strip().split("|")
        if len(parts) != 5:
            raise ValueError("Неверный формат данных в файле.")
        return Book(int(parts[0]), parts[1], parts[2], int(parts[3]), parts[4])

