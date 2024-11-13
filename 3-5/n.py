import json

users_filename, updates_filename = input(), input()

with open(users_filename, encoding='UTF-8') as users_file, open(updates_filename, encoding='UTF-8') as updates_file:
    users, updates = json.load(users_file), json.load(updates_file)

updated_data = {}

for user in users:
    name = user.pop('name')
    updated_data[name] = user

for user in updates:
    name = user.pop('name')
    for key in user.keys():
        if user[key] > updated_data[name].get(key, ''):
            updated_data[name][key] = user[key]

with open(users_filename, 'w', encoding='UTF-8') as users_file:
    json.dump(updated_data, users_file, sort_keys=False, indent=4, ensure_ascii=False)
