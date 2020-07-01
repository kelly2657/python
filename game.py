import turtle as t
import random
import pygame.mixer as sounds
sounds.init()
crush = sounds.Sound("explosion.wav")
eatfood = sounds.Sound("eating.wav")

score = 0
playing = False
#화면 설정
WIDTH = 800
HEIGHT = 600
wn = t.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("@AVOIDING TURTLE@ _ 2020810048오혜민")
wn.bgcolor("midnightblue")

#점수판(+ 어떤 거북이가 player고 villain인지 소개 -> 소개는 player가 첫 먹이를 먹으면 사라지게 함)
scorepen=t.Turtle()
scorepen.speed(0)
scorepen.color("white")
scorepen.penup()
scorepen.setposition(-390, 270)
scorestring = "SCORE:" + str(score)
scorepen.write(scorestring,False,"left", font=("Bold",15,"bold"))
scorepen.penup()
scorepen.goto(-390,260)
scorepen.pendown()
scorepen.write("RED = villain, GREEN = player!!",False,"left",font = ("Bold",10,"bold"))
scorepen.hideturtle()

#등장하는 캐릭터들
#player = t
villain = t.Turtle()
food = t.Turtle()
food2 = t.Turtle()
food3 = t.Turtle()
food5 = t.Turtle()

#거북이(player, villain)
t.shape("turtle")
t.color("lime")
villain.shape("turtle")
villain.color("red")
#먹이(색에 따른 점수가 다름)
food.shape("circle")
food.color("peachpuff")
food2.shape("circle")
food2.color("lightsalmon")
food3.shape("circle")
food3.color("salmon")
food5.shape("circle")
food5.color("tomato")

#모두의 첫 위치 지정
t.penup()
t.setposition(0,0)
t.pendown()
villain.penup()
villain.goto(0,200)
villain.pendown()
food.penup()
food2.penup()
food3.penup()
food5.penup()
food.goto(0,-200)
food2.goto(200,0)
food3.goto(-200,0)
food5.goto(300,30)
food.pendown()
food2.pendown()
food3.pendown()
food5.pendown()

#player 이동
def up():
    t.setheading(90)
def down():
    t.setheading(270)
def left():
    t.setheading(180)
def right():
    t.setheading(0)


#시작할때 False -> True
def start():
    global playing 
    if playing == False:
        playing = True
        t.clear()
        play()

#Title 정하기 (시작과 끝을 알림)
def title(m1,m2,m3):
    t.hideturtle()
    t.penup()
    t.clear()
    t.color("lavender")
    t.goto(0,100)
    t.write(m1,False,"center",font=("Bold",50,"bold"))
    t.goto(0,50)
    t.write(m2,False,"center",font=("Bold",30,"bold"))
    t.goto(0,0)
    t.write(m3,False,"center",font=("Bold",30,"bold"))
    t.home
    t.color("lime")
    t.showturtle()

#(게임 시작)
def play():
    global score
    global playing

    angle = villain.towards(t.pos())
    villain.setheading(angle)

    speed = (score/10 + 3)
    if speed > 15:
        speed = 15
    villain.penup()
    villain.forward(speed)
    villain.pendown()
    t.forward(5+ (speed*0.7))

#player거북이와 villain거북이가 만나면 game over
    if t.distance(villain) < 20:
        text = "SCORE:" + str(score)
        title("GAME OVER", text, "REGAME: press space")
        playing = False
        score = 0
        crush.play()

#player 거북이가 벽에 닿으면 반대 방향으로 전진
    x=t.xcor()
    y=t.ycor()
    if x >= 390 or x <= -390 or y >= 290 or y <= -290: #(x는 WIDTH/2-10, y는 HEIGHT/2-10이 안되게 )
        angle2 = t.towards(-t.pos())
        t.setheading(angle2)

#점수는 random 
    movex = random.randint(-230,230)
    movey = random.randint(-230,230)
    random_s = [10,40,30,20,50,100,-10,-30]
    if t.distance(food) < 12:
        score = score + random.choice(random_s)
        food.penup()
        food.goto(movex,movey)
        food.pendown()
        scorestring = "SCORE: " + str(score)
        scorepen.clear()
        scorepen.write(scorestring,False,"left", font=("Bold",15,"bold"))
        eatfood.play()
    if t.distance(food2) < 12:
        score = score + random.choice(random_s)
        movex = random.randint(-230,230)
        movey = random.randint(-230,230)
        food2.penup()
        food2.goto(movex,movey)
        food2.pendown()
        scorestring = "SCORE: " + str(score)
        scorepen.clear()
        scorepen.write(scorestring,False,"left", font=("Bold",15,"bold"))
        eatfood.play()   
    if t.distance(food3) < 12:
        score = score + random.choice(random_s)
        movex = random.randint(-230,230)
        movey = random.randint(-230,230)
        food3.penup()
        food3.goto(movex,movey)
        food3.pendown()
        scorestring = "SCORE: " + str(score)
        scorepen.clear()
        scorepen.write(scorestring,False,"left", font=("Bold",15,"bold"))
        eatfood.play()
    if t.distance(food5) < 12:
        score = score + random.choice(random_s)
        movex = random.randint(-230,230)
        movey = random.randint(-230,230)
        food5.penup()
        food5.goto(movex,movey)
        food5.pendown()
        scorestring = "SCORE: " + str(score)
        scorepen.clear()
        scorepen.write(scorestring,False,"left", font=("Bold",15,"bold"))
        eatfood.play()

# player가 작동시키지 않아도 게임이 시작하면 거북이는 움직인다
    if playing:
        t.ontimer(play,100)

t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
t.onkeypress(start,"space")
t.listen()

title("AVOIDING TURTLE", "[How to play: press space]","  ")

wn.mainloop()
