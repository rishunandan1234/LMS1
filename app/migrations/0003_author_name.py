# Generated by Django 4.2.6 on 2023-11-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_author_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]