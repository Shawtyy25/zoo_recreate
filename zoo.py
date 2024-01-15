import time
fName = './animals.csv'
aDataBase = open(fName, 'r+', encoding='utf-8-sig')

print('Ez egy állatkert, amit ön a saját elképzelése szerint alakíthat!')
print('Állat hozzáadása - (1)  állat eltávolítása - (2) lista megtekintése - (3)  kilépés - (0)')

aZoo2 = []
zoo = []
aZoo = []
userInput = None
found = False

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
    found = False    #found értékét mindig falsera állítja ha kilép a ciklusból!
    if userInput == '1':  #Állatok hozzáadása az állatkerthez.
        name = input('Milyen állatot szeretne hozzáadni? ') 
        
        for i in aZoo: #'name' változó vizsgálása, hogy benne van-e az adatbázisban.
            if name == i['aName']:
                print('Az állatkert igényt tart erre az állatra.')
                found = True

                while True:        
                
                    if name == i['aName']: 
                        amountStr = input('Hány darabot kíván adni az állatkertnek? ') #darabszám megadása
                        try:
                            amount = int(amountStr)
                            if amount > 0:
                                if name not in animals:
                                    animals[name] = amount     
                                    print(f'Az állatkert elfogadta az módosításodat! Így az állatkerti nyilvántartás a következő: ')
                                    print(animals)
                                    break
                                else:
                                    animals[name] += amount    
                                    print(f'Az állatkert elfogadta az módosításodat! Így az állatkerti nyilvántartás a következő: ')
                                    print(animals) 
                                    break    
                                
                                
                            else:
                                print(f'Az állatkert sajnálatos módon nem tudja elfogadni azt a/az {name} nevű állatot, amelyből 0 darabot szeretne adni.')
                                print('------------------------')   
                                
                        except ValueError:
                            print('------------------------')   
                            print('Ezt az értéket nem tudja felhasználni az állatkert! Kérlek számot adj meg.')
                            print()
                            
        if not found:
            print('------------------------')
            print('A megadott állat nem szerepel az állatkert igényei közt. ---> Állat hozzáadása az állatkert kereseti listájához - (1) / Kilépés - (0)')
            valueErrorAns = input('Mit szeretne tenni? ')

            if valueErrorAns == '1': #új állat hozzáadása a tömbhöz.
                print(f'A/az {name} nevű állat hozzáadása a listához...')  
                aDataBase.write(name + '\n')
                time.sleep(1)
                print('Állat hozzáadása sikeres.')
                aZoo.append({'aName': name})
                    
                #EZT MÉG FOLYTATNI KELL!!!           
            elif valueErrorAns == '0':
                print('------------------------')  
    
    if userInput == '3':
        print('------------------------')
        for i in aZoo: #hármas gomb lenyomással lekérdezzük a listát
            print(i['aName'])    
        print('------------------------')
                                 
print(animals)


                
 
aDataBase.close()
