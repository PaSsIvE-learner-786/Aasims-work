import random

def game():
  score = random.randint(1,60)
  with open ('hiscore.txt') as f:
    hiscore = f.read()
    if hiscore!='':
      hiscore=int(hiscore)
    else:
      hiscore=0
  if score>hiscore:
    with open('hiscore.txt','w') as f:
      f.write(str(score))
      print("new high score")
    print("your score is ",score," and your high score is ",score)
  else:
    print("your score is ",score)
game()  