from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    description = models.TextField(
                                   verbose_name='описание'
    )
    parent = models.ForeignKey(
                               'self', 
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               verbose_name='Из кого эволюционировал',
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
                                Pokemon,
                                on_delete=models.CASCADE,
                                )
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lon = models.DecimalField(max_digits=10, decimal_places=7)
    appeared_at = models.DateTimeField(
    )
    disappeared_at = models.DateTimeField(
    )
    level = models.PositiveSmallIntegerField(
                                             blank=True,
                                             null=True
    )
    health = models.PositiveSmallIntegerField(
                                             blank=True,
                                             null=True
    )
    strength = models.PositiveSmallIntegerField(
                                             blank=True,
                                             null=True
    )
    defence = models.PositiveSmallIntegerField(
                                             blank=True,
                                             null=True
    )
    stamina = models.PositiveSmallIntegerField(
                                             blank=True,
                                             null=True
    )
