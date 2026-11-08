
scores = [88, 71, 95, 75, 85]


print("Student Scores:")
for score in scores:
    print(score)
print()

passed_count = 0
failed_count = 0

for index, score in enumerate(scores, start=1):
    if score >= 90:
        result = "Excellent - Passed"
        passed_count += 1
    elif score >= 80:
        result = "Very Good - Passed"
        passed_count += 1
    elif score >= 75:
        result = "Good - Passed"
        passed_count += 1
    else:
        result = "Failed"
        failed_count += 1
        
    print(f"Student {index}: {score} - {result}")

print()


total_score = sum(scores)
average_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print(f"Total Score: {total_score}")
print(f"Average Score: {int(average_score) if average_score.is_integer() else average_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")