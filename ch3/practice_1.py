def average():
    korean = 80
    english = 75
    math = 55
    average = (korean + english+math)/3
    print(average)

def odd_even(a):
    if a%2 == 1:
        print("홀수입니다.")
    else:
        print("짝수입니다")

def id_num():
    id = "881120-1068234"
    YYYYMMDD=id[:6]
    num =id[7:]
    print(YYYYMMDD)
    print(num)

def id_sex():
    pin = "881120-1068234"
    sex_num = pin[7]
    print(sex_num)

def replace_pra():
    a = "a:b:c:d"
    
    print(a.replace(":","#"))

def reverse():
    a = [1,3,5,4,2]
    a.reverse()
    print(a)

def string_print():
    a = ['Life', 'is', 'too', 'short']
    print(" ".join(a))

def add_tuple():
    a = (1,2,3)
    a = a+(4,)
    print(a)

def dict_pra():
    a = {'A':90, 'B':80, 'C':70}
    result = a.pop('B')
    print(result)

def duplcate_del():
    a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
    s1 = set(a)
    print(s1)

if __name__ == "__main__":
    average()
    odd_even(13)
    id_num()
    id_sex()
    replace_pra()
    reverse()
    string_print()
    add_tuple()
    dict_pra()
    duplcate_del()