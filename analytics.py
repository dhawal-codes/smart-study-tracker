import matplotlib.pyplot as plt
from tracker import get_subject_totals
def show_subject_chart():
    data = get_subject_totals()
    print(data)
    subjects = list(data.keys())
    minutes = list(data.values())  
    plt.figure(figsize=(10, 6))
    plt.bar(subjects, minutes, color='skyblue')
    plt.xlabel("Subjects")
    plt.ylabel("Total Minutes")
    plt.title("Study Time by Subject")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
