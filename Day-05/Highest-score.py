# 🧮 Calculate Total and Maximum Scores Using Loops

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# ✅ Using Python's built-in sum() function
total_exam_score = sum(student_scores)
print("Total Exam Score:", total_exam_score)

# ✅ Calculating sum manually using a for loop
total = 0
for score in student_scores:
    total += score
print("Calculated Total using loop:", total)

# ✅ Finding the maximum score using built-in max()
print("Max Score (using max()):", max(student_scores))

# ✅ Finding the maximum score manually using a loop
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print("Max Score (using loop):", max_score)
