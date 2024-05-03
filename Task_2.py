import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def snowflake_koch(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def draw_snowflake_koch(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    
    snowflake_koch(t, order, size)

    window.mainloop()

def get_recursion_level():
    while True:
        try:
            recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха (ціле число): "))
            if recursion_level < 0:
                print("Будь ласка, введіть не від'ємне число.")
            else:
                return recursion_level
        except ValueError:
            print("Будь ласка, введіть ціле число.")

recursion_level = get_recursion_level()
draw_snowflake_koch(recursion_level)