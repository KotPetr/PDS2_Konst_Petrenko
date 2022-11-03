
class Car:

    def __init__(self, car_name : str, car_color : str, car_motor_volume : float):
        self.name = car_name
        self.color = car_color
        self.motor_volume = car_motor_volume

    def moove_forward(self):
        print(f'{self.color.capitalize()} {self.name} is mooving forward!')

    def moove_backward(self):
        print(f'{self.color.capitalize()} {self.name} is mooving backward!')


class TurningCar(Car):

    def turn_right(self):
        print(f'{self.color.capitalize()} {self.name} is turning right!')

    def turn_left(self):
        print(f'{self.color.capitalize()} {self.name} is turning left!')

car1 = Car('honda', 'red', 1.8)
car2 = Car('audi', 'white', 2.2)

car1.moove_forward()
car2.moove_backward()

car3 = TurningCar('toyota', 'black', 1.6)

car3.moove_forward()
car3.turn_left()
