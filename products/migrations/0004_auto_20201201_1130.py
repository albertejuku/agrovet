# Generated by Django 3.1.1 on 2020-12-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201201_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/'),
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]
