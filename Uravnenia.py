import tkinter
import math
import matplotlib.pyplot as plt
import numpy as np       

def plot_graph():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c

        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
        plt.axhline(0, color='black', linewidth=0.8)
        plt.axvline(0, color='black', linewidth=0.8)
        plt.title("График квадратного уравнения")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        result_label.config(text=f"Ошибка построения графика: {e}")

aken = tkinter.Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("800x250")
aken.configure(bg='white')
aken.resizable(width=False, height=False)
pealkiri = tkinter.Label(aken, text="Решение квадратного уравнения", font=("Futura", 20), bg='lightblue', fg='green')
pealkiri.pack(pady=20)
frame = tkinter.Frame(aken, bg='white')
frame.pack(pady=10)

entry_a = tkinter.Entry(frame, width=5, font=("Futura", 14), bg='lightblue')
entry_a.grid(row=0, column=0, padx=5)
label1 = tkinter.Label(frame, text="x**2 +", font=("Futura", 16), bg='white', fg='green')
label1.grid(row=0, column=1)

entry_b = tkinter.Entry(frame, width=5, font=("Futura", 14), bg='lightblue')
entry_b.grid(row=0, column=2, padx=5)
label2 = tkinter.Label(frame, text="x +", font=("Futura", 15), bg='white', fg='green')
label2.grid(row=0, column=3)

entry_c = tkinter.Entry(frame, width=5, font=("Futura", 14), bg='lightblue')
entry_c.grid(row=0, column=4, padx=5)
label3 = tkinter.Label(frame, text="= 0", font=("Futura", 16), bg='white', fg='green')
label3.grid(row=0, column=5)

nupp = tkinter.Button(frame, text="Решить", font=("Futura", 15), bg='green', fg='black', relief="ridge")
nupp.grid(row=0, column=6, padx=10)

graph_btn = tkinter.Button(frame, text="График", font=("Futura", 15), bg='green', fg='black', relief="ridge", command=plot_graph)
graph_btn.grid(row=0, column=10, pady=5, padx=10)

result_label = tkinter.Label(aken, text="Решение", font=("Futura", 14), bg='yellow', fg="black",width=60)
result_label.pack(pady=20)

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            result_label.config(text="Это не квадратное уравнение.")
            return

        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            result_label.config(text=f"Два различных корня: x1 = {x1}, x2 = {x2}")
        elif D == 0:
            x = -b / (2*a)
            result_label.config(text=f"Один корень: x = {x}")
        else:
            result_label.config(text="Нет действительных корней.")
    except ValueError:
        result_label.config(text="Введите корректные числа.")
nupp.config(command=solve_quadratic)

aken.mainloop()