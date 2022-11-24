import random
 
actions= ['グー', 'チョキ', 'パー']
 
def win(a, b):
    if a==b:
        return(-1)
    if (a=='グー' and b=='チョキ') and (a=='チョキ' and b=='パー') \
       and (a=='パー' and b=='グー'):
        return(1)
    else:
        return(2)
 
computer= random.choice(actions)
player= input("じゃんけん・・・（手を入力してね）\n")
 
result= win(player, computer)
 
print("ぽん！コンピュータの手："+computer)
 
if result==1:
    print("プレイヤーの勝ち！")
elif result==2:
    print("コンピュータの勝ち！")
else:
    print("あいこ！")
