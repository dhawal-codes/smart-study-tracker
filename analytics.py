import matplotlib.pyplot as plt
from tracker import get_subject_totals


# Function to display a bar chart of study time by subject
def show_subject_chart():
    
    # Get study time data from tracker module
    data = get_subject_totals()
    print(data)

    # Separate subjects and their corresponding study minutes
    subjects = list(data.keys())
    minutes = list(data.values())

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(subjects, minutes, color='skyblue')

    # Chart labels and title
    plt.xlabel("Subjects")
    plt.ylabel("Total Minutes")
    plt.title("Study Time by Subject")

    # Rotate subject names for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Display the chart
    plt.show()
