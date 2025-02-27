# Generated by Django 3.1.14 on 2022-09-11 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20220911_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon'),
        ),
    ]
