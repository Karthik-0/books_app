from django.views import generic
from .models import Book, Author, Publisher
from .filters import BookFilter
from .forms import BookForm
from django.urls import reverse_lazy
from taggit.models import Tag


class BookList(generic.ListView):
    model = Book
    template_name = 'index.html'
    filterset_class = BookFilter
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        books = Book.objects.all()
        authors = Author.objects.all()
        tags = books.values_list('genre__name', flat=True).distinct()
        data = super().get_context_data(**kwargs)
        filter = BookFilter(self.request.GET, queryset=books)
        data['filteredbooks'] = filter
        data['tags'] = tags
        data['authors'] = authors
        data['publishers'] = Publisher.objects.distinct()
        print(data['publishers'])
        return data


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'single_book.html'
    context_object_name = 'book'


class BookAdd(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    context_object_name = 'fields'
    success_url = reverse_lazy('index')


class BookDelete(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('index')


class BookUpdate(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'update_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('index')


class GenreList(generic.ListView):
    model = Tag
    template_name = 'genre_list.html'
    context_object_name = 'genres'


class GenreEdit(generic.UpdateView):
    model = Tag
    template_name = 'edit_genre.html'
    fields = ['name']
    context_object_name = 'genre'
    success_url = reverse_lazy('genre')


class GenreDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('genre')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AuthorList(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class AuthorEdit(generic.UpdateView):
    model = Author
    template_name = 'edit_author.html'
    fields = ['name']
    context_object_name = 'author'
    success_url = reverse_lazy('author')


class AuthorDelete(generic.DeleteView):
    model = Author
    success_url = reverse_lazy('author')