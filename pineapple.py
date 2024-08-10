import sys
import os
from PIL import Image
import glob

name_prefix = ""

start = 1

cat = []
cat.append((2,2))
#cat.append(())
#cat.append((2,2))


def pic_concat(pics, out_name):
    images = [Image.open(x) for x in pics]
    widths, heights = zip(*(i.size for i in images))
   
    max_width = max(widths)
    total_height = sum(heights)
   
    new_im = Image.new('RGB', (max_width, total_height), color="white")
   
    y_offset = 0
    for im in images:
        new_im.paste(im, (0,y_offset))
        y_offset += im.size[1]
    new_im.save(out_name)
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
            os.system('mv "%s" %s%04d.png'%(pics[i],name_prefix,cnt))
            i += 1
            cnt += 1

main()
