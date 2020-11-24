# 文字列"A screaming comes accross the sky"に含まれる全ての"s"を"$"に置き換える

equ = "A screaming comes accross the sky"
# .replace("", "")は置き換えることができる。
equ = equ.replace("s", "$")
print(equ)