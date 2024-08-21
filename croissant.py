import sys
import os
from PIL import Image, ImageChops
import glob

name_prefix = "Royal-A-"

start = 196

cat = []
cat.append((196,3))
#cat.append((2,2))


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    #If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def add_margin(im):
    w,h = im.size
    new_im = Image.new('RGB', (w+40, h+40), color="white")
    new_im.paste(im, (20,20))
    return new_im

def pic_concat(pics, out_name):
    images = [trim(Image.open(x)) for x in pics]
    
    widths, heights = zip(*(i.size for i in images))
   
    max_width = max(widths)
    total_height = sum(heights)
   
    new_im = Image.new('RGB', (max_width, total_height), color="white")
   
    y_offset = 0
    for im in images:
        new_im.paste(im, (max_width-im.size[0],y_offset))
        y_offset += im.size[1]
    add_margin(new_im).save(out_name)
    for pic in pics:
        os.system("rm %s"%pic)

def main():
    pics = sorted(glob.glob("*.png"))
    i,j = 0, 0
    cnt = start
    while i < len(pics):
        if j < len(cat) and cnt == cat[j][0]:
            #cat
            cat_pics = []
            for k in range(cat[j][1]):
                os.system('mv "%s" %s%04d-%d.png'%(pics[i],name_prefix, cnt, k))
                cat_pics.append("%s%04d-%d.png"%(name_prefix,cnt,k))
                i += 1
            pic_concat(cat_pics,"%s%04d.png"%(name_prefix,cnt))
            j += 1
            cnt += 1
        else:
            add_margin(trim(Image.open(pics[i]))).save("%s%04d.png"%(name_prefix,cnt))
            os.system('rm "%s"'%pics[i])
            i += 1
            cnt += 1

main()

#add_margin(trim(Image.open("L.png"))).show()
# cp Royal/*.png ~/Library/Application\ Support/Anki2/User\ 1/collection.media
