import django_filters
from .models import Book, Author, Publisher


def publishers(request):
    print(request)
    # company = request
    print(Publisher.objects.all())
    return Publisher.objects.all()


class BookFilter(django_filters.FilterSet):
    authors = django_filters.filters.ModelMultipleChoiceFilter(
        field_name='authors__name',
        to_field_name='name',
        queryset=Author.objects.all(),
    )
    publisher = django_filters.filters.ModelChoiceFilter(
        queryset=Publisher.objects.all(),
        to_field_name='name'
    )

    class Meta:
        model = Book
        fields = ['authors', 'publisher', 'genre__name']
