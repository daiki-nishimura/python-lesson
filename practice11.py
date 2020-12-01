#無限ループする数字当てプログラム。ユーザーに文字を入力してもらい、qが入力されたら終わり。数字が入力されたら正解か判断させる。正解の数値はプログラム内にいくつかリストを持たせておいてユーザーが入力した数字がそのどれかなら「正解」、一致しなかったら不正解と表示させる。もし数字かq意外の文字が入力されたら「数字を入力するか、qで終了します」と表示させる

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")