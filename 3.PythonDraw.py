#PythonDraw
import turtle

def drawSnake(rad,angle,len,neckrad):
#rad:描述圆形轨迹半径的位置
#angle:表示沿着圆形爬行的弧度值
#turtle.fd()函数表示直线爬行，参数表示爬行距离
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    #创建一个1300*800的窗口，左上角为坐标原点
    pythonsize = 30
    #宽度为30像素
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    #颜色为蓝色#3b9909
    turtle.seth(-40)
    #角度为-40度
    drawSnake(40,80,5,pythonsize/2)

main()
#函数只有被调用才会执行

