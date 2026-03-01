import customtkinter as ctk
import webbrowser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("Web Shortcut Tool")

# Kısayol sözlüğü
shortcuts = {
    "github": "https://github.com",
    "yt": "https://youtube.com",
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "insta": "https://instagram.com"
}

def open_site():
    text = entry.get().lower().strip()
    
    if text in shortcuts:
        webbrowser.open(shortcuts[text])
    else:
        # bilinmeyen şey yazılırsa google'da ara
        webbrowser.open(f"https://www.google.com/search?q={text}")

title = ctk.CTkLabel(app, text="WEB SHORTCUT", 
                     font=("Arial", 22, "bold"))
title.pack(pady=30)

entry = ctk.CTkEntry(app, placeholder_text="Site yaz (örn: github, yt)", width=250)
entry.pack(pady=15)

button = ctk.CTkButton(app, text="AÇ", command=open_site)
button.pack(pady=20)

app.mainloop()