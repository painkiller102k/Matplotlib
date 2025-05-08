import tkinter
import smtplib, ssl
from email.message import EmailMessage
from tkinter import Tk, filedialog, messagebox
import tkinter as tk
import os
import tkinter as ttk

aken = tk.Tk()
aken.title("E-posti klient")
aken.geometry("500x320")
aken["background"] = "lightblue"

frame = tkinter.Frame(aken, bg="lightblue")
frame.pack(pady=10, padx=10)

email1 = tkinter.Label(frame, text="E-post:", bg="black", fg="cyan", font=("Futura", 14))
email1.grid(row=0, column=0, padx=5, pady=5)
email_entry = tkinter.Entry(frame, width=30, bg="black", fg="cyan")
email_entry.grid(row=0, column=1, padx=5, pady=5)

teema1 = tkinter.Label(frame, text="Teema:", bg="black", fg="cyan", font=("Futura", 14))
teema1.grid(row=1, column=0, padx=5, pady=5)
teema_entry = tkinter.Entry(frame, width=30, bg="black", fg="cyan")
teema_entry.grid(row=1, column=1, padx=5, pady=5)

lisa1 = tkinter.Label(frame, text="Lisa fail:", bg="black", fg="cyan", font=("Futura", 14))
lisa1.grid(row=2, column=0, padx=5, pady=5)
lisa_entry = tkinter.Entry(frame, width=30, bg="black", fg="cyan")
lisa_entry.grid(row=2, column=1, padx=5, pady=5)

lisa_button = ttk.Button(frame, text="Vali", bg="white", fg="black", relief="ridge", command=lambda: vali_fail())
lisa_button.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="e")

kiri1 = tkinter.Label(frame, text="Kiri:", bg="black", fg="cyan", font=("Futura", 14))
kiri1.grid(row=3, column=0, padx=5, pady=5)
kiri_entry = tkinter.Text(frame, width=50, height=10, bg="black", fg="cyan")
kiri_entry.grid(row=3, column=1, padx=5, pady=5)

button_saada = ttk.Button(frame, text="Saada", bg="white", relief="ridge", command=lambda: send_gmail(email_entry.get(), teema_entry.get(), kiri_entry.get("1.0", tk.END), lisa_entry.get()))
button_saada.grid(row=3, column=1, padx=5, pady=5, sticky="e")

def send_gmail(email, teema, kiri, fail):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "rossakovmartin@gmail.com"
    parool = "hqkr ilem enqc cvah"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, parool)
            
            for recipient in email.replace(";", ",").split(","):
                msg = EmailMessage()
                msg["From"] = kellelt
                msg["To"] = recipient.strip()
                msg["Subject"] = teema
                msg.set_content(kiri)

                if os.path.isfile(fail):
                    with open(fail, "rb") as f:
                        faili_sisu = f.read()
                        msg.add_attachment(faili_sisu, maintype="application", subtype="octet-stream", filename=os.path.basename(fail))
                server.send_message(msg)
            with open("saadetud_kirjad.txt", "a", encoding="utf-8") as logi_fail:
                logi_fail.write(f"Kellele: {email}\nTeema: {teema}\nFail: {fail}\n\n")

            messagebox.showinfo("Edu!", "E-kiri saadetud edukalt!")

    except Exception as e:
        messagebox.showerror("Viga", f"Ei saanud kirja saata:\n{e}")

def vali_fail():
    fail = filedialog.askopenfilename(title="Vali fail", filetypes=[("Kõik failid", "*.*")])
    if fail:
        lisa_entry.delete(0, tk.END)
        lisa_entry.insert(0, fail)

teema = True

def muuda_teema():
    global teema
    uus_bg = "pink" if teema else "black"
    uus_fg = "black" if teema else "cyan"

    aken.configure(bg="lightgreen" if teema else "lightblue")
    frame.configure(bg="lightgreen" if teema else "lightblue")
    
    for widget in frame.winfo_children():
        if isinstance(widget, (tkinter.Label, tkinter.Entry, tkinter.Button, tkinter.Text)):
            widget.configure(bg=uus_bg, fg=uus_fg)
    teema = not teema

button_teema = tkinter.Button(frame, text="Teema", bg="white", fg="black", relief="ridge", command=muuda_teema)
button_teema.grid(row=4, column=1, padx=5, pady=10, sticky="e")


aken.mainloop()