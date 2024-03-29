# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonItem(scrapy.Item):
    numero = scrapy.Field()
    nom = scrapy.Field()
    types = scrapy.Field()
    lien = scrapy.Field()
    image_mini = scrapy.Field()
    image = scrapy.Field()
    stats = scrapy.Field()
    evolutions = scrapy.Field()
    sensibilities = scrapy.Field()
    attaques = scrapy.Field()
