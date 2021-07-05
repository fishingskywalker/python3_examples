# define a list of fruit
fruit = ['Apple','Banana','Orange']
def SelectedFruit(fruit):
    selected = ['Apple','Cherry','Orange']
    if(fruit in selected):
        return True
selectionList = filter(SelectedFruit, fruit)
print('The selected fruit is:')
for produce in selectionList:
    print(produce)

