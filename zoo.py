fName = './animals.csv'
aDataBase = open(fName, 'r', encoding='utf-8-sig')

print('Ez egy állatkert, amit ön a saját elképzelése szerint alakíthat!')
print('Állat hozzáadása - (1)  állat eltávolítása - (2)  kilépés - (0)')

zoo = []
aZoo = []
animals = {}
userInput = None


aDataBase.seek(0) #a mutató lenullázása.

for i in aDataBase.readlines():
    aDict = {}
    aDict['aName'] = i.strip()
    aZoo.append(aDict)


print('\nAz állatkert ezeket az állatokat keresi: ')
print('------------------------')
print()

for i in aZoo: #igényelt állatok kiíratása.
    print(i['aName'])
    
print('\n------------------------')

while userInput != '0':
    userInput = input('Mit szeretne tenni? ')
    
    if userInput == '1':  #Állatok hozzáadása az állatkerthez.
        name = input('Milyen állatot szeretne hozzáadni? ') 
            
        for i in aZoo: #'name' változó vizsgálása, hogy benne van-e az adatbázisba.
            if name == i['aName']:
                print('Az állatkert igényt tart erre az állatra.')
                        
                if name == i['aName']: 
                    
                    amount = int(input('Hány darabot kíván adni az állatkertnek? ')) #darabszám megadása
                
                    if amount > 0:
                        animals[name] += amount 
                        zoo.append(animals)
                    else:
                        print(f'Az állatkert sajnálatos módon nem tudja elfogadni azt a {name} nevű állatot, amelyből 0 darabot szeretne adni.')
                        print('------------------------')
                        
                    
                    
                
 
aDataBase.close()