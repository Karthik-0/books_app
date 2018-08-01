from .models import Book
from django.forms import ModelForm


class BookForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['pub_date'].widget.attrs.update(
            {'data-toggle': "datepicker",
             'class': 'form-control datepicker'})

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'totalpages', 'cover', 'desc', 'genre',
                  'publisher', 'pub_date', 'authors']
