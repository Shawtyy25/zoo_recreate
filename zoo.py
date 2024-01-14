fName = './animals.csv'
aDataBase = open(fName, 'r', encoding='utf-8-sig')

print('Ez egy állatkert, amit ön a saját elképzelése szerint alakíthat!')
print('Állat hozzáadása - (1)  állat eltávolítása - (2)  kilépés - (0)')

zoo = []
animals = {}
userInput = None
aDict = {}



print('\nAz állatkert ezeket az állatokat keresi: ')
animalList = aDataBase.readlines()
print(''.join(animalList))

for i in animalList:
    aDict['animalname'] = i.strip()
    

while userInput != '0':
    userInput = input('Mit szeretne tenni? ')
    
    if userInput == '1':  #Állatok hozzáadása az állatkerthez
        name = input('Milyen állatot szeretne hozzáadni? ') 
        
        
    

            
aDataBase.close()