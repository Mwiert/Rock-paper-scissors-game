import math
from os import system
import random
import tkinter as tk
from typing import Text
from PIL import Image, ImageTk
import time


rPcChoise = ["Taş","Kağıt","Makas"]
winnerTempTas,winnerTempKagit,winnerTempMakas= "Taş","Kağıt","Makas"
rakipPc = random.choice(rPcChoise);
print(rakipPc)  
    
def tasSonuc():
        if(winnerTempTas==rakipPc):
            print("Berabere")
            pencere.configure(background="gray")
        elif(winnerTempMakas==rakipPc):
            print("Kazanan Taş. Kazandın Tebrikler!!!")
            pencere.configure(background="green")
        elif(winnerTempKagit==rakipPc):
            print("Kazanan Kağıt. Kaybettin...")
            pencere.configure(background="red")

        

        
def kagitSonuc():
        if(winnerTempTas==rakipPc):
            print("Kazanan Kağıt. Kazandın Tebrikler!!!")
            pencere.configure(background="green")
        elif(winnerTempMakas==rakipPc):
            print("Kazanan Makas. Kaybettin..."),
            pencere.configure(background="red")
        elif(winnerTempKagit==rakipPc):
            print("Berabere")
            pencere.configure(background="gray")




   
def makasSonuc():
        if(winnerTempTas==rakipPc):
            print("Kazanan Taş. Kaybettin...")
            pencere.configure(background="red")
        elif(winnerTempMakas==rakipPc):
            print("Berabere")
            pencere.configure(background="gray")
        elif(winnerTempKagit==rakipPc):
            print("Kazanan Makas. Kazandın Tebrikler!!!")
            pencere.configure(background="green")

def exit():
    quit()
      

pencere = tk.Tk()
pencere.title("Adding Image to Button")
pencere.geometry("300x700+50+100")
pencere.resizable(width="FALSE", height="FALSE")

btnInfo = tk.Button(text="Çıkmak için tıklayın",command=exit) 
btnInfo.pack()   

btnTasResim = ImageTk.PhotoImage(Image.open("img//rock.PNG"))
btnTas = tk.Button(pencere,image=btnTasResim,command=tasSonuc)
btnTas.pack()
btnKagitResim = ImageTk.PhotoImage(Image.open("img\\paper.PNG"))
btnKagit = tk.Button(pencere,image=btnKagitResim,command=kagitSonuc)
btnKagit.pack()
btnMakasResim = ImageTk.PhotoImage(Image.open("img\\sccrs.PNG"))
btnMakas = tk.Button(pencere,image=btnMakasResim,command=makasSonuc)
btnMakas.pack()

btnInfoTwo = tk.Button(text="Yeşil-->Kazandığınızı\nKırmızı-->Kaybettiğinizi\nGri-->Beraberlik\nGösterir.") 
btnInfoTwo.pack()

tk.mainloop()

