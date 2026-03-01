import qrcode
url="https://careercenter.tops-int.com/dashboard"
a=qrcode.make(url)
a.save("tops.png")

