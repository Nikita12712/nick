import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):

        return self.width * self.height

    def __eq__(self, other):

        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):

        if isinstance(other, Rectangle):
            total_area = self.get_square() + other.get_square()

            side = math.sqrt(total_area)
            return Rectangle(side, side)
        raise ValueError("Можна додавати тільки об'єкти типу Rectangle")

    def __mul__(self, n):

        if isinstance(n, (int, float)) and n > 0:
            new_area = self.get_square() * n
            side = math.sqrt(new_area)
            return Rectangle(side, side)
        raise ValueError("Множення можливе тільки на позитивні числа")

    def __str__(self):

        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

# Перевіряємо площу
assert r1.get_square() == 8
assert r2.get_square() == 18


r3 = r1 + r2
assert r3.get_square() == 26


r4 = r1 * 4
assert r4.get_square() == 32


assert Rectangle(3, 6) == Rectangle(2, 9)


print(r1)
print(r2)
print(r3)
print(r4)
