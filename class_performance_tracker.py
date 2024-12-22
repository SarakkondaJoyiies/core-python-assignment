def cal_avg(students):
    avgs = {}
    for name, marks in students.items():
        avgs[name] = sum(marks) / len(marks)
    return avgs

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
avg_marks = cal_avg(students)
topper = max(avg_marks, key=avg_marks.get)

print("Average Marks:", avg_marks)
print("Top Performer:", topper)
