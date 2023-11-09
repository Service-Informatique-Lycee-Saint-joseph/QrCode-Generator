from customtkinter import CTk, CTkLabel, CTkTextbox, CTkButton, CTkImage, CENTER
from PIL import Image
import qrcode
from qrcode.constants import ERROR_CORRECT_L

class QRGenerator:

    def __init__(self, window : CTk) -> None:
        self.window = window

    def run(self):
        self.views()
        self.window.mainloop()

    def create_QR(self, link : str, size : int = 3, box_size : int = 3, border : int = 5, color : str = "black"):
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

    def showQR(self):
        try:
            self.QRlabel.destroy()
        except:
            pass
        self.qr = self.create_QR("http://youtube.com")
        self.imgQR : CTkImage = CTkImage(Image.open("qrcode.png"), size=(150, 150))
        self.QRlabel : CTkLabel = CTkLabel(master=self.window, text="", image=self.imgQR)
        self.QRlabel.place(relx=0.5, rely=0.7, anchor= CENTER)

    def views(self):
        self.window.geometry("720x400")

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

        self.generateButton : CTkButton = CTkButton (
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
