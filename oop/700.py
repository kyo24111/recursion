setA = {1,2,3}
setB = {2,3}

print(setA >= setB)
print(setA > setB)
print(setB.issubset(setA))

setC = {2,3}
setD = {2,3}

print(setC >= setD)
print(setC > setD)
print(setD.issubset(setC))

setE = {'r','s'}
setF = {'s','t','r','i','n','g'}

print(setF > setE)
print(setE.issubset(setF))

setG = {'red','blue'}
setH = {'red','green','yellow','black'}

print(setH > setG)
print(setG.issubset(setH))


# # 問題1 webサイトのカラーパターン
# # Josephはwebサイトのデザインを考えています。ブランドイメージに統一感を持たせるため、クライアントから使っても良い色を指定されています。クライアントから指定された色のリストと、Josephが選んだ色のリストが与えられるので、Josephが選んだ色を使うことができるかどうかを判定するcanUseColorPatternという関数を定義してください。
# def canUseColorPattern(suggestColors, myList):
#     # ここから書きましょう。


# red = (255,0,0)
# pink = (255,192,203)
# orange = (255,165,0)
# yellow = (255,255,0)
# lightgreen = (144,255,144)
# green = (0,128,0)
# skyblue = (135,206,235)
# blue = (0,0,255)
# purple = (128,0,128)
# brown = (165,42,42)
# white = (255,255,255)
# black = (0,0,0)

# suggestColors = [red, pink, orange, yellow, lightgreen, green, skyblue, blue, purple, brown, white, black]

# print(canUseColorPattern(suggestColors, [(255,192,203), (144,255,144), (0,0,0)])) 
# print(canUseColorPattern(suggestColors, [(255,192,203), (255,255,255), (0,128,0)])) 
# print(canUseColorPattern(suggestColors, [(254,192,203), (165,42,42), (255,192,203)])) 
# print(canUseColorPattern(suggestColors, [(0,0,255), (128,0,128), (255,128,0)])) 


# # 問題2 ギターのコード
# # Brennanはギターの練習をしています。いくつかのコードを弾けるようになったので、そのコードだけを使った曲を弾いてみたくなりました。Brennanが弾くことができるコードと、曲のコード進行が書かれたリストが与えられるので、Brennanがその曲を演奏できるかどうかを返すcanPlayMusicという関数を定義してください。
# def canPlayMusic(codes, musicCodeList):
#     # ここから書きましょう。


# print(canPlayMusic(['C','Am','G','F'], ['C','G','Am','F','C','G','F','C','C','G','Am','F']))
# print(canPlayMusic(['C','Am','D','G','E'], ['C','G','Am','Em7','F','C','F','G','C','G','Am','G']))
# print(canPlayMusic(['C','Am','D','G','Em','Bm'], ['C','D','Em','Bm','C','D','Em','Em','D','C','D','Em']))
# print(canPlayMusic(['C','Am','D','G','E'], ['G','Am7','Dsus4', 'D','G','C','G','C','G','Dsus4','D']))


# # 問題3 すべての部分集合を列挙
# # 数字の配列が与えられるので、その集合の部分集合をすべて列挙した配列を返すenumerateSubsetという関数を定義してください。
# import itertools # 直積集合を計算できるライブラリを呼び出します。

# def enumrateSubset(intArr):
#     # ここから書きましょう。

    
# print(enumrateSubset([1,2]))
# print(enumrateSubset([10,11,12,13]))