from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np  # Пример использования внешнего пакета

if __name__ == "__main__":
    N = 5  # Пример номера варианта
    rectangle = Rectangle(N, N, "blue")
    circle = Circle(N, "green")
    square = Square(N, "red")

    print(rectangle)
    print(circle)
    print(square)

    # Пример использования numpy
    print(f"Numpy array: {np.array([1, 2, 3])}")
