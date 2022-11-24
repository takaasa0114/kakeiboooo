import Kettle

class Brita(Kettle.Kettle):
    def __init__(self, maxwater):
        super().__init__(maxwater)
        self.cartridge= self.water
  

    def putWater(self, a, t):
        super().putWater(a, t)
        self.cartridge+= a
            
    def pour(self):
        super().pour()
        if(self.cartridge>1000):
            print("なんかにおうぞ！")

    def change(self):
        self. cartridge= 0
        print("カートリッジを交換しました。")
    
       
           
if __name__ == '__main__':
    b= Brita(2000)
    b.putWater(600, 20)
    b.pour()

    b.putWater(600, 20)
    b.pour()
    b.change()

    b.putWater(600, 20)
    b.pour()
