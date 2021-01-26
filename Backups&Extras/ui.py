get_concat_v_multi_resize(
    [hat_presented, tshirt_presented, jeans_presented, shoes_presented, ]).save(
    'The_outfit_V2.jpg')

final_product = Image.open("The_outfit_V2.jpg")
final_product.show()
