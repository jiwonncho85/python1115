# Function2.py

def setValue(newValue):
    x = newValue

result = setValue(5)
print(result)


# 튜플 리턴

def times(a,b):
    return a+b, a*b

result = times(3,4)
print(result)

# 참조를 전달

def change(x):
    x[0] = "H"

# 함수를 호출

wordlist = ["J", "A", "M"]

#change(wordlist)
print("함수 호출후:", wordlist)


def change1(x):
    # 내부에 복사를 생성(Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)

print("함수 호출후:", wordlist)

