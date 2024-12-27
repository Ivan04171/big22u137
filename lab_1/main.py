import sys
import math

def get_coefficient(per):
    while True:
        try:
            value = float(input(per))
            return value
        except ValueError:
            print("Некорректное значение. Пожалуйста, введите число.")
def polozh(num1, num2):
    if num1 >= 0 and num2 >= 0:
        x1 = math.sqrt(num1)
        x2 = -math.sqrt(num1)
        x3 = math.sqrt(num2)
        x4 = -math.sqrt(num2)
        print(f"Уравнение имеет четыре действительных корня: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 ={x4}")
    elif num1 >= 0 and num2 < 0:
        x1 = math.sqrt(num1)
        x2 = -math.sqrt(num1)
        print(f"Уравнение имеет два действительных корня: x1 = {x1}, x2 = {x2}")
    elif num1 < 0 and num2 >= 0:
        x1 = math.sqrt(num2)
        x2 = -math.sqrt(num2)
        print(f"Уравнение имеет два действительных корня: x1 = {x1}, x2 = {x2}")
    else:
        print(f"Уравнение не имеет действительных корней")


def main():
    if len(sys.argv) == 4:
        try:
            A = float(sys.argv[1])
            B = float(sys.argv[2])
            C = float(sys.argv[3])
        except ValueError:
            print("Некорректные значения в параметрах командной строки. Вводите коэффициенты с клавиатуры.")
            A = get_coefficient("Введите коэффициент A: ")
            B = get_coefficient("Введите коэффициент B: ")
            C = get_coefficient("Введите коэффициент C: ")
    else:
        A = get_coefficient("Введите коэффициент A: ")
        B = get_coefficient("Введите коэффициент B: ")
        C = get_coefficient("Введите коэффициент C: ")

    if A == 0:
        print("Коэффициент A не может быть равен нулю для биквадратного уравнения.")
        return

    # Вычисляем дискриминант
    D = B**2 - 4*A*C

    # Анализируем дискриминант
    if D < 0:
        print("Уравнение не имеет действительных корней.")
    elif D == 0:
        x = -B / (2 * A)
        if x < 0:
            print(f"Уравнение не имеет действительных корней")
        else:
            x1 = math.sqrt(x)
            x2 = -math.sqrt(x)
            print(f"Уравнение имеет два действительных корня: x1 = {x1}, x2 = {x2}")
    else:
        x1 = (-B + D ** 0.5) / (2 * A)
        x2 = (-B - D ** 0.5) / (2 * A)
        polozh(x1, x2)

if __name__ == "__main__":
    main()