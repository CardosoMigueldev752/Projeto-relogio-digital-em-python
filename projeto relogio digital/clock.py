import tkinter as tk
from time import strftime
import locale
import requests

# tenta configurar os nomes de dia/mês em português
try:
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
except locale.Error:
    pass  # se o sistema não tiver essa locale instalada, segue em inglês mesmo

CIDADE = "Caxambu"  # troque pela sua cidade (use + no lugar de espaço)

root = tk.Tk()
root.title("Digital clock")
root.configure(bg="black")

date_label = tk.Label(root, font=("Helvetica", 18), bg="black", fg="white")
date_label.pack(pady=(20, 0))

clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
clock_label.pack(fill="both", expand=True)

weather_label = tk.Label(root, font=("Helvetica", 18), bg="black", fg="yellow")
weather_label.pack(pady=(0, 20))

def atualizar_relogio():
    agora = strftime("%H:%M:%S")
    clock_label.config(text=agora)
    root.after(1000, atualizar_relogio)

def atualizar_data():
    hoje = strftime("%A, %d de %B de %Y")
    date_label.config(text=hoje)
    root.after(60000, atualizar_data)  # não precisa checar toda hora, 1x por minuto basta

def atualizar_clima():
    try:
        resposta = requests.get(f"https://wttr.in/{CIDADE}?format=%C+%t", timeout=5)
        weather_label.config(text=resposta.text.strip())
    except requests.exceptions.RequestException:
        weather_label.config(text="Clima indisponível")
    root.after(600000, atualizar_clima)  # atualiza a cada 10 min, clima não muda a cada segundo

atualizar_relogio()
atualizar_data()
atualizar_clima()
root.mainloop()