# Generated by Django 3.0.5 on 2020-04-19 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_carditem_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CardItem',
            new_name='CartItem',
        ),
    ]
