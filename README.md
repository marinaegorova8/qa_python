# qa_python

## Список реализованных тестов:

1. `test_add_new_book_add_two_books` - добавление двух новых книг в коллекцию.
2. `test_add_new_book_duplicate_not_added` - повторное добавление уже существующей книги не создает дубликат.
3. `test_set_book_genre_valid_and_invalid_genre` - параметризованная проверка установки допустимого и несуществующего жанра для книги.
4. `test_get_book_genre_empty_genre` - у только что добавленной книги жанр не задан (возвращается пустая строка).
5. `test_get_books_with_specific_genre_only_fantasy` - получение списка книг с определенным жанром.
6. `test_get_books_genre_with_added_book_and_genre` - получение словаря с добавленной книгой и ее жанром.
7. `test_get_books_for_children_without_age_rating` - фильтрация книг для детей (книги с возрастным рейтингом не попадают в список).
8. `test_add_book_in_favorites_only_existing` - параметризованная проверка добавления в избранное существующей в коллекции книги и игнорирования отсутствующей.
9. `test_delete_book_from_favorites_success` - удаление книги из списка избранного.
10. `test_get_list_of_favorites_books_full_list` - получение актуального списка избранных книг.