# Generated by Django 4.2.6 on 2024-08-10 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_card_cardproduct_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardproduct',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_products', to='project.card'),
        ),
    ]