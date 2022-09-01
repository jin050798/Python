def is_odd(a):
    if a % 2 == 1:
        print("홀수 입니다")
    else:
        print("짝수 입니다")

def avg_forever(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

def input_prac():
    input1 = input("첫번째 숫자를 입력하세요:")
    input2 = input("두번째 숫자를 입력하세요:")

    total = int(input1) + int(input2)
    print("두 수의 합은 %s 입니다" % total)
    
def test():
    f1 = open("C:/Users/KOSTA/project/doit/ch4/test.txt",'w')
    f1.write("Life is too short")
    f1.close()

    f2 = open("C:/Users/KOSTA/project/doit/ch4/test.txt",'r')
    print(f2.read())
    f2.close()

def input_test():
    f1 = open("C:/Users/KOSTA/project/doit/ch4/test2.txt","a")
    n = input("입력하세요 : ")
    f1.write(n)
    f1.write("\n")
    f1.close

def java_no():
    f = open("C:/Users/KOSTA/project/doit/ch4/test.txt",'r')

    body = f.read()
    f.close()

    body = body.replace('java', 'python')

    f = open("C:/Users/KOSTA/project/doit/ch4/test.txt",'w')
    f.write(body)
    f.close

if __name__ == "__main__":
    #is_odd(13)
    #print(avg_forever(1,2,3,4,5))
    #test()
    #input_test()
    java_no()