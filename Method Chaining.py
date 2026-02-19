class Car:
    def turn_on(self):
        print()
        return self

    def drive(self):
        print()
        return self

    def brake(self):
        print()
        return self

    def turn_off(self):
        print()
        return self

car = Car()

car.turn_on().drive()
car.brake().turn_off()

car.turn_on().drive().brake().turn_off()