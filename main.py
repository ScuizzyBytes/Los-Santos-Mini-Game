import subprocess

import customtkinter as ctk
import PIL

Rober = PIL.Image.open("9GAMES/assests/images/Icon.png")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("9GAMES")
        self.resizable(False, False)
        
        self.NINEGAMES = ctk.CTkLabel(self, text="Welcome to 9GAMES", font=("Arial", 30, "bold"), width=400, height=50)
        self.NINEGAMES.place(x=100, y=10)
        
        self.ROBERGME_img = ctk.CTkImage(light_image=Rober, dark_image=Rober, size=(160, 160))
       
        self.RoberLabel = ctk.CTkLabel(self, text="", image=self.ROBERGME_img)
        self.RoberLabel.pack(pady=100, padx= 60, anchor="w")
        
        self.PlayRober = ctk.CTkButton(self, text="Play", font=("Arial", 30, "bold"), width=200, text_color="white", fg_color="green", command= self.Run_Rober)
        self.PlayRober.place(y=270, x= 40)
    
    def Run_Rober(self):
        subprocess.Popen(["python3", "9GAMES/games/ROBER_GAME.py"])
        
app = App()
app.mainloop()