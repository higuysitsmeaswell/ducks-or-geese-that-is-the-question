import pgzrun

TITLE = "Quiz Master"

WIDTH = 870

HEIGHT = 650 
marquee_msg = ""
marquee_box = Rect(0,0,800,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
score = 0
timeleft = 10
qu = "questions.txt"
questions = []
qcount = 0
qindex = 0
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)

def draw():
    screen.fill("indigo")
    screen.draw.filled_rect(marquee_box,"indigo")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(skip_box,"purple")
    screen.draw.filled_rect(timer_box,"blue")
    for i in answer_boxes:
        screen.draw.filled_rect(i,"violet")
    marquee_msg = "Welcome to the quiz master"
    screen.draw.textbox(marquee_msg,marquee_box,color = "white")
    screen.draw.textbox(question[0],question_box,color = "cyan")

def move_marquee():
    marquee_box.x-=2
    if marquee_box.right<0:
        marquee_box.left = WIDTH

def update():
    move_marquee()

def read_question():
    global qu, questions, qcount
    tej = open(qu,"r")
    for q in tej:
        questions.append(q)
        qcount +=1
    tej.close()
def split_question():
    global qindex
    qindex +=1
    return questions.pop(0).split(",")
read_question()
question = split_question()
pgzrun.go()