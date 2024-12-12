from domain.library import Library

class LibraryApp:
    """Приложение для управления библиотекой."""

    def __init__(self, library: Library):
        self.library = library

    def run(self) -> None:
        """Запуск приложения."""
        while True:
            self._display_menu()
            try:
                choice = input("Выберите действие: ").strip()
                if not choice:
                    raise ValueError("Ввод не может быть пустым.")
                match choice:
                    case "1":
                        title = input("Введите название книги: ").strip()
                        author = input("Введите автора книги: ").strip()
                        year = int(input("Введите год издания книги: ").strip())
                        self.library.add_book(title, author, year)
                    case "2":
                        book_id = int(input("Введите ID книги для удаления: ").strip())
                        self.library.remove_book(book_id)
                    case "3":
                        query = input("Введите поисковый запрос: ").strip()
                        self.library.search_books(query)
                    case "4":
                        self.library.display_books()
                    case "5":
                        book_id = int(input("Введите ID книги для изменения статуса: ").strip())
                        print("Выберите статус:\n1. в наличии\n2. выдана")
                        status_choice = input("Введите номер статуса: ").strip()
                        status = "в наличии" if status_choice == "1" else "выдана" if status_choice == "2" else None
                        if status:
                            self.library.change_status(book_id, status)
                        else:
                            print("Ошибка: Некорректный выбор статуса.")
                    case "6":
                        print("Выход.")
                        break
                    case _:
                        print("Ошибка: Некорректный выбор действия.")
            except ValueError :
                print(f"Ошибка: Год должен быть введен цифрами")

    def _display_menu(self) -> None:
        """Выводит меню."""
        common_menu = "\nМеню:\n1. Добавить книгу"
        if self.library.books:
            common_menu += "\n2. Удалить книгу\n3. Найти книгу\n4. Отобразить книги\n5. Изменить статус книги"
        common_menu += "\n6. Выход"
        print(common_menu)

