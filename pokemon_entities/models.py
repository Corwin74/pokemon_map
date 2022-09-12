from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField('имя', max_length=200)
    title_jp = models.CharField(
                                'имя (яп.)',
                                max_length=200,
                                blank=True,
    )
    title_en = models.CharField(
                                'имя (англ.)',
                                max_length=200,
                                blank=True,
    )
    image = models.ImageField(
                              'изображение',
                              null=True,
                              blank=True,
    )
    description = models.TextField(
                                   'описание',
                                   blank=True,
    )
    parent = models.ForeignKey(
                               'self',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               verbose_name='Из кого эволюционировал',
                               related_name='descendant',
    )

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
                                Pokemon,
                                on_delete=models.CASCADE,
                                related_name='entities',
                                verbose_name='вид покемона',
    )
    lat = models.DecimalField(
                              'широта',
                              max_digits=10,
                              decimal_places=7,
    )
    lon = models.DecimalField(
                              'долгота',
                              max_digits=10,
                              decimal_places=7,
    )
    appeared_at = models.DateTimeField('время появления')
    disappeared_at = models.DateTimeField('время исчезновения')
    level = models.PositiveSmallIntegerField(
                                             'уровень',
                                             blank=True,
                                             null=True,
    )
    health = models.PositiveSmallIntegerField(
                                             'здоровье',
                                             blank=True,
                                             null=True,
    )
    strength = models.PositiveSmallIntegerField(
                                             'сила',
                                             blank=True,
                                             null=True
    )
    defence = models.PositiveSmallIntegerField(
                                            'защита',
                                            blank=True,
                                            null=True,
    )
    stamina = models.PositiveSmallIntegerField(
                                             'выносливость',
                                             blank=True,
                                             null=True,
    )

    def __str__(self):
        return f'{self.pokemon} ({self.level})'

    class Meta:
        verbose_name = 'Место появления'
        verbose_name_plural = 'Места появления'
