# リスト["The", "fox", "jumped", "over", "the", "fence", "."]の文字列を正しい英文になるように連結する。単語間に空白が必要だが"."に空白はいらない。

# まず指定されたリストを作る　
list = ["The", "fox", "jumped", "over", "thw", "fence", "."]
# 連結させるメソッドがjoinであり" "で指定したlist内の"文字列"の終わりに空白を追加している
list = " ".join(list) 
# listの[ ]内のインデックスを指定しており（０）は無くてもできる。+で追加している
list = list[0: -2] + "." 
print(list)