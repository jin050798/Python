
#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
def third_mul():
    i=1
    sum =0
    while i<1000:
        j = i*3
        if j >1000:
            break
        sum +=j
        i=i+1

    print(sum)
#while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성
def while_star():
    i = 1
    
    while i <= 5:
        j = 0
        while j < i:
            print("*",end="")
            j +=1
        print("")
        i +=1

#for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
def for_prac():
    for i in range(1,101) :
        print(i)
#for문을 사용하여 A 학급의 평균 점수를 구해 보자.
def for_avg():
    a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    sum = 0
    for i in range(0,10):
        sum = sum + a[i]
    avg = sum / 10 
    print(avg)


if __name__ == "__main__":
    for_avg()