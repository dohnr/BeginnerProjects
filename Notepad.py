import tkinter as tk
window = tk.Tk()
window.geometry("700x700")
window.title("Notepad")
label = tk.Label(window, text= "Notepad", font=("Arial, 70"))
label.pack(padx=20, pady=20)
textbox = tk.Text(window, font = ("Arial", 16))
textbox.pack(padx=10)
button = tk.Button(window, text ="Close", font=("Arial", 18), command =window.destroy)
button.pack(padx=10, pady=10)

window.mainloop()