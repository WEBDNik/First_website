# Generated by Django 3.1.7 on 2021-03-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mynews',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
