""" print('大家今天好嗎?')
name = "Joannie"
namegroup = ["Joannie", "Kelly", "Amy", "John"]

namegroup.append("Mary")
#namegroup.sort
print(namegroup) """

#tName = input("請輸入老師的姓名:")
#print("老師的名字是:", tName)

num1_score = [90, 88, 100, 78, 92]
englishList = []
englishList.append(num1_score[2])
print(englishList)

#二維陣列
scores = [[70, 88, 100, 80, 84], [65, 78, 80, 78, 85], 
[70, 78, 84, 90, 96], [100, 90, 98, 77, 60], [66, 80, 78, 98, 65]]

print(scores[3][3]) #77分
totalScores = 0
for i in scores[0]:
    totalScores += i

print(totalScores)


