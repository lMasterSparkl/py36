import turtle#彩色蟒蛇
import random
colors1=["red","yellow","purple","blue"]
def drawSnake(rad,angle,len,neckrad):    
    for i in range(len):

        turtle.pencolor(colors1[random.randint(0,3)])#列表用中括号调用元素！！！！！【】
        turtle.circle(rad,angle)
        turtle.pencolor(colors1[random.randint(0,3)])
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
def main ():
    turtle.setup(1920,800,0,0)
    pythonsize=30
    
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()
