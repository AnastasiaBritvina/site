# Generated by Django 3.1.4 on 2021-06-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_application_newinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='newInfo',
            field=models.TextField(blank=True),
        ),
    ]
