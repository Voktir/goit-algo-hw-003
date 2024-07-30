import turtle

def koch_curve(t:turtle.Turtle, order: int, size: int):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order: int, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.left(-120)

    window.mainloop()

def main():
    while True:
        try:
            order = int(input("Введіть число для кривої Коха: "))
            if order <= 0:
                print("Рівень рекурсії повинен бути додатнім.")
            else:
                break
        except ValueError:
            print("Будь ласка, введіть число.")

    draw_koch_curve(order)

if __name__ == "__main__":
    main()