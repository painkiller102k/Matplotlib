import tkinter

k=0
def vajutatud(): # левая кнопка мыши +
    global k
    k+=1
    pealkiri.config(text=f"Sa vajutasid nuppu {k} korda")
    nupp.config(text="Vajuta mind uuesti", fg='black')

def vajutatudPK(event): # правой кнопкой мыши -
    global k
    k-=1
    pealkiri.config(text=f"Sa vajutasid nuppu {k} korda")
    nupp.config(text="Vajuta mind uuesti", fg='black')

aken=tkinter.Tk()
aken.title("Test")
aken.geometry("400x400")
aken.configure(bg='gray')
aken.resizable(width=False, height=False)
aken.iconbitmap("icon.ico")
pealkiri=tkinter.Label(aken, text="Tere tulemast", font=("Futura", 20), bg='white', fg='purple')
pealkiri.pack(pady=20)
nupp=tkinter.Button(aken, text="Vajuta mind", font=("Futura", 15), bg='white', fg='purple', relief="ridge", command=vajutatud)
#ridge, sunken,raised,groove как выглядит кнопка
nupp.pack(pady=20)
nupp.bind("<Button-3>", vajutatudPK) #сделать работу правой кнопки мыши
sisestus=tkinter.Entry(aken, font=("Futura", 15), bg='white', fg='purple', width=20)
sisestus.pack(pady=20)
sisestus.insert(0, "Sisesta midagi siia")
sisestus.bind("<FocusIn>", lambda event: sisestus.delete(0, tkinter.END)) # удаление текста при нажатии

aken.mainloop()