import requests
from tkinter import *
import customtkinter
from tkinter import messagebox


def UI_Scraping():
    r = requests.get("https://httpbin.org/get",headers= {
        "hacker":"True"
        
    })

    if r.status_code == 200:
        data = r.json()
        request_label.configure(text=r.text)
        messagebox.showinfo("Successfully","Successfully")
    else:
        messagebox.showinfo("Error","Error")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("650x600")

root.iconbitmap("C:\\Users\\Kmuwl\\Downloads\\Dapino-Summer-Blue-Polaroid-Picture.512.ico")

root.title("Blake's Scraper")

(["origin"])

img = customtkinter.CTkCanvas(root,)
img.pack(fill = "both",expand = True)
photo = PhotoImage(file = "C:\\Users\\Kmuwl\\Downloads\\Monroe.png")

img = customtkinter.CTkLabel(root,image=photo)
img.place(x = 0, y = 0,relheight=1,relwidth=1)

entry1 = customtkinter.CTkEntry(master=root, placeholder_text="Successfully")

button = customtkinter.CTkButton(master=root, text="Get Request", command=UI_Scraping)
button.pack(pady=12, padx=10)
button.place(relx = 0.5, rely = 0.5, anchor = customtkinter.CENTER)

request_label = customtkinter.CTkLabel(master = root,text="")
request_label.pack()

root.mainloop()
