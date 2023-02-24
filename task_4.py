class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.speed} км/ч')

    def go(self):
        print(f'{self.color} {self.name} движется')

    def stop(self):
        print(f'{self.name} остановился')

    def turn_left(self):
        print(f'{self.name} повернул налево')

    def turn_rigth(self):
        print(f'{self.name} повернул направо')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Превышение скорости! '
                  f'Снизьте скорость на {self.speed - 60} км/ч! ')
        else:
            print(f'Скорость автомобиля {self.name} {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Превышение скорости! '
                  f'Снизьте скорость на {self.speed - 40} км/ч! ')
        else:
            print(f'Скорость автомобиля {self.name}c{self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(67, 'серый', 'Hyundai Solaris', False)
car2 = SportCar(90, 'красный', 'Chevrolet Comaro', False)
car3 = WorkCar(50, 'белый', 'Skoda Octavia', False)
car4 = PoliceCar(80, 'серебристый', 'LADA Vesta', True)
car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()
car1.go()
car1.turn_rigth()
car4.turn_left()
car1.stop()