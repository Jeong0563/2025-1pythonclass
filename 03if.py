# 03.19
#조건문

grade = ""
score = int(input("점수 입력"))

print(score)

if score > 60 :
    grade ="합격"
elif score > 50:
    grade = "임시"
else :
    grade = "불합격"
print(grade)


if score >= 90 :
    grade="a"
if score >=80 :
    grade = "b"
if score >= 70 :
    grade = "c"
else :
    grade = "f"

print(grade)

if score >= 90 :
    grade="a"
elif score >=80 :
    grade = "b"
elif score >= 70 :
    grade = "c"
else :
    grade = "f"

print(grade)