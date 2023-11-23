#!/usr/bin/python3
# -*- coding: utf-8 -*

# Script d'origine :
# https://www.geeksforgeeks.org/how-to-generate-qr-codes-with-a-custom-logo-using-python/

# import modules
import qrcode
from PIL import Image

# You have 2 parts in this script
# At first, you generate a QRcode with an image in the center of the QR code
# Or, you generate a QRcode without image.

Logo_added=(int(input("Voulez-vous ajouter un logo à votre QRcode ? :\n 0 = non ; 1 = oui\n")))

# Generating QRcode and Adding an image in the QR code center
if Logo_added>0:
 Logo_link =(input("notez le chemin du fichier image\nPar exemple : /home/alban/gererate_qr-code/tux.jpeg\n"))
 logo = Image.open("./img/logo.png")

# taking base width
 basewidth = 100

# adjust image size1
 wpercent = (basewidth/float(logo.size[0]))
 hsize = int((float(logo.size[1])*float(wpercent)))
 logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
 QRcode = qrcode.QRCode(
 error_correction=qrcode.constants.ERROR_CORRECT_H
 )

# taking url or text
 url=(input("Tapez l'adresse complète avec https:// ou le texte voulu :\n"))

# adding URL or text to QRcode
 QRcode.add_data(url)

# generating QR code
 QRcode.make()

# taking color name from user
#QRcolor = 'Orange'
 QRcolor=(input("Quelle couleur voulez-vous ?\norange, black, white, ... ???\n"))


# adding color to QR code
 QRimg = QRcode.make_image(
 fill_color=QRcolor, back_color="White").convert('RGB')

# set size of QR code
 pos = ((QRimg.size[0] - logo.size[0]) // 2,
 (QRimg.size[1] - logo.size[1]) // 2)
 QRimg.paste(logo, pos)

# save the QR code generated
#QRimg.save('gfg_QR_bis.png')
 name_wanted=(input("Tapez le nom voulu (sans extention) pour le fichier PNG du QR-code :\n"))
 name_out=name_wanted+'.png'
 QRimg.save(name_out)

 print('QR code generated!')

# Generating QRcode without image
else:
 print("OK, pas de logo\n")

# adjust image size
QRcode = qrcode.QRCode(
error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url=(input("Tapez l'adresse complète avec https:// ou le texte voulu :\n"))

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
#QRcolor = 'Orange'
QRcolor=(input("Quelles couleur voulez-vous ?\nOrange, Black, White, ... ???\n"))

# adding color to QR code
QRimg = QRcode.make_image(
fill_color=QRcolor, back_color="White").convert('RGB')

# save the QR code generated
#QRimg.save('gfg_QR_bis.png')
name_wanted=(input("Tapez le nom voulu (sans extention) pour le fichier PNG du QR-code :\n"))
name_out=name_wanted+'.png'
QRimg.save(name_out)

print('QR code generated!')