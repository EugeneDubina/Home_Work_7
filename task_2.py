class Road:

    weight = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length  # длина в метрах
        self._width = width  # ширина в метрах

    def mass_calculation(self):
        print(
            f'Масса асфальта равна: '
            f'{int((self._length * self._width * self.weight * self.thickness) / 1000)} '
            f'т')


instance = Road(20, 5000)
instance.mass_calculation()