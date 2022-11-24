#PILの中のImageというモジュールを使えるようにする．モジュールもオブジェクトとして扱われる．
from PIL import Image
 
filename= "picture.png"
 
#以前やったテキストファイルと同様に，オープンして変数に割り当てる．
image= Image.open(filename)

#表示する
print image.format

 
