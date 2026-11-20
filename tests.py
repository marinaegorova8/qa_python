import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'genre, expected_genre',
        [
            ('Фантастика', 'Фантастика'),
            ('Роман', ''),
        ]
    )
    def test_set_book_genre_valid_and_invalid_genre(self, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')

        collector.set_book_genre('Война и мир', genre)

        assert collector.get_book_genre('Война и мир') == expected_genre

    def test_get_book_genre_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')

        assert collector.get_book_genre('Война и мир') == ''

    def test_get_books_with_specific_genre_only_fantasy(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Сияние')
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Марсианин', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Властелин колец', 'Марсианин']

    def test_get_books_genre_with_added_book_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Каштановый человечек')
        collector.set_book_genre('Каштановый человечек', 'Детективы')

        assert collector.get_books_genre() == {'Каштановый человечек': 'Детективы'}

    def test_get_books_for_children_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гравити Фолз')
        collector.add_new_book('Игра Эндера')
        collector.add_new_book('Сияние')
        collector.add_new_book('Каштановый человечек')

        collector.set_book_genre('Гравити Фолз', 'Мультфильмы')
        collector.set_book_genre('Игра Эндера', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Каштановый человечек', 'Детективы')

        assert collector.get_books_for_children() == ['Гравити Фолз', 'Игра Эндера']

    @pytest.mark.parametrize(
        'book_to_add, expected_favorites',
        [
            ('Мастер и Маргарита', ['Мастер и Маргарита']),
            ('Гарри Поттер', []),
        ]
    )
    def test_add_book_in_favorites_only_existing(self, book_to_add, expected_favorites):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')

        collector.add_book_in_favorites(book_to_add)

        assert collector.get_list_of_favorites_books() == expected_favorites

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')

        collector.delete_book_from_favorites('Мастер и Маргарита')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_full_list(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита', 'Властелин колец']