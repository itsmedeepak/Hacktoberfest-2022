import qrcode
import image
qr=qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the ocde image and compicated
    box_size= 10, #size of the box where the qr code will be displayed
    border = 5, # to show the border of the box
)
data =""#add the website link in the data field.
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="red",back_color="silver")
img.save("test.png")

