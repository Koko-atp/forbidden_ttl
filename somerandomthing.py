class damn :
    name : None
    age : None
    job : None
    hunger : int
    class food :
        burger : int
        food : int
        water : int
        def __init__(self):
            bruger = self.burger = 0    
            food = self.food = 0    
            water = self.water = 0    
            pass

        
    def __init__(self) :
        name = self. name = 'Unknow'
        age = self. age = 'Unknow'
        job = self.job = 'Unknow'
        hunger = self.hunger = 100
    def show(self):
        print(f'name : {self.name} \n age : {self.age} \n job : {self.job} \n Hunger : {self.hunger}%')

    # def eat(self):
    #     self.food.burger

    #     print()
    #     food = int(input('what to eat?'))
               
    #     print(f'you now aat a {food}')

    #     self.hunger += 50
    
    def menu(self) :
        self.show()

        
start = damn()
# start.menu()
  ######################################################## inventory test

inventory = dict({
    'burger' : 0 ,
    'food' : 0 ,
    'water' : 0 ,
})

t = str(input('::::'))
for i in inventory :
    if t == i :
        inventory[i] += 1
    print(f'{i} : {inventory[i]}')