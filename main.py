import pyqrcode
from PIL import Image

# Solicita o link ao usuário
link = input("Digite o link: ")

# Cria o QR Code
qr_code = pyqrcode.create(link)

# Salva o QR Code como imagem PNG
qr_code.png("qr_code.png", scale=5)

qr_code.show()
