from rembg import remove
from PIL import Image
input_path = 'sample.jpg'
output_path = 'result.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)