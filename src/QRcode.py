import os
from customtkinter import CTk, CTkLabel, CTkTextbox, CTkButton, CTkImage, CTkOptionMenu, StringVar, CENTER
from tkinter import Label, filedialog
from PIL import Image, ImageTk
import qrcode
from qrcode.constants import ERROR_CORRECT_L

APP_PATH = os.path.dirname(os.path.realpath(__file__))

class QRGenerator:

    def __init__(self, window : CTk) -> None:
        self.window = window

    def run(self):
        self.views()
        self.window.mainloop()

    def create_QR(self, link : str, size : int = 10, box_size : int = 3, border : int = 5, color : str = "black"):
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
        if not os.path.exists("C:\Qrcode"):
            os.mkdir("C:\Qrcode")
        print(self.getTextSave())
        img.save("C:/Qrcode/" + str(self.getTextSave()) + ".png")

    def viewQR(self, color : str = "black"):
        try:
            self.QRlabel.destroy()
        except:
            pass
        self.qr = self.create_QR(self.getTextLink(), color=color)
        self.imgQR : ImageTk.PhotoImage = ImageTk.PhotoImage(self.qr)
        self.QRlabel : Label = Label(master=self.window, 
                                        text="", 
                                        image=self.imgQR
        )

    def showQRFirsttime(self, color : str = "black"):
        if self.getTextLink() != "\n":
            self.viewQR(color)
            self.window.geometry("720x550")
            self.linkLabel.place(relx=0.5, rely=0.07, anchor= CENTER)
            self.linkTextbox.place(relx=0.5, rely=0.15, anchor= CENTER)
            self.generateButton.place(relx=0.5, rely=0.26, anchor= CENTER)
            self.QRlabel.place(relx=0.2, rely=0.55, anchor= CENTER)
            self.saveWidget()
            self.colorWidget()

    def showQR(self, color : str = "black"):
        if self.getTextLink() != "\n":
            self.viewQR(color)
            self.QRlabel.place(relx=0.2, rely=0.55, anchor= CENTER)
            
    def colorCallback(self):
        self.selectColor = self.colorOptionmenu.get()
        self.colorOptionmenu.set(self.selectColor)
        match self.selectColor:
            case "Noir":
                self.showQR()
                self.colorOptionmenu.configure(button_color="black")
            case "Vert":
                self.showQR("green")
                self.colorOptionmenu.configure(button_color="green")
            case "Jaune":
                self.showQR("yellow")
                self.colorOptionmenu.configure(button_color="yellow")
            case "Bleu":
                self.showQR("blue")
                self.colorOptionmenu.configure(button_color="blue")
            case "Rouge":
                self.showQR("red")
                self.colorOptionmenu.configure(button_color="red")

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
        self.saveLabel.place(relx=0.65, rely=0.44, anchor= CENTER)
        self.saveTextbox.place(relx=0.65, rely=0.50, anchor= CENTER)
        self.saveButton.place(relx=0.65, rely=0.57, anchor= CENTER)


    def colorWidget(self):
        self.couleur = ["Noir", "Vert", "Jaune", "Bleu", "Rouge"]
        self.colorLabel : CTkLabel = CTkLabel(
            master=self.window, 
            text='Couleur du QRcode',
            font=("Courier", 16)
        )
        self.colorOptionmenu : CTkOptionMenu = CTkOptionMenu(
            master = self.window,
            button_color="black",
            values = self.couleur,
            command = lambda x:self.colorCallback()
        )
        self.colorLabel.place(relx=0.2, rely=0.8, anchor= CENTER)
        self.colorOptionmenu.place(relx=0.2, rely=0.85, anchor= CENTER)

    def views(self):
        self.window.geometry("720x200")
        self.window.resizable(width=False, height=False)
        self.window.title("QRCode")
        # self.window.iconbitmap(APP_PATH + r'\..\img\icon.ico')
        self.linkWidget()

if __name__ == "__main__":
    window = CTk()
    app = QRGenerator(window)
    app.run()
