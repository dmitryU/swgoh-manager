#!/usr/bin/env python3
import requests
import json
import lxml.html
import cssselect
from .models import *


def update_character_database():
    # загрузить базу данных персонажей
    response = requests.get('https://swgoh.gg/api/characters')
    json_data = response.json()
    for idx, c in enumerate(json_data):
        found = Character.objects.filter(base_id=c['base_id'])
        if len(found) == 0:
            character = Character(base_id=c['base_id'], name=c['name'], power=c['power'], description=c['description'], url=c['url'], image=c['image'], combat_type=c['combat_type'])
        else:
            character = found[0]
            character.name = c['name']
            character.power = c['power']
            character.description = c['description']
            character.url = c['url']
            character.image = c['image']
            character.combat_type = c['combat_type']
        character.save()
    # загрузить базу данных кораблей
    response = requests.get('https://swgoh.gg/api/ships')
    json_data = response.json()
    for c in json_data:
        found = Character.objects.filter(base_id=c['base_id'])
        if len(found) == 0:
            character = Character(base_id=c['base_id'], name=c['name'], power=c['power'], description=c['description'], url=c['url'], image=c['image'], combat_type=c['combat_type'])
        else:
            character = found[0]
            character.name = c['name']
            character.power = c['power']
            character.description = c['description']
            character.url = c['url']
            character.image = c['image']
            character.combat_type = c['combat_type']
        character.save()


#response = requests.get('https://swgoh.gg/api/guilds/34508/units')
#json_data = response.json()
#with open('units.json','w+') as file:
#    json.dump(json_data, file)

def update_units(guild):
    # запрос в свгох
    print("Загрузка данных по складам гильдии %s" % guild)
    response = requests.get("https://swgoh.gg/api/guilds/%d/units" % guild.guild_id)
    json_data = response.json()
    # подготовка игроков для поиска и сопоставления
    players = Player.objects.filter(guild=guild)
    print("Загрузка данных завершена, начинаю сопоставление")
    units_added = 0
    units_updated = 0
    # разбор полученных данных
    for base_id, units in json_data.items():
        # найти персонажа
        characters = Character.objects.filter(base_id=base_id)
        if len(characters) == 0:
            print("Персонаж %s не найден!" % base_id)
            continue
        # перебрать всех юниты этого персонажа
        for u in units:
            # найти игрока
            player = None
            for p in players:
                if p.player_name == u['player']:
                    player = p
                    break
            if player == None:
                print("Не найден игрок %s!" % u['player'])
                continue
            # поискать юнит
            found = Unit.objects.filter(character=characters[0], player=player)
            if found:
                unit = found[0]
                unit.gear_level = u.get('gear_level', '0')
                unit.power = u['power']
                unit.level = u['level']
                unit.rarity=u['rarity']
                units_added = units_added + 1
            else:
                unit = Unit(character=characters[0], player=player, gear_level=u.get('gear_level', '0'),
                    power=u['power'], level=u['level'], rarity=u['rarity'])
                units_updated = units_updated + 1
            unit.save()
    print("Обновление данных по складам гильдии %s завершено. Юнитов добавлено %d, обновлено %d" % (guild, units_added, units_updated))



def update_guild(guild):
    # запрос в свгох
    print("Загрузка данных по игрокам гильдии %s" % guild)
    response = requests.get("https://swgoh.gg/g/%d/%s/" % (guild.guild_id, guild.name))
    root = lxml.html.fromstring(response.text)
    players = root.cssselect('.character-list table tbody tr td:first-child')
    players_added = 0
    players_updated = 0
    # добавить или обновить игроков из ги
    print("В гильдии %s опубликовано игроков %d" % (guild, len(players)))
    for p in players:
        name = p.attrib['data-sort-value']
        login = p[0].attrib['href'][3:-1]
        found = Player.objects.filter(swgoh_name=login)
        if len(found) == 0:
                player = Player(player_name=name, swgoh_name=login, guild=guild, active=True)
                players_added = players_added + 1
        else:
                player = found[0]
                player.player_name = name
                player.active = True
                player.guild = guild # он мог быть в другой ги
                players_updated = players_updated + 1
    print("Обновление данных игроков гильдии %s завершено. Игроков добавлено %d, обновлено %d" % (guild, players_added, players_updated))
    # убрать игроков которые уже не в ги
    for player in Player.objects.filter(guild=guild):
        found = False
        for p in players:
            if p[0].attrib['href'][3:-1] == player.swgoh_name:
                found = True
                break
        if not found:
            player.active = False
            player.save()


def update_guilds():
    # Обновить данные по всем гильдиям
    for guild in Guild.objects.all():
        if guild.active:
            update_guild(guild)