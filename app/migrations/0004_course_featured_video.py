# Generated by Django 4.2.6 on 2023-11-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='featured_video',
            field=models.CharField(max_length=300, null=True),
        ),
    ]