
fName = './animals.csv'
aDataBase = open(fName, 'r', encoding='utf-8-sig')

print('Ez egy állatkert, amit ön a saját elképzelése szerint alakíthat!')
print('Állat hozzáadása - (1)  állat eltávolítása - (2)  kilépés - (0)')

zoo = []
aZoo = []
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

animals = {}

while userInput != '0':
    userInput = input('Mit szeretne tenni? ')
    
    if userInput == '1':  #Állatok hozzáadása az állatkerthez.
        name = input('Milyen állatot szeretne hozzáadni? ') 
        
        
        for i in aZoo: #'name' változó vizsgálása, hogy benne van-e az adatbázisba.
            if name == i['aName']:
                print('Az állatkert igényt tart erre az állatra.')
                
                while True:        
                    
                    if name == i['aName']: 
                        
                        amountStr = input('Hány darabot kíván adni az állatkertnek? ') #darabszám megadása
                        
                        try:
                            amount = int(amountStr)
                            
                            if amount > 0:
                                if name not in animals:
                                    animals[name] = amount     
                                    break
                                else:
                                    animals[name] += amount    
                                    break                      
                            else:
                                    print(f'Az állatkert sajnálatos módon nem tudja elfogadni azt a/az {name} nevű állatot, amelyből 0 darabot szeretne adni.')
                                    print('------------------------')   

                        except ValueError:
                            print('Ezt az értéket nem tudja felhasználni az állatkert! Kérlek számot adj meg.')
                            print()
                        
print(animals)
                    
                    
                
 
aDataBase.close()