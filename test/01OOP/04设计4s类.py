class Store(object):
    def select_car(self,car_type):
        pass
    def order(self,car_type):
        return self.select_car(car_type)

class BMWCarStore(Store):
    def select_car(self,car_type): #父类定义了个空方法，实例会优先调用子类的方法
        return BMWFactory().select_car_by_type(car_type)
        
class BMWFactory(object):
    def select_car_by_type(self,car_type):
        pass


bmw_store=BMWCarStore()
bmw=bmw_store.order("720li")


class CarStore(Store):
    def select_car(self,car_type):
        return Factory().select_car_by_type(car_type)

   



class Factory(object):
    def select_car_by_type(self,car_type):
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