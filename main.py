import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x200")
        self.root.title("Text App")
        
        self.mainframe = tk.Frame(self.root, background = 'white')
        self.mainframe.pack(fill="both", expand=True)

        self.text = ttk.Label(self.mainframe, text= "Hello World", background="white", font=("Brass Mono", 30))
        self.text.grid(row=0, column=0)

        self.set_text = ttk.Entry(self.mainframe)
        self.set_text.grid(row=1, column=0, pady=10, sticky="NWES")
       
        self.set_button = ttk.Button(self.mainframe, text= "Set Text", command=self.set_name)
        self.set_button.grid(row=1, column=1, pady=10)

        colour = ["red", "Yellow", "Blue", "Green"]
        self.set_colour = ttk.Combobox(self.mainframe, values= colour)
        self.set_colour.grid(row=2, column=0, pady=10, sticky="NWES")

        self.colour_button = ttk.Button(self.mainframe, text= "Set Colour", command=self.set_colour_button)
        self.colour_button.grid(row=2, column=1, pady=10)

        self.reverse = ttk.Button(self.mainframe, text= "Reverse Text", command=self.reverse_text)
        self.reverse.grid(row=3, column=0, pady=10)

        self.root.mainloop()

        return
    def set_name(self):
        new_name = self.set_text.get()
        self.text.config(text = new_name)

    def set_colour_button(self):
        color= self.set_colour.get()    
        self.text.config(foreground= color)

    def reverse_text(self):
        new = self.text.cget("text")
        reversal = new[::-1]
        self.text.config(text = reversal)
if __name__ == "__main__":
    App()



        


   

        