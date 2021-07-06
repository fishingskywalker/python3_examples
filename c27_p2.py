# define the class
class Profession:
    name = "Spoony The Bard"
    # define the method
    def details(self):
        print("Hit Points: 1d8 per Bard level")
        print("Proficiencies: Light Armor, Simple Weapons, Musical Instrucments")
        print("Equipment: Rapier, Longsword, Simple Weapon")

# create the profession object
prof = Profession()
# print the class variable
print("Name:",prof.name)
# call the class method
prof.details()

