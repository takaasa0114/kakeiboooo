import Kettle
 
 
class CoffeeMaker(Kettle.Kettle):
    def __init__(self, maxwater):
        super().__init__(maxwater)
        self.beans= 0
   
    def putBeans(self, b):
       self.beans+= b
       print(f"コーヒー豆を{b:.1f}g入れました。")
 
    def brew(self):
        if(self.beans>=10 and self.temp>=90):
            super().pour()
            self.beans= 0
            print("おいしいコーヒーが出来上がりました．")
        else:
            print("コーヒー豆が足りないか，温度が適切ではありません．")
    
    def printStatus(self):
        print(f"容量{self.maxwater:.1f}mlのコーヒーメーカーには{self.temp:.1f}℃のお湯が{self.water:.1f}ml，コーヒー豆が{self.beans:.1f}gはいっています。")
        
            
if __name__ == '__main__':
    c= CoffeeMaker(1000)
    c.putWater()
    c.printStatus()
    c.brew()
    c.putBeans(20)
    c.printStatus()
    c.brew()
    c.heat()
    c.printStatus()
    c.brew()
