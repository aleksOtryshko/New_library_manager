import unittest
from unittest.mock import MagicMock
from application.library_app import LibraryApp
from domain.library import Library

class TestLibraryApp(unittest.TestCase):
    def setUp(self):
        self.library = MagicMock(spec=Library)
        self.app = LibraryApp(self.library)

    def test_run(self):
        self.app.run = MagicMock()
        self.app.run()
        self.app.run.assert_called_once()

if __name__ == "__main__":
    unittest.main()

