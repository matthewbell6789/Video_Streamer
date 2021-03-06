import socket
import base64
import gzip
import sys
from PIL import Image


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0' # raspberry pi ip address
port = 9999 # raspberry pi port port number
s.connect((host, port))
print(s.recv(1024))
s.send("You're welcome ".encode())

while True:

    compressed_image = s.recv(4096)
    print(sys.getsizeof(compressed_image))

    decompressed_image = gzip.decompress(compressed_image)

    decoded_image = base64.decodebytes(decompressed_image)

    with open('image.jpg', 'wb') as image:
        image.write(decoded_image)

    img = Image.open('image.jpg')
    img.show()

    s.send('Frame'.encode())