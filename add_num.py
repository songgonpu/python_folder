from PIL import Image,ImageDraw,ImageFont
import sys


def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40)
    fillcolor = "#ff0000"
    width,height = img.size
    draw.text((width-40,0),'99',font=myfont,fill=fillcolor)
    
    img = img.convert('RGB') 
    img.save('result.jpg')
    #img.save('result.jpg','jpeg')
    
    return 0
    
if __name__=='__main__':
    image_path=sys.argv[1]
    image = Image.open(image_path)
    add_num(image)
    
    

