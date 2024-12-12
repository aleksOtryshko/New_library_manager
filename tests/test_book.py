import unittest
from domain.book import Book

class TestBook(unittest.TestCase):
    def test_sanitize_input(self):
        self.assertEqual(Book._sanitize_input("  Hello, World!  "), "Hello, World!")
        with self.assertRaises(ValueError):
            Book._sanitize_input("")
        with self.assertRaises(ValueError):
            Book._sanitize_input("@#$%")

    def test_validate_year(self):
        Book.validate_year(2000)
        with self.assertRaises(ValueError):
            Book.validate_year(700)
        with self.assertRaises(ValueError):
            Book.validate_year(2025)

    def test_to_text(self):
        book = Book(1, "Title", "Author", 2000, "в наличии")
        self.assertEqual(book.to_text(), "1|Title|Author|2000|в наличии")

    def test_from_text(self):
        text = "1|Title|Author|2000|в наличии"
        book = Book.from_text(text)
        self.assertEqual(book.book_id, 1)
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.year, 2000)
        self.assertEqual(book.status, "в наличии")

if __name__ == "__main__":
    unittest.main()

