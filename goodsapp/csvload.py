import csv
from .models import Book
from dimensionsapp.models import Author, Serie, Jenre, Binding, FormatBook, AgeRestriction, PublishingHouse
from decimal import Decimal


def decode_utf8(input_iterator):
    for l in input_iterator:
        yield l.decode('utf-8')


def loadcsv(file):
    """
    Load books to catalog without any validation
    Create or update books, key values: authors and name
    :param file: uploaded file, which open as binary
    :return: None
    """
    reader = csv.DictReader(decode_utf8(file), delimiter=';')
    for row in reader:
        book_queryset=Book.objects.all()
        book_authors = []
        book_jenre = []
        for autor in row['authors'].split(','):
            a = autor.strip()
            m_author, created = Author.objects.get_or_create(name=a, defaults={'namePublic': a})
            book_queryset = book_queryset.filter(authors__name=a)
            book_authors.append(m_author)
        for jenre in row['jenre'].split(','):
            j = jenre.strip()
            m_jenre, created = Jenre.objects.get_or_create(name=j)
            book_jenre.append(m_jenre)
        book_serie, created = Serie.objects.get_or_create(name=row['serie'].strip())
        book_binding, created = Binding.objects.get_or_create(name=row['binding'].strip())
        book_formatbook, created = FormatBook.objects.get_or_create(name=row['format_book'].strip())
        book_agerestriction, created = AgeRestriction.objects.get_or_create(name=row['age_restrictions'].strip(),
                                                                            defaults={'order': 0})
        book_publisher, created = PublishingHouse.objects.get_or_create(name=row['publisher'].strip())
        book_isactive = row['is_active'].strip().lower() == 'true'
        book_name = row['name'].strip()
        book_price = Decimal(row['price'].strip().replace(',', '.'))
        book_yearpublishing = int(row['year_publishing'].strip())
        book_countpages = int(row['count_pages'].strip())
        book_isbn = row['isbn'].strip()
        book_weight = float(row['weight'].strip().replace(',', '.'))
        book_countbooks = int(row['count_books'].strip())
        book_rate = float(row['rate'].strip().replace(',', '.'))
        book, created = book_queryset.update_or_create(
            name=book_name,
            defaults={
                'price': book_price,
                'serie': book_serie,
                'year_publishing': book_yearpublishing,
                'count_pages': book_countpages,
                'binding': book_binding,
                'format_book': book_formatbook,
                'isbn': book_isbn,
                'weight': book_weight,
                'age_restrictions': book_agerestriction,
                'publisher': book_publisher,
                'count_books': book_countbooks,
                'is_active': book_isactive,
                'rate': book_rate,
            }
        )
        if not created:
            book.authors.clear()
            book.jenre.clear()
        book.authors.add(*book_authors)
        book.jenre.add(*book_jenre)

