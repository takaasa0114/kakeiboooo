import Pet
 
class HappyPet(Pet.Pet):
    def __init__(self, n, l=5, h=0):
        super().__init__(n,l)
        self.name=("ハッピー"+str(n))
        self.happiness=h
 
    def play(self):
        super().play()
        if(self.life>=4 and self.happiness>=2):
            print("しあわせだにゃぁ・・・")
 
    def listen(self, call):
        self.unname=call
        if self.unname.find(f"{self.name}") ==-1:
            print("うるさいにゃ、、、")
            self.happiness-=1
        else:
            print(f"はーい{self.name}をよんだかにゃ？") 
            self.happiness+=3
            
            

 
 
if __name__ == '__main__':
    hp1= HappyPet("ねこ次郎")
    hp1.play()
    hp1.listen("ハッピーねこ次郎")
    hp1.listen("やっぱりすし次郎")
    hp1.listen("おーいハッピーねこ次郎")
    hp1.listen("1")
    hp1.play()
