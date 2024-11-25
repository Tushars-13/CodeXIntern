import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load the data
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("Oops! File not found. Check the file path.")
        return None

# Function to plot Pie chart of Gender distribution
def plot_gender_pie_chart(data):
    gender_counts = data['Gender'].value_counts()
    gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])
    plt.title('Gender Distribution of Students')
    plt.ylabel('')  # Hide the y-label
    plt.show()

# Function to plot a bar chart of SGPA distribution
def plot_sgpa_distribution(data):
    plt.figure(figsize=(8,6))
    sns.histplot(data['SGPA'], kde=True, color='blue')
    plt.title('SGPA Distribution of Students')
    plt.xlabel('SGPA')
    plt.ylabel('Frequency')
    plt.show()

# Function to plot the number of students in each branch (Bar Chart)
def plot_branch_distribution(data):
    branch_counts = data['Branch'].value_counts()
    branch_counts.plot(kind='bar', color='orange')
    plt.title('Number of Students in Each Branch')
    plt.xlabel('Branch')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    plt.show()

# Function to plot a scatter plot between SGPA and Year of Birth
def plot_sgpa_vs_year(data):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='Year of Birth', y='SGPA', data=data, color='purple')
    plt.title('SGPA vs Year of Birth')
    plt.xlabel('Year of Birth')
    plt.ylabel('SGPA')
    plt.show()

# Function to plot Top 5 students with highest SGPA (Bar Chart)
def plot_top_5_students(data):
    top_5 = data.nlargest(5, 'SGPA')
    plt.figure(figsize=(8,6))
    sns.barplot(x='Name', y='SGPA', data=top_5, palette='viridis')
    plt.title('Top 5 Students with Highest SGPA')
    plt.xlabel('Student Name')
    plt.ylabel('SGPA')
    plt.xticks(rotation=45)
    plt.show()

# Menu-driven function for visualizations
def menu():
    print()
    print("-----------------------------------------------------------------------")
    print()
    print("Loading visualizations for your CSV file :) ")
    print()
    data = load_data("students.csv")
    if data is None:
        return  # Stop if no data is loaded

    while True:
        print("\n--- Visualization Menu ---")
        print("1. Pie chart of Gender distribution")
        print("2. SGPA distribution (Histogram with KDE)")
        print("3. Number of students in each branch (Bar chart)")
        print("4. Scatter plot of SGPA vs Year of Birth")
        print("5. Top 5 students with highest SGPA (Bar chart)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            plot_gender_pie_chart(data)
        
        elif choice == '2':
            plot_sgpa_distribution(data)
        
        elif choice == '3':
            plot_branch_distribution(data)
        
        elif choice == '4':
            plot_sgpa_vs_year(data)
        
        elif choice == '5':
            plot_top_5_students(data)
        
        elif choice == '6':
            print("Exiting. Bye!")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()

