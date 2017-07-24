import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def makeImage(text="Band Name here",fn_in="bg.png",fn_out="a_test.png"):
    font = ImageFont.truetype("C:\\Users\\Kodkod\\Google Drive\\dev\\flask_projects\\band_name_generator\\DejaVuSans-Bold.ttf",32)
    tcolor = (255,0,0)
    text_pos = (50,100)
    img = Image.open(fn_in)
    draw = ImageDraw.Draw(img)
    text = "...and your band\n   shall be called\n     "+text
    draw.text(text_pos, text, fill=tcolor, font=font)
    del draw
    try:
        img.save(fn_out)
        return fn_out
    except:
        return "Failed to save image"