# Generated by Django 2.0.7 on 2018-07-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('isbn', models.IntegerField()),
                ('pagenos', models.IntegerField()),
                ('cover', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('genre', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=30)),
                ('pub_date', models.DateField()),
                ('authors', models.CharField(max_length=30)),
            ],
        ),
    ]
