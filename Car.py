class Car(object):
    def __init__(self, name="名無し", pos=1, amount=3):
        self.driver=name
        self.position=pos
        self.gas=amount

    def turn(self, position=1):
        self.direction=position 
    
    def drive(self):
        if self.gas>=1:
            self.gas-=1
            print("ブルル、、")
            if self.direction==1:
                self.position+=1
            else:
                self.position-=1
        else:
            print("ガス欠で動けません！")

    def refuel(self, amount):
        self.gas+=amount

    def printStatus(self):
        print(f"{self.driver}さん号はいま{self.position}丁目にいます。")