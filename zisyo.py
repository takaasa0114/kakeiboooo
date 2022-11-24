pricelist={"りんご":int(100),"バナナ":int(200),"トマト":int(150),"きゅうり":int(70),"レタス":int(150),
"はくさい":int(100),"しいたけ":int(250),"キャベツ":int(150),"エリンギ":int(200)} #1
print(list(pricelist.items())) #2
wa=pricelist["きゅうり"]+pricelist["キャベツ"]
print(wa) #3
pricelist["まつたけ"]=int(1100) #4
pricelist.update({"くり":int(400)}) #4
print(pricelist) 
def calcTotal(items):  #5
    nedan=0
    for i in range(len(items)):
        if (items[i] in pricelist):
            nedan += int(pricelist[items[i]])
    print('・'.join(items)+"の合計金額は"+str(nedan)+"円です")
calcTotal(["バナナ", "はくさい", "エリンギ"])

zisyo=[]  #6
while True:
    word= input("何か教えてよ")
    if (word in zisyo):
        print(str(word)+"って"+str(zisyo[word])+"だよね。")
    else:
        print(str(word)+"ってなんだっけ？")
        newword= input("その意味を教えてよ。")
        zisyo.update({word:newword})

