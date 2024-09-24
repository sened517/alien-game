import pgzrun
from random import randint
alien=Actor("alien")
alien.pos=300,300
msg="shoot the alien"
score=0

def draw():
    screen.fill("light blue")
    alien.draw()
    screen.draw.text(msg,(200,50))
    screen.draw.text(f"Score {score}",(100,50))

def on_mouse_down(pos):
  global msg,score
  if alien.collidepoint(pos):
     sounds.eep.play()
     alien.x=randint(50,400)
     alien.y=randint(50,400)
     msg="Good shot"
     score=score+1
  else:
     msg="You missed it"
     score=score-1               





pgzrun.go()