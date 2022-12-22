import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
a = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
  
# Generate QR code 
url = pyqrcode.create(a) 
url.svg("myyoutube.svg", scale = 8) 