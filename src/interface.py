import os
from customtkinter import CTk, CTkLabel, CTkTextbox, CTkButton, CTkImage, CENTER
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
    
    def getText(self):
        return self.linkTextbox.get("1.0",'end')
    
    def saveAs(self, img):
        img.save("./save/qrcode.png")


    def showQR(self):
        if self.getText() != "\n":
            try:
                self.QRlabel.destroy()
            except:
                pass
            self.qr = self.create_QR(self.getText())
            self.imgQR : ImageTk.PhotoImage = ImageTk.PhotoImage(self.qr)
            self.QRlabel : Label = Label(master=self.window, 
                                         text="", 
                                         image=self.imgQR
            )

            self.QRlabel.place(relx=0.5, rely=0.7, anchor= CENTER)
            self.saveButton.place(relx=0.9, rely=0.35, anchor= CENTER)

    def saveButton(self, qr):
        self.saveButton : CTkButton = CTkButton(
        master=self.window,
        text="Enregistrer",
        command=self.saveAs(self.qr)
        )

    def views(self):
        self.window.geometry("720x400")
        self.window.resizable(width=False, height=False)
        self.window.title("QRCode")
        self.window.iconbitmap(APP_PATH + r'\..\img\icon.ico')

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
            command=self.showQR
        )

        self.linkLabel.place(relx=0.5, rely=0.1, anchor= CENTER)
        self.linkTextbox.place(relx=0.5, rely=0.2, anchor= CENTER)
        self.generateButton.place(relx=0.5, rely=0.35, anchor= CENTER)

window = CTk()
app = QRGenerator(window)
app.run()
