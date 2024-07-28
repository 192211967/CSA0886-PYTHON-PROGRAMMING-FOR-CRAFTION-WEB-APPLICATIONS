import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Subjects': ['Math', 'Science', 'English', 'History', 'Art'],
    'Marks': [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)
csv_file_path = 'student_marks.csv'
df.to_csv(csv_file_path, index=False)
df_from_csv = pd.read_csv(csv_file_path)
plt.figure(figsize=(10, 5))
plt.plot(df_from_csv['Subjects'], df_from_csv['Marks'], marker='o', linestyle='-', color='b')
plt.title('Student Marks in Different Subjects')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.ylim(0, 100)
plt.grid(True)
plt.show()
