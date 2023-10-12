import random
class kotik:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.satiety=50
        self.alive=True

    def eat(self):
        print ("Time to eat")
        self.satiety+=2.5
        self.gladness+=3
    def sleep(self):
        print("I will sleep")
        self.gladness+=3
        self.satiety-=1.5
    def chill(self):
        print("Rest time")
        self.gladness+=5
        self.satiety-=1
    def is_alive(self):
        if self.satiety< -0.7:
            print("Cast out//")
            self.alive=False
        elif self.gladness<=0:
            print("Depresion")
            self.alive=False
        elif self.satiety>80:
            print("I ate too much...")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {round(self.satiety,2)}")
    def live(self,day):
        day="Day" +str(day)+ "of" + self.name +"life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.eat()
        elif live_cube==2:
            self.sleep()
        elif live_cube==3:
            self.chill()
        self.end_of_day()
        self.is_alive()
nick=kotik(name="Koshak")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)