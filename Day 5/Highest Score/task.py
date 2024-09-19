from ipaddress import summarize_address_range

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#FIND MIN
min_score=student_scores[0]
#manually
for score in student_scores:
    if score< min_score:
        min_score=score
print(min_score)

#method
print (min(student_scores))

#FIND SUM
sum_student_score=0
for score in student_scores:
    sum_student_score+=score
print(sum_student_score)
#method
print(sum(student_scores))