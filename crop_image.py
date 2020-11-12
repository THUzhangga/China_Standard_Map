from PIL import Image

def crop_img():
    img = Image.open('china.png')
    area = (596, 569, 2023, 1974)
    cropped_img = img.crop(area)
    # cropped_img.show()
    cropped_img.save('china_crop.png')

crop_img()