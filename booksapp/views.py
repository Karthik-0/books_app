from django.views import generic
from .models import Book
from .filters import BookFilter
from django.urls import reverse_lazy


class BookList(generic.ListView):
    model = Book
    template_name = 'index.html'
    filterset_class = BookFilter
    context_object_name = 'books'
    # queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        books = Book.objects.all()
        tags = books.values_list('genre__name',flat=True).distinct()
        # tag = ", ".join(o.name for o in obj.tags.all()
        # print(tags)
        data = super().get_context_data(**kwargs)
        filter = BookFilter(self.request.GET, queryset=books)
        # print(filter.qs)
        data['filteredbooks'] = filter
        data['tags'] = tags
        # print(data['filteredbooks'])
        return data


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'single_book.html'
    context_object_name = 'book'


class BookAdd(generic.CreateView):
    model = Book
    fields = ['title', 'isbn', 'pagenos', 'cover', 'desc', 'genre',
              'publisher', 'pub_date', 'authors']
    template_name = 'add_book.html'
    context_object_name = 'fields'
    success_url = reverse_lazy('index')


class BookDelete(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('index')


class BookUpdate(generic.UpdateView):
    model = Book
    fields = ['title', 'isbn', 'pagenos', 'cover', 'desc', 'genre',
              'publisher', 'pub_date', 'authors']
    template_name = 'update_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('index')
