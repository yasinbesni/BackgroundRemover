from rembg import remove

my_path = "image.jpeg"
output_path = "output.png"

with open(my_path, 'rb') as a:
    with open(output_path, 'wb') as b:
        my_file = a.read()
        output_file = remove(my_file)
        b.write(output_file)
