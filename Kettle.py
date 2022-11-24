class Kettle(object):
  
    def __init__(self, maxw=1000.0):
        self.water= 100.0
        self.temp= 20.0
        self.maxwater= maxw
      
  
    def putWater(self, amount=100, temperature=20):
        print("水を入れます。")
        maxamount= self.maxwater-self.water
        if(maxamount<amount):
            netamount= maxamount
            print("お湯がいっぱいです。")
        else:
            netamount= amount
        self.temp= (self.water*self.temp+netamount*temperature)/(self.water+netamount)
        self.water= self.water+netamount
  
    def printStatus(self):
        print(f"容量{self.maxwater:.1f}mlのポットには{self.temp:.1f}℃のお湯が{self.water:.1f}mlはいっています。")
  
  
    def heat(self):
        print("水をあたためています。")
        self.temp= self.temp+1000.0/self.water*25.0
        if(self.temp>100):
            self.temp=100
            print("お湯が沸きました")
  
    def pour(self):
        print(f"{self.temp:.1f}℃のお湯を{self.water:.1f}ml注ぎました．")
        self.water= 0
        self.temp= 20
  
  
if __name__ == '__main__':
    k= Kettle(500)
    k.printStatus()
    k.putWater(200, 25)
    k.printStatus()
    k.putWater(300, 10)
    k.printStatus()
    k.heat()
    k.printStatus()
    k.heat()
    k.pour()