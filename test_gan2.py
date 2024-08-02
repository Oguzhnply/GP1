
import tkinter as tk
from tkinter import messagebox


def start_gan_simulation():
    messagebox.showinfo("Başlatıldı", "GAN Kodunu Başlatmak için gerekli işlemleri ekleyin.")


def test_gan_gui():
    root = tk.Tk()
    root.title("Test GAN GUI")

    root.configure(bg='#f0f0f0')
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    label_welcome = tk.Label(root, text="WELCOME TO DESKTOP ADAPTATION APP", font=("Helvetica", 16), bg='#f0f0f0')
    label_welcome.pack(side="bottom", pady=10)

    btn_start_gan = tk.Button(root, text="Start GAN", command=start_gan_simulation, width=30, height=5,
                              bg='#4CAF50', fg='white')
    btn_start_gan.pack(pady=20)

    root.mainloop()


test_gan_gui()