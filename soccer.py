def game(fname, t1, t2):
    f= open(fname, "r", encoding='utf-8')
    result= None
    for line in f:
        data= line[:-1].split(",")
        if(data[0]==t1 and data[2]==t2):
            result="試合結果 {0:　<8s}  {1:>2}  -  {2:<2}  {3:　>8s}".format(data[0],data[1],data[3],data[2])
        elif(data[2]==t1 and data[0]==t2):
            result="試合結果 {0:　<8s}  {1:>2}  -  {2:<2}  {3:　>8s}".format(data[2],data[3],data[1],data[0])
 
    f.close()
    if result==None:
        result= "試合無し {0:　<10s}　-　{1:　>10s}".format(t1, t2)
 
    print(result)
         
def add(fname, t1, s1, t2, s2):
    f= open(fname, "a", encoding='utf-8')
    f.write("{0},{1},{2},{3}\n".format(t1, s1, t2, s2))
    f.close()
    game(fname, t1, t2)
    print("を追加しました．")


filename="wc2018qh (3).csv"
game(filename, "日本", "セネガル")
game(filename, "日本", "コロンビア")
game(filename, "セネガル", "日本")
add(filename, "フランス", 4, "クロアチア", 2)
game(filename, "フランス", "クロアチア")

