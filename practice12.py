# 円を表す circle クラスを定義して、そのクラスに面積を計算して返すメソッドareaを持たせる。面積の計算にはPythonの組み込みモジュールmathのpi定数が使える。次にcircleオブジェクトを作ってareaメソッドを呼び出し結果を出力する。

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.calculate_area())