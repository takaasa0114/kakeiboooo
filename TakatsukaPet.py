import Pet
import random
import sys
import time

class TakatsukaPet(Pet.Pet):

    def __init__(self, n="名無しちゃん", hh=2):
        self.name=n
        self.happy=hh
        print(f"{self.name}参上だにゃ！")
        

    def esayari(self):
        a=random.randint(1,3)
        b=int(input("猫に餌をあげるよ、魚をあげるときは1、肉をあげるときは2、グラタンをあげるときは3をいれてね"))
        if a==1:
            print("猫はお魚の気分だったね。")
        if a==2:
            print("猫はお肉の気分だったね。")
        if a==3:
            print("猫はグラタンの気分だったね。")

        if a==b:
            self.happy+=2
            print(f"{self.name}はうれしいにゃ！")
        
        if a !=b:
            self.happy-=1
            print(f"{self.name}はこんなのいらないにゃ！")

    def PrintStatus(self):
        print(f"猫の幸せ度は{self.happy}だよ")

    def Owakare(self):
        if self.happy<=0:
            print("こんな飼い主はいやにゃ！")
            time.sleep(5)
            sys.exit()

        else:
            print("大好きにゃ")

if __name__ == '__main__':
    p3=TakatsukaPet("asahi",1)
    p3.esayari()
    p3.PrintStatus()
    p3.Owakare()
    p3.esayari()
    p3.PrintStatus()
    p3.Owakare()
