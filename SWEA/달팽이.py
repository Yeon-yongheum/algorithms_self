num = int(input())
for num2 in range(num):
        n = int(input())
        result=[[0 for i in range(n)] for j in range(n)]
        flag = 0
        count = 1
        x = 0
        y = 0
        cnt = 1
        result[0][0] = 1
        for t in range(n-1):
                if n-cnt == 0:
                        result[y][x] = count
                else:
                        for a in range(4):
                                for i in range(n-cnt):
                                        if a == 0:
                                                result[y][x] = count
                                                x += 1
                                        elif a == 1:
                                                result[y][x] = count
                                                y += 1
                                        elif a == 2:                                
                                                result[y][x] = count
                                                x -= 1
                                        elif a == 3:
                                                result[y][x] = count
                                                y -= 1
                                        count += 1    
                        y += 1
                        x += 1
                        cnt += 2
        print(f'#{num2+1}')
        for c in range(n):
                for c2 in range(n):
                        print(result[c][c2],end=' ')
                print('')