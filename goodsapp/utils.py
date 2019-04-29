from goodsapp.models import Book
from dimensionsapp.models import *


def author_book(author):
    if type(author) == str:
        author = Author.objects.get(name=author)
    return author.book_set.all()


def print_author_book(author):
    for book in author_book(author):
        print(book.description())


class ObjUtil:
    def __init__(self, model_class):
        self.model_class = model_class

    def create(self, data):
        aut = self.model_class(**data)
        # if 'description' in data.keys():
        #     aut.description = data['description']
        aut.save()

    def bulk_create(self, count, default_name):
        list_ = [self.model_class(name=default_name + str(i)) for i in range(1, count + 1)]
        self.model_class.objects.bulk_create(list_)

    def count(self, name=None):
        if name is None:
            return self.model_class.objects.count()
        return self.model_class.objects.filter(name__startswith=name).count()

    def delete(self, id_key):
        try:
            if type(id_key) == int:
                aut = self.model_class.objects.get(id=id_key)
            else:
                aut = self.model_class.objects.get(name=id_key)
            aut.delete()
        except self.model_class.DoesNotExist:
            print(id_key, 'doesn\'t find')

    def update(self, data):
        di = data.copy()
        name = di.pop("name")
        return self.model_class.objects.update_or_create(name=name, defaults=di)

    def get_or_create(self, data):
        di = data.copy()
        name = di.pop("name")
        return self.model_class.objects.get_or_create(name=name, defaults=di)


def create_book(book_dict):
    book = Book(name=book_dict['name'],
                price=book_dict['price'],
                year_publishing=book_dict['year_publishing'],
                count_pages=book_dict['count_pages'],
                isbn=book_dict['isbn'],
                weight=book_dict['weight'],
                count_books=book_dict['count_books'],
                is_active=book_dict['is_active'],
                rate=book_dict['rate'])
    serie_obj, created = ObjUtil(Serie).update(book_dict['serie'])
    book.serie = serie_obj
    binding_obj, created = ObjUtil(Binding).get_or_create(book_dict['binding'])
    book.binding = binding_obj
    book.format_book = ObjUtil(FormatBook).get_or_create(book_dict['format_book'])[0]
    book.age_restrictions = ObjUtil(AgeRestriction).get_or_create(
        book_dict['age_restrictions'])[0]
    book.publisher = ObjUtil(PublishingHouse).get_or_create(
        book_dict['publisher'])[0]
    book.save()
    aut_gen = ObjUtil(Author)
    for author in book_dict['authors']:
        aut_obj, created = aut_gen.get_or_create(author)
        book.authors.add(aut_obj)
    jen_gen = ObjUtil(Jenre)
    for jenre in book_dict['jenre']:
        jen_obj, created = jen_gen.update(jenre)
        book.jenre.add(jen_obj)
