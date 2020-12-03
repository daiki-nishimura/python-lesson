# 三角形を表すTriangleクラスを定義して面積を返すareaメソッドを持たせる。そしてTriangleオブジェクトを作ってareaメソッドを呼び出して結果を出力する。
class Triangle():

    def __init__(self,b, h):
        self.bottom = b
        self.height = h

    def triangle_area(self):
        return self.bottom * self.height / 2

a_triangle = Triangle(10, 2)
print(a_triangle.triangle_area())