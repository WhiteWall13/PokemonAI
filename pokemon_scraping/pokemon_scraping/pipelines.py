# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

# import json
# import os

# from scrapy.exporters import JsonItemExporter
# import psycopg2
# from scrapy.exceptions import DropItem


# # Définition de la pipeline pour le traitement des données par Scrapy
# class PokemonScrapingPipeline:  # Quand la spider est ouverte
#     def open_spider(self, spider):
#         # Création du répertoire des données
#         os.makedirs("../data", exist_ok=True)
#         # Ouvre ou créé le pokemons.json qui devra contenir les données de scrapy des pokemons
#         try:
#             self.file = open("../data/pokemons.json", "rb+")
#         except FileNotFoundError:
#             self.file = open("../data/pokemons.json", "w+b")
#         try:
#             self.data = json.load(self.file)
#         except json.JSONDecodeError:
#             self.data = []
#         # Réinitialisation du curseur
#         self.file.seek(0)

#     # Quand la spider est fermée
#     def close_spider(self, spider):
#         # Création d'un exportateur d'objects en JSON
#         exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
#         exporter.start_exporting()
#         # Exportation de chaque objects
#         for item in self.data:
#             exporter.export_item(item)
#         exporter.finish_exporting()
#         # Troncature du fichier pour retirer les données en trop
#         self.file.truncate()
#         self.file.close()

#     # Traitement de chaque object récupéré par la spider
#     def process_item(self, item, spider):
#         # Vérifi si l'object existe puis il est mit à jour
#         for existing_item in self.data:
#             if existing_item["numero"] == item["numero"]:
#                 existing_item.update(item)
#                 break
#         else:
#             # Si l'object n'existe pas on le crée
#             self.data.append(item)
#         return item

# Importation des modules nécessaires
import json
import os
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter


class PokemonPipeline:
    # Quand la spider est ouverte
    def open_spider(self, spider):
        # Création du répertoire des données
        os.makedirs("../data", exist_ok=True)
        # Ouvre ou créé le pokemons.json qui devra contenir les données de scrapy des pokemons
        try:
            self.file = open("../data/pokemons.json", "rb+")
        except FileNotFoundError:
            self.file = open("../data/pokemons.json", "w+b")
        try:
            self.data = json.load(self.file)
        except json.JSONDecodeError:
            self.data = []
        # Réinitialisation du curseur
        self.file.seek(0)

    # Quand la spider est fermée
    def close_spider(self, spider):
        # Création d'un exportateur d'objects en JSON
        exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        exporter.start_exporting()
        # Exportation de chaque objects
        for item in self.data:
            exporter.export_item(item)
        exporter.finish_exporting()
        # Troncature du fichier pour retirer les données en trop
        self.file.truncate()
        self.file.close()

    # Traitement de chaque object récupéré par la spider
    def process_item(self, item, spider):
        # Vérifi si l'object existe puis il est mit à jour
        for existing_item in self.data:
            if existing_item["numero"] == item["numero"]:
                existing_item.update(item)
                break
        else:
            # Si l'object n'existe pas on le crée
            self.data.append(item)
        return item
