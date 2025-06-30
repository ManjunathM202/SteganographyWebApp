from PIL import Image
import io

def encode_image(uploaded_image, data_bytes):
    img = Image.open(uploaded_image).convert("RGB")
    data = ''.join(format(byte, '08b') for byte in data_bytes) + '1111111111111110'
    pixels = list(img.getdata())
    new_pixels = []

    data_index = 0
    for pixel in pixels:
        r, g, b = pixel
        if data_index < len(data):
            r = (r & ~1) | int(data[data_index])
            data_index += 1
        if data_index < len(data):
            g = (g & ~1) | int(data[data_index])
            data_index += 1
        if data_index < len(data):
            b = (b & ~1) | int(data[data_index])
            data_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()

def decode_image(uploaded_image):
    img = Image.open(uploaded_image)
    pixels = list(img.getdata())
    bits = ""
    for pixel in pixels:
        for color in pixel:
            bits += str(color & 1)

    end = bits.find('1111111111111110')
    if end != -1:
        bits = bits[:end]
        bytes_out = bytearray()
        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            if len(byte) == 8:
                bytes_out.append(int(byte, 2))
        return bytes(bytes_out)
    return b""
