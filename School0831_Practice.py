time = int(input(">>>초 입력"))
minute = time//60
second = time%60
print(minute, "분", second, "초")


min = int(input(">>>분 입력"))
day = min // 1440
time2 = min // 1440
second2 = min % 1440 % 60
print(day, "일", time2, "시간", second2, "분")


premoney = int(input(">>>>원금 입력"))
year = int(input(">>>몇년 넣을지 입력")) 
interest = int(input(">>이자 이율 입력"))
print(premoney * (1+interest)* (1+interest)* (1+interest)* (1+interest)* (1+interest))


number = int(input(">>>숫자 입력"))
print(number*(number+1)/2)

grape = int(input(">>>>포도 개수 입력"))
strawberry = int(input(">>>>딸기 개수 입력"))
print("포도의 무게는", 75 * grape, "g이며 딸기의 무게는", 113.5 * strawberry, "g이며, 총 무게는",
            75 * grape + 113.5 * strawberry, "g입니다.")