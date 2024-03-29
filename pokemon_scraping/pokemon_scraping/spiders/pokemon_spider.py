import scrapy
from pokemon_scraping.items import PokemonItem


class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    head = "https://www.pokepedia.fr"
    start_urls = [
        "https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_de_la_premi%C3%A8re_g%C3%A9n%C3%A9ration",
        "https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_de_la_deuxi%C3%A8me_g%C3%A9n%C3%A9ration",
        "https://pokepedia.fr/Liste_des_Pok%C3%A9mon_de_la_troisi%C3%A8me_g%C3%A9n%C3%A9ration",
        "https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_de_la_quatri%C3%A8me_g%C3%A9n%C3%A9ration",
    ]

    def parse(self, response):
        for row in response.xpath("//table/tbody/tr"):
            numero = row.xpath("td[1]/text()").get()
            if numero and numero.isdigit():
                item = PokemonItem()
                try:
                    numero = int(numero)
                except ValueError:
                    print(f"Le numéro {numero} n'est pas un nombre valide.")
                item["numero"] = numero
                item["nom"] = row.xpath("td[3]/a/text()").get()
                # types = row.xpath("td[8]//img/@alt").getall()
                # print(types)
                # item["types"] = ", ".join(types)
                item["types"] = row.xpath("td[8]//img/@alt").getall()
                item["image_mini"] = self.head + row.xpath("td[2]//img/@src").get()
                item["lien"] = self.head + row.xpath("td[3]/a/@href").get()
                yield item
