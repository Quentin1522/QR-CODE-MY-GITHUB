import qrcode

img = qrcode.make('https://github.com/Quentin1522')
img.save('qrcode.png')