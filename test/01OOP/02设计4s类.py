class CarStore(object):
    def order(self,car_type):
        return select_car_by_type(car_type)

def select_car_by_type(car_type):
     if car_type=="索纳塔":
        return Suonata()
     elif car_type=="名图":
        return Mingtu()


class Car(object):
    def move(self):
        print("车在移动......")
    def musice(self):
        print("车在播放音乐......")
    def stop(self):
        print("停车......")

class Suonata(Car):
    pass

class Mingtu(Car):
    pass

car_store=CarStore()
car=car_store.order("索纳塔")
car.move()
car.musice()
car.stop()