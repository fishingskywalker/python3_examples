
# define a dictionary
classes = {'Barbarian':'Constitution & Strength',
           'Bard':'Charisma & Intelligence',
           'Cleric':'Wisdom & Charisma',
           'Druid':'Wisdom & Dexterity',
           'Fighter':'Strengh & Constitution',
           'Monk':'Dexterity & Wisdom',
           'Paladin':'Charisma & Strength',
           'Ranger':'Strength & Dexterity',
           'Rogue':'Dexterity & Charisma',
           'Sorceror':'Constitution & Intelligence',
           'Warlock':'Intelligence & Constitution',
           'Wizard':'Intelligence & Wisdom'}

# append a new class
classes['Beggar'] = 'Deception & Sleght of Hand'

print("The main & secondary stats for the classes are as follows:")
# print the values in the dictionary
for template in classes:
    print(classes[template])

# take the class name as input to search
search = input("Search for a class name: ")

# search the class in the dictionary
for template in classes:
    if template == search:
        print(classes[template])
        break

