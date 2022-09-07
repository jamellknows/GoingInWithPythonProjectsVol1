import qrcode as qr 
img = qr.make("https://www.youtube.com/codingwith")

def qrcodegen(website, savename="defaultname"):
    ws = website
    img = qr.make(f"{ws}")
    
    img.save(savename+"-qr.png")

