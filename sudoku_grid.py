import turtle
import random


CELL = 40                  # اندازه هر خانه (پیکسل) 
N = 9
SIZE = CELL * N            

start_x = -SIZE/2
start_y = SIZE/2

screen = turtle.Screen()
screen.setup(width=SIZE + 100, height=SIZE + 100)
screen.title("9x9 Sudoku Grid")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)                 # بالاترین سرعت
screen.tracer(0, 0)        # غیرفعال کردن انیمیشن برای سرعت رسم

def draw_line(x1, y1, x2, y2, width=1):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.pensize(width)
    t.goto(x2, y2)
    t.penup()

# 1) خطوط نازک (هر خانه) width=1
for i in range(N + 1):
    x = start_x + i * CELL
    # عمودی
    draw_line(x, start_y, x, start_y - SIZE, width=1)
for j in range(N + 1):
    y = start_y - j * CELL
    # افقی
    draw_line(start_x, y, start_x + SIZE, y, width=1)

# 2) خطوط 3x3 (هر 3 خانه) width=3
for i in range(0, N + 1, 3):
    x = start_x + i * CELL
    draw_line(x, start_y, x, start_y - SIZE, width=3)
for j in range(0, N + 1, 3):
    y = start_y - j * CELL
    draw_line(start_x, y, start_x + SIZE, y, width=3)

# 3) حاشیه بیرونی width=5
draw_line(start_x, start_y, start_x + SIZE, start_y, width=5)            # بالا
draw_line(start_x, start_y - SIZE, start_x + SIZE, start_y - SIZE, width=5)  # پایین
draw_line(start_x, start_y, start_x, start_y - SIZE, width=5)            # چپ
draw_line(start_x + SIZE, start_y, start_x + SIZE, start_y - SIZE, width=5)  # راست

screen.update()
#turtle.done()

location = []
for row in range(9):
    for col in range(9):
        x = start_x + col * CELL + CELL/2
        y = start_y - row * CELL - CELL/2
        location.append((x, y))


board = [[0 for _ in range(9)] for _ in range(9)]

def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    # بررسی مربع 3×3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def fill_random_cells(board, count=38):
    filled = 0
    while filled < count:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] == 0:  
            num = random.randint(1, 9)
            if is_valid(board, row, col, num):
                board[row][col] = num
                draw_number(row, col, num)
                filled += 1
                
def draw_number(row, col, num):
    x = start_x + col * CELL + CELL / 2
    y = start_y - row * CELL - CELL / 2
    t.goto(x, y - 10) 
    t.write(str(num), align="center", font=("Arial", 14, "bold"))
        
fill_random_cells(board)
screen.update()
screen.mainloop()
