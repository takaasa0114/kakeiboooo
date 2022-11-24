gaitaka=[]
gaihiku=[]
kaitaka=[]
kaihiku=[]
seitaka=[]
seihiku=[]
kyoutaka=[]
kyouhiku=[]
sintaka=[]
sinhiku=[]
import time
for z in range(10000):
    x=input("あなたの名前を教えてね")
    print("今から質問に答えてね。全く当てはまらないのは0、ほとんど当てはまらないのは1、どちらでも無いのは2、"+
          "やや当てはまるのは3,完全に当てはまるの4を選んでね")
    time.sleep(3)
    a=int(input("質問1。初対面の人に会うのが好きで、初めてでも会話を楽しめる"))
    b=int(input("質問2。思いやりがあって、それを行動に移し、差別せず親切にする"))
    c=int(input("質問3。きっちりと物事をこなし、手際よく、効率よく物事を行なう"))
    d=int(input("質問4。いつも心配事が多く、不安になりやすいほうだ"))
    e=int(input("質問5。新しいことを知るのが好きでクリエイティブ、好奇心や探求心がつよい"))
    ff=int(input("質問6。恥ずかしがり屋で物静か、人が多いパーティなどは苦手だ"))
    gg=int(input("質問7。思ったことを口にし、他人の感情に流されず、冷静な判断をする"))
    hh=int(input("質問8。後先考えず衝動的に行動し、ギリギリまで物事に手をつけない事がある"))
    ii=int(input("質問9。たいていリラックスして落ち着いている"))
    jj=int(input("質問10。物事を現実的に考えて型破りなことはしない、保守的な考えだ"))
    f=4-ff
    g=4-gg
    h=4-hh
    i=4-ii
    j=4-jj
  
    if a+f>=5:
        print(str(x)+"さんは外向性が高く、")
        gaitaka.append(x)
    else:
        print(str(x)+"さんは外向性が低く、")
        gaihiku.append(x)
    if b+g>=5:
        print("開放性が高く、")
        kaitaka.append(x)
    else:
        print("開放性が低く、")
        kaihiku.append(x)
    if c+h>=5:
        print("誠実性が高く、")
        seitaka.append(x)
    else:
        print("誠実性が低く、")
        seihiku.append(x)
    if d+i>=5:
        print("協調性が高く、")
        kyoutaka.append(x)
    else:
        print("協調性が低く、")
        kyouhiku.append(x)
    if e+j>=5:
        print("神経症的傾向が高い傾向があります。")
        sintaka.append(x)
    else:
        print("神経症的傾向が低い傾向があります。")
        sinhiku.append(x)

    if a+f>=5:
        if len(gaitaka)==0:
            print("あなたと外向性が合う人はまだいないよ。")
        else:
            print("あなたと外向性が合う人は")
            print(gaitaka)
            print("さんたちだよ")
    if a+f<=4:
        if len(gaihiku)==0:
            print("あなたと外向性が合う人はまだいないよ。")
        else:
            print("あなたと外向性が合う人は")
            print(gaihiku)
            print("さんたちだよ")

        
        
    
    
