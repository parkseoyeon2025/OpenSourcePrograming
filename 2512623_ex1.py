#수정해보기
#git clone practice
import random


student_num=[0]*15
korean=[0]*15
english=[0]*15
math=[0]*15
for i in range(15):
    korean[i]=random.randint(1,100)
    english[i]=random.randint(1,100)
    math[i]=random.randint(1,100)
    student_num[i]=i+1
    
score=[]

for i in range(4):
    score.append(student_num)
    score.append(korean)
    score.append(english)
    score.append(math)

korean_total=0
english_total=0
math_total=0

for i in range(15):
    korean_total=korean_total+korean[i]
    english_total=english_total+english[i]
    math_total=math_total+math[i]
    
korean_avg=(korean_total)/15
english_avg=(english_total)/15
math_avg=(math_total)/15

    
transposed_score=[]
for i in range(len(score[0])):
    row=[]
    for r in score:
        row.append(r[i])
    transposed_score.append(row)


    
max_score=[max(korean),max(english),max(math)]
min_score=[min(korean),min(english),min(math)]
avg_score=[korean_avg,english_avg,math_avg]



print("학번 국어 영어 수학")

for i in range(15):
    for j in range(4):
        print(f"{transposed_score[i][j]}",end="    ")
    print("") 
print("="*50)

print("최고",end="   ")
for i in range(3):
    print(f"{max_score[i]}",end="   ")
print("")
    
print("최저",end="   ")
for i in range(3):
    print(f"{min_score[i]}",end="   ")
print("")
    
    
print("평균",end="   ")
for i in range(3):
    print(f"{avg_score[i]:.2f}",end="   ")
print("")
    
