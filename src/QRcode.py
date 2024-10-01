import os
from customtkinter import CTk, CTkLabel, CTkTextbox, CTkButton, CTkOptionMenu, CTkSlider , CTkToplevel, CTkFrame, CENTER
from tkinter import filedialog 
from tkinter import messagebox
from tkinter import Label
from PIL import Image, ImageTk
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_H

APP_PATH = os.path.dirname(os.path.realpath(__file__))

class QRGenerator:

    def __init__(self, window : CTk) -> None:
        self.window = window
        self.open = False

    def run(self):
        self.views()
        self.window.mainloop()

    def createQR(self, link : str, size : int = 10, box_size : int = 3, border : int = 5, color : str | tuple = "black"):
        self.qr : qrcode.QRCode = qrcode.QRCode(
            version=size,
            error_correction= ERROR_CORRECT_L,
            box_size=box_size,
            border=border
        )

        self.qr.add_data(link)
        self.qr.make(fit=True)

        self.img = self.qr.make_image(fill_color=color, back_color="white")
        return self.img
    
    def getTextLink(self):
        return self.linkTextbox.get("1.0",'end')
    
    def getTextSave(self):
        return self.saveTextbox.get("1.0",'end')[:-1]
    
    def saveAs(self, img):
        """
        if not os.path.exists("C:\Qrcode"):
            os.mkdir("C:\Qrcode")
        if os.path.exists("C:/Qrcode/" + str(self.getTextSave()) + ".png"):
            self.twoSameFilesWidget(img)
        else:
            img.save("C:/Qrcode/" + str(self.getTextSave()) + ".png")
        """
        fichier = ""
        while fichier=="":
            fichier = filedialog.asksaveasfilename(defaultextension=".png",
                                       filetypes=[("PNG files", "*.png")])
            if (fichier == ""):
                messagebox.showerror("QRCODE","Aucun fichier selectionné")
                
                


    def callbackCancelButton(self):
        self.saveToplevel.destroy()
        self.saveToplevel.update()


    def callbackReplaceButton(self, img):
        img.save("C:/Qrcode/" + str(self.getTextSave()) + ".png")
        self.saveToplevel.destroy()
        self.saveToplevel.update()


    def viewQR(self, basewidth : int = 65, img : str = "", color : str | tuple = "black"):
        self.basewidth = basewidth
        try:
            self.QRlabel.destroy()
        except:
            pass
        if img != "":
            self.qr = self.createQRwithimage(link=self.getTextLink(), basewidth=self.basewidth, img=img, color=color)
        else:
            self.qr = self.createQR(self.getTextLink(), color=color)
        self.imgQR : ImageTk.PhotoImage = ImageTk.PhotoImage(self.qr)
        self.QRlabel : Label = Label(master=self.window, 
                                        text="", 
                                        image=self.imgQR
        )
    
    def createQRwithimage(self, link : str, basewidth : int = 65,  img: str = "",  size : int = 10, box_size : int = 3, border : int = 5, color : str | tuple = "black"):
        self.logo = Image.open(img)
        self.basewidth = basewidth
        self.wpercent = (self.basewidth/float(self.logo.size[0]))
        self.hsize = int((float(self.logo.size[1])*float(self.wpercent)))
        self.logo = self.logo.resize((self.basewidth, self.hsize), Image.Resampling.LANCZOS)
        self.qr : qrcode.QRCode = qrcode.QRCode(
            version=size,
            error_correction= ERROR_CORRECT_H,
            box_size=box_size,
            border=border
        )
        self.qr.add_data(link)
        self.qr.make()
        self.qr = self.qr.make_image(fill_color=color, back_color="White").convert('RGB')
        self.pos = ((self.qr.size[0] - self.logo.size[0]) // 2,
        (self.qr.size[1] - self.logo.size[1]) // 2)
        self.qr.paste(self.logo, self.pos)
        return self.qr


    def showQRFirsttime(self, color : str | tuple = "black"):
        if self.getTextLink() != "\n":
            self.viewQR(color=color)
            self.window.geometry("720x550")
            self.linkLabel.place(relx=0.5, rely=0.07, anchor= CENTER)
            self.linkTextbox.place(relx=0.5, rely=0.15, anchor= CENTER)
            self.generateButton.place(relx=0.5, rely=0.26, anchor= CENTER)
            self.QRlabel.place(relx=0.2, rely=0.55, anchor= CENTER)
            self.saveWidget()
            self.colorWidget()
            self.imgWidget()

    def showQR(self, basewidth : int = 65 , img : str = "", color : str | tuple = "black"):
        self.basewidth = basewidth
        if self.getTextLink() != "\n":
            self.viewQR(img=img, basewidth=self.basewidth, color=color)
            self.QRlabel.place(relx=0.2, rely=0.55, anchor= CENTER)
            
    def optionCallback(self):
        self.selectImg = self.imgOptionmenu.get()
        match self.selectImg:
            case "Sans":
                self.img = ""
                self.open = False
                try:
                    self.progressbarImg.destroy()
                    self.progressBarLabel.destroy()
                except:
                    pass
            case "STJO":
                self.img = "./img/logo.png"
                if self.open == False:
                    self.progressbarImgWidget()
                    self.open = True
                else:
                    self.progressbarImg.set(65)
                    self.progressBarLabel.configure(text=self.progressbarImg.get())
        self.selectColor = self.colorOptionmenu.get()
        self.colorOptionmenu.set(self.selectColor)
        match self.selectColor:
            case "Noir":
                self.showQR(img=self.img)
                self.colorOptionmenu.configure(button_color="black")
            case "Vert":
                self.showQR(img=self.img, color = "green")
                self.colorOptionmenu.configure(button_color="green")
            case "Jaune":
                self.showQR(img=self.img, color = "yellow")
                self.colorOptionmenu.configure(button_color="yellow")
            case "Bleu":
                self.showQR(img=self.img, color = "blue")
                self.colorOptionmenu.configure(button_color="blue")
            case "Rouge":
                self.showQR(img=self.img, color = "red")
                self.colorOptionmenu.configure(button_color="red")
            case "Orange":
                self.showQR(img=self.img, color = "orange")
                self.colorOptionmenu.configure(button_color="orange")
            case "Cyan":
                self.showQR(img=self.img, color = "cyan")
                self.colorOptionmenu.configure(button_color="cyan")
            case "Marron":
                self.showQR(img=self.img, color = "brown")
                self.colorOptionmenu.configure(button_color="brown")
            case "Gris":
                self.showQR(img=self.img, color = "grey")
                self.colorOptionmenu.configure(button_color="grey")
            case "Rose":
                self.showQR(img=self.img, color = "pink")
                self.colorOptionmenu.configure(button_color="pink")
            case "Violet":
                self.showQR(img=self.img, color = "purple")
                self.colorOptionmenu.configure(button_color="purple")
            case "STJO":
                self.showQR(img=self.img, color = (0, 91, 155))
                self.colorOptionmenu.configure(button_color='#005b9b')
            case "vert stjo":
                self.showQR(img=self.img, color = (182, 201, 49))
                self.colorOptionmenu.configure(button_color='#B6C931')
            case "orange stjo" :
                self.showQR(img=self.img, color = (213, 124, 29))
                self.colorOptionmenu.configure(button_color='#D57C1D')
            case "bleu clair stjo" :
                self.showQR(img=self.img, color = (108, 186, 236))
                self.colorOptionmenu.configure(button_color='#6CBAEC')
        

    def progressBarCallback(self):
        try:
            self.progressBarLabel.configure(text=self.progressbarImg.get())
        except:
            pass
        self.selectImg = self.imgOptionmenu.get()
        match self.selectImg:
            case "Sans":
                try:
                    self.progressbarImg.destroy()
                    self.progressBarLabel.destroy()
                except:
                    pass
                self.img = ""
            case "STJO":
                self.img = "./img/logo.png"
        self.basewidth = int(self.progressbarImg.get())
        #print(self.basewidth)
        self.selectColor = self.colorOptionmenu.get()
        self.colorOptionmenu.set(self.selectColor)
        match self.selectColor:
            case "Noir":
                self.showQR(img=self.img, basewidth=self.basewidth)
                self.colorOptionmenu.configure(button_color="black")
            case "Vert":
                self.showQR(img=self.img, basewidth=self.basewidth, color ="green")
                self.colorOptionmenu.configure(button_color="green")
            case "Jaune":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "yellow")
                self.colorOptionmenu.configure(button_color="yellow")
            case "Bleu":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "blue")
                self.colorOptionmenu.configure(button_color="blue")
            case "Rouge":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "red")
                self.colorOptionmenu.configure(button_color="red")
            case "Orange":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "orange")
                self.colorOptionmenu.configure(button_color="orange")
            case "Cyan":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "cyan")
                self.colorOptionmenu.configure(button_color="cyan")
            case "Marron":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "brown")
                self.colorOptionmenu.configure(button_color="brown")
            case "Gris":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "grey")
                self.colorOptionmenu.configure(button_color="grey")
            case "Rose":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "pink")
                self.colorOptionmenu.configure(button_color="pink")
            case "Violet":
                self.showQR(img=self.img, basewidth=self.basewidth, color = "purple")
                self.colorOptionmenu.configure(button_color="purple")
            case "STJO":
                self.showQR(img=self.img, basewidth=self.basewidth, color = (0, 91, 155))
                self.colorOptionmenu.configure(button_color='#005b9b')
            case "vert stjo":
                self.showQR(img=self.img, color = (182, 201, 49))
                self.colorOptionmenu.configure(button_color='#B6C931')
            case "orange stjo" :
                self.showQR(img=self.img, color = (213, 124, 29))
                self.colorOptionmenu.configure(button_color='#D57C1D')
            case "bleu clair stjo" :
                self.showQR(img=self.img, color = (108, 186, 236))
                self.colorOptionmenu.configure(button_color='#6CBAEC')

    def linkWidget(self):
        self.linkLabel : CTkLabel = CTkLabel(
            master=self.window, 
            text='Lien',
            font=("Courier", 20)
        )
        self.linkTextbox : CTkTextbox = CTkTextbox(
            master=self.window,
            height=50,
            width= 600,
            font=("Arial", 25)
        )
        self.generateButton : CTkButton = CTkButton(
            master=self.window,
            text="Générer",
            command= lambda : self.showQRFirsttime()
        )
        self.linkLabel.place(relx=0.5, rely=0.2, anchor= CENTER)
        self.linkTextbox.place(relx=0.5, rely=0.5, anchor= CENTER)
        self.generateButton.place(relx=0.5, rely=0.8, anchor= CENTER)

    def twoSameFilesWidget(self, img):
        self.saveToplevel : CTkToplevel = CTkToplevel(self.window)
        self.saveToplevel.geometry("400x250")
        self.confirmLabel : CTkLabel = CTkLabel(
            master=self.saveToplevel,
            text="Un fichier portant le même nom extiste déjà, veux tu le remplacer ?"
        )
        self.confirmLabel.pack()
        self.confirmSavebutton = CTkButton(
            master=self.saveToplevel, 
            text="Remplacer",
            command= lambda : self.callbackReplaceButton(img)
        )
        self.leavebutton = CTkButton(
            master=self.saveToplevel, 
            text="Annuler",
            command= lambda : self.callbackCancelButton()
        )

        self.confirmLabel.place(relx=0.5, rely=0.3, anchor= CENTER) 
        self.confirmSavebutton.place(relx=0.7, rely=0.8, anchor= CENTER) 
        self.leavebutton.place(relx=0.3, rely=0.8, anchor= CENTER) 

        self.saveToplevel.grab_set()
        self.saveToplevel.focus_set()
        self.saveToplevel.focus_force()

    def saveWidget(self):
        self.saveLabel : CTkLabel = CTkLabel(
            master=self.window, 
            text='Nom du fichier',
            font=("Courier", 16)
        )
        self.saveButton : CTkButton = CTkButton(
            master=self.window,
            text="Enregistrer",
            command = lambda : self.saveAs(self.qr)
        )
        self.saveTextbox : CTkTextbox = CTkTextbox(
            master=self.window,
            height=10,
            width= 300,
            font=("Arial", 14)
        )
        #self.saveLabel.place(relx=0.65, rely=0.44, anchor= CENTER)
        #self.saveTextbox.place(relx=0.65, rely=0.50, anchor= CENTER)
        self.saveButton.place(relx=0.65, rely=0.57, anchor= CENTER)


    def colorWidget(self):
        self.couleur = ["Noir", "Vert", "Jaune", "Bleu", "Rouge", "Orange", "Cyan", "Marron", "Gris", "Rose", "Violet", "STJO","vert stjo","orange stjo","bleu clair stjo"]
        self.colorLabel : CTkLabel = CTkLabel(
            master=self.window, 
            text='Couleur du QRcode',
            font=("Courier", 16)
        )
        self.colorOptionmenu : CTkOptionMenu = CTkOptionMenu(
            master = self.window,
            button_color="black",
            values = self.couleur,
            command = lambda x: self.optionCallback()
        )
        self.colorLabel.place(relx=0.2, rely=0.8, anchor= CENTER)
        self.colorOptionmenu.place(relx=0.2, rely=0.85, anchor= CENTER)


    def imgWidget(self):
        self.img = ["Sans", "STJO"]
        self.imgLabel : CTkLabel = CTkLabel(
            master=self.window, 
            text='Image sur le QRcode',
            font=("Courier", 16)
        )
        self.imgOptionmenu : CTkOptionMenu = CTkOptionMenu(
            master = self.window,
            values = self.img,
            command = lambda x: self.optionCallback()
        )
        self.imgLabel.place(relx=0.65, rely=0.8, anchor= CENTER)
        self.imgOptionmenu.place(relx=0.65, rely=0.85, anchor= CENTER)
    
    def progressbarImgWidget(self):
        self.borderWidth = 65
        self.progressbarImg : CTkSlider = CTkSlider(
            master = self.window,
            from_=20,
            to=80,
            number_of_steps=60,
            command= lambda x : self.progressBarCallback()
        )
        self.progressBarLabel : CTkLabel = CTkLabel(
            master=self.window, 
            text=self.borderWidth,
            font=("Courier", 16)
        )
        self.progressbarImg.place(relx=0.65, rely=0.9, anchor=CENTER)
        self.progressBarLabel.place(relx=0.65, rely=0.95, anchor=CENTER)

    def views(self):
        self.window.geometry("720x200")
        self.window.resizable(width=False, height=False)
        self.window.title("QRCode")
        self.window.iconbitmap("./img/icon.ico")
        self.linkWidget()
