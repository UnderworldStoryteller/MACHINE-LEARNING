from PIL import Image

im = Image.open('westbrook.jpg')#打开图片
pix = im.load()#导入像素
width = im.size[0]#获取宽度
height = im.size[1]#获取长度
demo=open('rgb1.txt','a+')#打开存rgb值的文件，如果不存在就创建
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]  # pix获取rgb值
        rgb = r, g, b
        demo.write(str(rgb) + "\n")  # 把rgb值写入文件

demo.close()

x = width #x坐标  通过对txt里的行数进行整数分解
y = height  #y坐标  x*y = 行数

im = Image.new("RGB",(x,y))#创建图片


x = width  #x坐标  通过对txt里的行数进行整数分解
y = height  #y坐标  x*y = 行数

im = Image.new("RGB",(x,y))#创建图片
file = open('rgb1.txt') #打开rbg值文件

#通过一个个rgb点生成图片
for i in range(0,x):
    for j in range(0,y):
        line = file.readline()#获取一行
        line = line.strip("(")
        line = line.strip()
        line = line.strip(")")
        rgb = line.split(",")#分离rgb
        im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])%2))#rgb转化为像素
im.show()

