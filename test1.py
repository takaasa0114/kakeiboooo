worddic= {"angle": int(10), "apple": "りんご", "comic": "コミック", \
          "doctor": "博士", "hospital": "病院", "zoo": "動物園", \
          "computer": "パソコン"}
 
while True:
    word= input("単語を入力してね。\n")
    if(word in worddic):
        print("{0}の意味は{1}です．".format(word, worddic[word]))
    else:
        print("{0}は辞書に載っていません．".format(word))