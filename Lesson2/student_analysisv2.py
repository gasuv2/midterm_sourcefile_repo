
def classify_grade(grade):
  
    if 90 <= grade <= 100:
        return "Excellent", "Passed"
    elif 85 <= grade <= 89:
        return "Very Good", "Passed"
    elif 80 <= grade <= 84:
        return "Good", "Passed"
    elif 75 <= grade <= 79:
        return "Satisfactory", "Passed"
    else:
        return "Needs Improvement", "Failed"


def load_students(filename):
  
    students = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                
     
                if not cleaned_line or cleaned_line.startswith("#"):
                    continue

                parts = cleaned_line.split(",")
                if len(parts) != 3:
                    continue  

                student_id = parts[0].strip()
                name = parts[1].strip()
                
                try:
                    grade = float(parts[2].strip())
                except ValueError:
                    continue 

            
                if 0 <= grade <= 100:
                    students.append({
                        "student_id": student_id,
                        "name": name,
                        "grade": grade
                    })

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading '{filename}': {e}")

    return students


def calculate_statistics(students):

    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for s in students:
        g = s["grade"]
        total_grade += g

        _, status = classify_grade(g)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

    
        if g > highest_student["grade"]:
            highest_student = s
        if g < lowest_student["grade"]:
            lowest_student = s

    average = total_grade / len(students)

    return {
        "num_students": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }


def display_students(students):

    if not students:
        print("No student records available.")
        return

    print("\n" + "=" * 75)
    print(f"{'Student ID':<12} | {'Student Name':<22} | {'Grade':<6} | {'Classification':<18} | {'Status':<10}")
    print("=" * 75)

    for s in students:
        classification, status = classify_grade(s["grade"])
        name = s["name"]

        if len(name) > 22:
            name = name[:19] + "..."
            
        print(f"{s['student_id']:<12} | {name:<22} | {s['grade']:<6.2f} | {classification:<18} | {status:<10}")

    print("=" * 75)


def display_statistics(statistics):

    if not statistics:
        print("No statistics to display.")
        return

    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['num_students']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    
    highest = statistics['highest']
    lowest = statistics['lowest']
    print(f"Highest: {highest['name']} - {highest['grade']:.2f}")
    print(f"Lowest: {lowest['name']} - {lowest['grade']:.2f}")


def search_student(students, keyword):

    matches = []
    clean_keyword = keyword.strip().lower()

    for s in students:
        if clean_keyword in s["student_id"].lower() or clean_keyword in s["name"].lower():
            matches.append(s)

    return matches


def save_report(students, statistics, filename):

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 75 + "\n")
            f.write("                     STUDENT GRADE ANALYSIS REPORT\n")
            f.write("=" * 75 + "\n\n")

            f.write("CLASS STATISTICS SUMMARY:\n")
            f.write(f"Number of students: {statistics['num_students']}\n")
            f.write(f"Class average: {statistics['average']:.2f}\n")
            f.write(f"Passed: {statistics['passed']}\n")
            f.write(f"Failed: {statistics['failed']}\n")
            
            h = statistics['highest']
            l = statistics['lowest']
            f.write(f"Highest-performing student: {h['name']} ({h['student_id']}) - {h['grade']:.2f}\n")
            f.write(f"Lowest-performing student:  {l['name']} ({l['student_id']}) - {l['grade']:.2f}\n\n")

            f.write("=" * 75 + "\n")
            f.write(f"{'Student ID':<12} | {'Student Name':<22} | {'Grade':<6} | {'Classification':<18} | {'Status':<10}\n")
            f.write("=" * 75 + "\n")

            for s in students:
                classification, status = classify_grade(s["grade"])
                f.write(f"{s['student_id']:<12} | {s['name']:<22} | {s['grade']:<6.2f} | {classification:<18} | {status:<10}\n")

            f.write("=" * 75 + "\n")

        print(f"\nReport successfully saved to '{filename}'.")
    except OSError as e:
        print(f"File writing error: {e}")


def main():
    
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_students(students)
        elif choice == '2':
            display_statistics(statistics)
        elif choice == '3':
            keyword = input("Enter search term (ID or Name): ")
            matches = search_student(students, keyword)
            if matches:
                print(f"\nFound {len(matches)} matching result(s):")
                display_students(matches)
            else:
                print("\nNo matching records found.")
        elif choice == '4':
            save_report(students, statistics, "grade_report.txt")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose an option from 1 to 5.")
            continue


if __name__ == "__main__":
    main()