import os
from customtkinter import CTk, CTkLabel, CTkTextbox, CTkButton, CTkImage, CTkOptionMenu, CENTER
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

    def showQR(self, color : str = "black"):
        if self.getTextLink() != "\n":
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
            self.window.geometry("720x700")
            self.linkLabel.place(relx=0.5, rely=0.05, anchor= CENTER)
            self.linkTextbox.place(relx=0.5, rely=0.12, anchor= CENTER)
            self.generateButton.place(relx=0.5, rely=0.20, anchor= CENTER)
            self.QRlabel.place(relx=0.3, rely=0.4, anchor= CENTER)
            self.saveWidget()
            self.colorWidget()
            
    def colorCallback(self):
        self.showQR(self.colorOptionmenu.get())

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
            command= lambda : self.showQR()
        )
        self.linkLabel.place(relx=0.5, rely=0.1, anchor= CENTER)
        self.linkTextbox.place(relx=0.5, rely=0.2, anchor= CENTER)
        self.generateButton.place(relx=0.5, rely=0.35, anchor= CENTER)


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
            width= 200,
            font=("Arial", 14)
        )
        self.saveLabel.place(relx=0.70, rely=0.3, anchor= CENTER)
        self.saveTextbox.place(relx=0.70, rely=0.35, anchor= CENTER)
        self.saveButton.place(relx=0.70, rely=0.42, anchor= CENTER)


    def colorWidget(self):
        self.colorLabel : CTkLabel = CTkLabel(
            master=self.window, 
            text='Couleur du QRcode',
            font=("Courier", 16)
        )
        self.colorOptionmenu : CTkOptionMenu = CTkOptionMenu(
            master=self.window,
            values=["Vert", "Jaune", "Bleu", "Rouge"],
            command=self.colorCallback()
        )
        self.colorLabel.place(relx=0.5, rely=0.6, anchor= CENTER)
        self.colorOptionmenu.place(relx=0.5, rely=0.7, anchor= CENTER)

    def views(self):
        self.window.geometry("720x400")
        self.window.resizable(width=False, height=False)
        self.window.title("QRCode")
        self.window.iconbitmap(APP_PATH + r'\..\img\icon.ico')
        self.linkWidget()

if __name__ == "__main__":
    window = CTk()
    app = QRGenerator(window)
    app.run()
