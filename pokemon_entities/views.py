import folium

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_active_pokemons(request):
    time_now = localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    active_entities = PokemonEntity.objects.filter(
                        disappeared_at__gte=time_now,
                        appeared_at__lte=time_now
                        )
    for pokemon_entity in active_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_ru,
            'title_jp': pokemon.title_jp,
            'title_en': pokemon.title_en,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    time_now = localtime()
    for pokemon_entity in requested_pokemon.entities.filter(
                        disappeared_at__gte=time_now,
                        appeared_at__lte=time_now
                                                            ):
        add_pokemon(
                    folium_map,
                    pokemon_entity.lat,
                    pokemon_entity.lon,
                    request.build_absolute_uri(requested_pokemon.image.url)
        )
    pokemon = {
               'pokemon_id': pokemon_id,
               'img_url': requested_pokemon.image.url,
               'title_ru': requested_pokemon.title_ru,
               'title_jp': requested_pokemon.title_jp,
               'title_en': requested_pokemon.title_en,
               'description': requested_pokemon.description,
    }
    if requested_pokemon.parent:
        pokemon['previous_evolution'] = {
                                'pokemon_id': requested_pokemon.parent.id,
                                'title_ru': requested_pokemon.parent.title_ru,
                                'img_url': requested_pokemon.parent.image.url,
                                }
    if descendant_pokemon := requested_pokemon.descendant.first():
        pokemon['next_evolution'] = {
                                'pokemon_id': descendant_pokemon.id,
                                'title_ru': descendant_pokemon.title_ru,
                                'img_url': descendant_pokemon.image.url,
                                }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
