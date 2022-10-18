print('welcome to my quiz')
player=input('do you want to play ? : ')
if player!='yes' :
    quit()
print('okey go')
score=0
answer = input('what does cpu stand for ? ')
if answer =='central':
    print('correct')
    score +=1
else:
    print('incorrect')
answer2 = input('what does cpu stand for ? ')
if answer2 =='cnetral':
    print('correct')
    score +=1
else:
    print('incorrect')
answer3 = input('what time is it  ? ')
if answer3 =='3:12pm':
    print('correct')
    score +=1
else:
    print('incorrect')
answer4 = input('what is today ? ')
if answer4 =='tue':
    print('correct')
    score +=1
else:
    print('incorrect')

print('you got '+str(score))

