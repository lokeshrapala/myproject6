# Generated by Django 4.0.1 on 2022-01-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
