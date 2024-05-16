import segno

price_tag =segno.make("helloworkd")
caminho = "D:\\projetolibras\\libras\\main\\static\\main\\images\\"
price_tag.save(f"{caminho}qrcode.png", scale=10)

def qrcodegenerator(selflink):
    tag = segno.make(selflink)
    qrdirectory = "D:\\projetolibras\\libras\\main\\static\\main\\images\\"
    tag.save(f"{qrdirectory}qrcode.png", scale=15)