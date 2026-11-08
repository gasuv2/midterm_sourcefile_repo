raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
   
    "Fred,90,85",         
    "Gina",               
    "Henry,90,eighty,85",  
    "Ivy,",              
]


PASSING_GRADE = 75


student_scores = {}

print("=== PROCESSING RAW RECORDS ===")


for record in raw_records:

    fields = record.split(",")


    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    
    name = fields[0].strip()

   
    scores = []
    try:
       
        for score_str in fields[1:]:
            scores.append(int(score_str.strip()))
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

  
    student_scores[name] = scores

print("\n--------------------------------------------------\n")

print("ORGANIZED STUDENT RECORDS")
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")

print("\n--------------------------------------------------\n")


ranking = []


passed_count = 0
failed_count = 0
sum_of_averages = 0


for name, scores in student_scores.items():
    
    if not scores:
        continue

    total = sum(scores)
    num_scores = len(scores)
    average = total / num_scores
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1


    sum_of_averages += average

  
    ranking.append((average, name, highest_score, lowest_score, remark))


ranking.sort(reverse=True)

print("STUDENT GRADE REPORT")
print(f"{'Rank':<6}{'Name':<7}{'Average':<9}{'Highest':<9}{'Lowest':<8}{'Remark'}")

for rank, (avg, name, highest, lowest, remark) in enumerate(ranking, start=1):
    print(f"{rank:<6}{name:<7}{avg:<9.2f}{highest:<9}{lowest:<8}{remark}")

print("\n--------------------------------------------------\n")


total_valid_students = len(ranking)

if total_valid_students > 0:
    class_average = sum_of_averages / total_valid_students
    highest_student = f"{ranking[0][1]} - {ranking[0][0]:.2f}"
    lowest_student = f"{ranking[-1][1]} - {ranking[-1][0]:.2f}"
else:
    class_average = 0.0
    highest_student = "N/A"
    lowest_student = "N/A"

print("CLASS SUMMARY")
print(f"Number of Students: {total_valid_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Highest: {highest_student}")
print(f"Lowest: {lowest_student}")