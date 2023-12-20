import customtkinter
import os
from PIL import Image, ImageOps, ImageDraw
# set up window

# pip3 install pillow

root = customtkinter.CTk()
root.title("cybersoft")
root.geometry("600x400")


def add_border_radius(image_path, radius):
    image = Image.open(image_path)
    mask = Image.new('L', image.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result


# hình ảnh
image_folder = 'img'

image_path = os.path.join(image_folder, "iphone1.png")
rounded_image = add_border_radius(image_path, 20)

# my_image = customtkinter.CTkImage(light_image=Image.open(image_path),
#                                   dark_image=Image.open(
#                                       image_path),
#                                   size=(300, 300))


my_image = customtkinter.CTkImage(light_image=rounded_image,
                                  dark_image=rounded_image,
                                  size=(300, 300))
image_label = customtkinter.CTkLabel(root, image=my_image, text="")
image_label.pack()
root.mainloop()
