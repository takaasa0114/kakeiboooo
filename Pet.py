import random
 
class Pet(object):
    def __init__(self, n="名無しにゃん", l=5):
        self.name= n
        self.life= l
        print(f"{self.name}参上だにゃ！")
 
    def eat(self):
        self.life+=2
        print(f"{self.name}は美味しかったにゃ！")

 
    def play(self):
        #random.randint(x, y)はx以上y以下の整数値をランダムに返す関数
        v= random.randint(1, 4)
        if(self.life>=v):
            self.life-= v
            for i in range(v):
                print("ごろ")
            print(f"{self.name}はたのしいにゃ")
        else:
            print(f"{self.name}はもうだるいにゃ")
 
 
if __name__ == '__main__':
    p1= Pet("ねこ太郎", 4)
    p1.play()
    p1.play()
    p1.play()    
    p1.eat()
    p1.eat()
    p1.play()
    p2=Pet()
    p2.eat()