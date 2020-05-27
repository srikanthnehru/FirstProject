import qrcode
img = qrcode.make("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
img.save("GoogleNews_QR.png","PNG")