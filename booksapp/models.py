from django.db import models
from taggit.managers import TaggableManager


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.IntegerField(verbose_name="ISBN")
    totalpages = models.IntegerField()
    cover = models.FileField(upload_to='image/', max_length=200)
    desc = models.TextField()
    genre = TaggableManager(related_name="books")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    pub_date = models.DateField()
    authors = models.ManyToManyField("Author")

    def __str__(self):
        return self.title
