
import pandas as pd
import matplotlib.pyplot as plt

# Student data
students = {
    "Name": ["Harini", "Akhila", "Priya", "Rahul", "Sneha"],
    "Maths": [85, 75, 95, 60, 88],
    "Science": [90, 80, 92, 65, 85],
    "English": [78, 85, 96, 70, 90],
    "Computer": [92, 70, 89, 55, 95],
    "Social": [88, 90, 94, 68, 92]
}

# Create DataFrame
df = pd.DataFrame(students)

# Calculate total and average
subjects = ["Maths", "Science", "English", "Computer", "Social"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df["Total"] / len(subjects)

# Grade Calculation

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(calculate_grade)

print("\nGrade Distribution:")
print(df[["Name", "Average", "Grade"]])


# Display analysis
print("\nSTUDENT PERFORMANCE ANALYSIS")
print(df)

print("\nClass Average:", round(df["Average"].mean(), 2))
print("Topper:", df.loc[df["Average"].idxmax(), "Name"])

# Student Performance Bar Chart

plt.figure(figsize=(10, 5))

plt.bar(df["Name"], df["Average"])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

# Subject-wise Performance Analysis



subject_average = df[subjects].mean()

plt.figure(figsize=(9, 5))

plt.bar(
    subject_average.index,
    subject_average.values,
    color="orange"
)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--")

plt.tight_layout()

plt.show()

# Grade Distribution Pie Chart

grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Grade Distribution")

plt.tight_layout()
plt.show()

# Export Student Performance Data

df.to_csv("student_performance_results.csv", index=False)

print("\nStudent results saved successfully!")
print("File: student_performance_results.csv")




