from src.QRcode import*

windows = CTk()
windows.title("STJO : QR Code")

qrCodeApp = QRGenerator(windows)
qrCodeApp.run()