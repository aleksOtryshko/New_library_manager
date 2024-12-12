from infrastructure.file_repository import FileRepository
from domain.library import Library
from application.library_app import LibraryApp

if __name__ == "__main__":
    repository = FileRepository("library.txt")
    library = Library(repository)
    app = LibraryApp(library)
    app.run()

