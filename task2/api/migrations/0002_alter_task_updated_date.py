# Generated by Django 4.1.10 on 2023-08-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]