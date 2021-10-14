import json
import requests

print('Profile Athena Generator - by fevers')

print('\nWhats your config name?')
iname = input('>> ')

print('\nDo you want to load either all or new cosmetics?\n(1): All\n(2): New')
ioption = input('>> ')

if ioption == '1':
    print('\nUser selected Generate All Cosmetics. Generating Profile_Athena now.')
if ioption == '2':
    print('\nUser selected Generate New Cosmetics. Generating Profile_Athena now.')


with open(f'profile_athena.json', 'w') as x:
        with open('empty.json') as f:
            ting = json.load(f)
        json.dump(ting, x, indent = 4)

a_file = open(f"profile_athena.json", "r")
json_object = json.load(a_file)
a_file.close()

if ioption == '1':
    response = requests.get('https://benbot.app/api/v1/cosmetics/br?lang=en')
else:
    response = requests.get('https://benbot.app/api/v1/newCosmetics?lang=en')

if ioption == '1': # All items
    for i in response.json():
        id = i['id']
        backendtype = i['backendType']
        id = f'{backendtype}:{id}'

        json_object['items'][id] = {
            'attributes': {
                "favorite": False,
                "item_seen": True,
                "level": 1,
                "max_level_bonus": 0,
                "rnd_sel_cnt": 0,
                "variants": [],
                "xp": 0
            },
            'templateId': f'{id}'
        }
        try:
            variants = True
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']
        except:
            variants = None

        if variants == True:
            print(i['id'])
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']

            json_object['items'][id]['attributes']['variants'] = [{
               "active": f"{active}",
               "channel": f"{channel}",
               "owned": []
            }]
            for i in i['variants'][0]['options']:
                tag = i['tag']
                json_object['items'][id]['attributes']['variants'][0]['owned'] = [
                    f"{tag}"
                ]
            

else: # New items
    for i in response.json()['items']:
        id = i['id']
        backendtype = i['backendType']
        id = f'{backendtype}:{id}'

        json_object['items'][id] = {
            'attributes': {
                "favorite": False,
                "item_seen": True,
                "level": 1,
                "max_level_bonus": 0,
                "rnd_sel_cnt": 0,
                "variants": [],
                "xp": 0
            },
            'templateId': f'{id}'
        }

a_file = open(f"profile_athena.json", "w")
json.dump(json_object, a_file, indent = 4)

print('\nGenerated!')