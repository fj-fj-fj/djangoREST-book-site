# Generated by Django 3.1.4 on 2020-12-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Author null', max_length=255),
            preserve_default=False,
        ),
    ]
