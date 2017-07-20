import math

while True:
    try:
        n = int(input())
        info = 'NO'
        if n == 0:
            print('YES')
        elif n < 0:
            print('NO')
        else:
            for i in range(int(math.sqrt(n)) + 1):
                for j in range(int(math.sqrt(n)) + 1):
                    if i*i + j*j == n:
                        info = 'YES'
                        break
            print(info)

    except:
        quit()