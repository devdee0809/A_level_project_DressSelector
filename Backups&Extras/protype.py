import random
from PIL import Image

# Introduction to program, will convert to labels and buttons later
print("welcome to the outfit designer")
print("In a few seconds, we will generae a new outfit for you using our back catalouge")

# delays to ensure user has time to read/interact
print("Looks like we are done")

# generate random integers - this is the random aspect of the outfit generator
hat_choice = random.randint(1, 4)

# time saving idea

#hat_choice1 = ("Hat" + str(hat_choice) + ".jpeg")

# print(hat_choice1)

#hat_choice = random.choice(["Hat1.jpeg", "Hat2.jpeg", "Hat3.jpeg"])

# simple if/else statements to make an oufit


if hat_choice == 1:
    hat_presented = Image.open("Hat1.jpeg")
elif hat_choice == 2:
    hat_presented = Image.open("Hat2.jpeg")
else:
    hat_presented = Image.open("Hat3.jpeg")

tshirt_choice = random.randint(1, 4)

if tshirt_choice == 1:
    tshirt_presented = Image.open("Tshirt1.jpeg")
elif hat_choice == 2:
    tshirt_presented = Image.open("Tshirt2.jpeg")
else:
    tshirt_presented = Image.open("Tshirt3.jpeg")


shoes_choice = random.randint(1, 4)

if shoes_choice == 1:
    shoes_presented = Image.open("Shoe1.jpeg")
elif shoes_choice == 2:
    shoes_presented = Image.open("Shoe2.jpeg")
else:
    shoes_presented = Image.open("Shoe3.jpeg")


jeans_choice = random.randint(1, 5)

if jeans_choice == 1:
    jeans_presented = Image.open("Jeans1.jpeg")
elif jeans_choice == 2:
    jeans_presented = Image.open("Jeans2.jpeg")
elif jeans_choice == 3:
    jeans_presented = Image.open("Jeans3.jpeg")
else:
    jeans_presented = Image.open("Jeans4.jpeg")


# now create an image that resizes all images in library and then concates them vertically
def concat_vertical_resize(
        hat_presented, tshirt_presented, resample=Image.BICUBIC,
        resize_big_image=True):

    if hat_presented.width == tshirt_presented.width:
        _hat_presented = hat_presented
        _tshirt_presented = tshirt_presented

    elif (((hat_presented.width > tshirt_presented.width) and resize_big_image) or
          ((hat_presented.width < tshirt_presented.width) and not resize_big_image)):
        _hat_presented = hat_presented.resize((tshirt_presented.width, int(
            hat_presented.height * tshirt_presented.width / hat_presented.width)), resample=resample)
        _tshirt_presented = tshirt_presented

    else:
        _hat_presented = hat_presented
        _tshirt_presented = tshirt_presented.resize((hat_presented.width, int(
            tshirt_presented.height * hat_presented.width / tshirt_presented.width)), resample=resample)
    dst = Image.new('RGB', (_hat_presented.width,
                            _hat_presented.height + _tshirt_presented.height))
    dst.paste(_hat_presented, (0, 0))
    dst.paste(_tshirt_presented, (0, _hat_presented.height))
    return dst


concat_vertical_resize(
    hat_presented, tshirt_presented, resize_big_image=False).save(
    'The_outfit.jpg')

final_product = Image.open("The_outfit.jpg")
final_product.show()


# prototype function to concate a list of images vertically - this is how i will take the protoype further and include shoes, shorts etc

def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
    min_width = min(im.width for im in im_list)
    im_list_resize = [
        im.resize(
            (min_width, int(im.height * min_width / im.width)),
            resample=resample) for im in im_list]
    total_height = sum(im.height for im in im_list_resize)
    dst = Image.new('RGB', (min_width, total_height))
    pos_y = 0
    for im in im_list_resize:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst


get_concat_v_multi_resize(
    [hat_presented, tshirt_presented, jeans_presented, shoes_presented, ]).save(
    'The_outfit_V2.jpg')

final_product = Image.open("The_outfit_V2.jpg")
final_product.show()
