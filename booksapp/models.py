from django.db import models
from taggit.managers import TaggableManager


class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.IntegerField()
    pagenos = models.IntegerField()
    cover = models.CharField(max_length=300)
    desc = models.TextField()
    genre = TaggableManager(related_name="tags")
    publisher = models.CharField(max_length=30)
    pub_date = models.DateField()
    authors = models.CharField(max_length=30)

    def __str__(self):
        return self.title
