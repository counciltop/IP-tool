import customtkinter as ctk
import socket
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("500x500")
app.title("Fsociety IP Tool")

def lookup_ip():
    target = entry.get()

    try:
        ip = socket.gethostbyname(target)
        response = requests.get(f"http://ip-api.com/json/{ip}").json()

        result_text = f"""
Domain: {target}
IP: {ip}
Ülke: {response['country']}
Şehir: {response['city']}
ISP: {response['isp']}
Org: {response['org']}
        """

        result_label.configure(text=result_text)

    except:
        result_label.configure(text="Hata oluştu!")

# Başlık
title = ctk.CTkLabel(app, text="FSOCIETY IP", 
                     font=("Arial", 28, "bold"))
title.pack(pady=30)

# Giriş kutusu
entry = ctk.CTkEntry(app, 
                     placeholder_text="Fsociety IP", 
                     width=300,
                     height=40)
entry.pack(pady=15)

# Buton
button = ctk.CTkButton(app, text="SORGULA", command=lookup_ip)
button.pack(pady=20)

# Sonuç
result_label = ctk.CTkLabel(app, text="", justify="left")
result_label.pack(pady=20)

app.mainloop()