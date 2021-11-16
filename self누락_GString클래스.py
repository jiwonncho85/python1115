# 전역변수
str = "Not Class Member"
# 클래스 정의
class GString:
    str = ""
    def __init__(self):
        # 인스턴스 멤버 변수
        self.str = "" 
        GString.str = "클래스 변수"
    def set(self, msg):
        self.str = msg
    def print(self):
        # 버그 발생
        print(str)

g = GString()
g.set("First Message")
g.print()
print("str:{0}".format(GString.str))
