from PIL import Image
img=Image.new('RGB',(1473,1440),'black')
img1=Image.open('C:\Users\Равиль\warhol\marlin.jpg')
img.paste(img1,(0,0),img1.im)

img.save("img_with_watermark.png")          
img.show()


