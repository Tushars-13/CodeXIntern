import pandas as pd

# Function to load the data
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("Oops! File not found. Check the file path.")
        return None

# Function to calculate average SGPA
def calculate_average_sgpa(data):
    avg_sgpa = data['SGPA'].mean()
    return avg_sgpa

# Function to list students by year of birth
def list_students_by_year(data, year):
    return data[data['Year of Birth'] == year]

# Function to list students by branch
def list_students_by_branch(data, branch):
    return data[data['Branch'].str.upper() == branch.upper()]

# Function to list students by gender, sorted alphabetically
def list_students_by_gender(data, gender):
    gender = gender.capitalize()  # Ensure first letter is uppercase
    filtered = data[data['Gender'] == gender]
    return filtered.sort_values(by='Name')

# Function to find the student with the highest SGPA
def get_student_with_highest_sgpa(data):
    return data[data['SGPA'] == data['SGPA'].max()]

# Function to find the student with the lowest SGPA
def get_student_with_lowest_sgpa(data):
    return data[data['SGPA'] == data['SGPA'].min()]

# Function to get the top 5 students
def get_top_5_students(data):
    return data.sort_values(by='SGPA', ascending=False).head(5)

# Main menu function
def menu():
    # Get the file from the user
    file_path = input("Enter the path to your CSV file (in .csv format): ")
    data = load_data(file_path)
    if data is None:
        return  # Stop if no data is loaded

    while True:
        # Show menu options
        print("\n--- Menu ---")
        print("1. Calculate average SGPA of the class")
        print("2. List students by year of birth")
        print("3. List students by branch")
        print("4. List students by gender (alphabetical order)")
        print("5. Show the student with the highest SGPA")
        print("6. Show the student with the lowest SGPA")
        print("7. Show the top 5 students")
        print("8. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == '1':
            avg_sgpa = calculate_average_sgpa(data)
            print(f"Average SGPA of the class: {avg_sgpa:.2f}")
        
        elif choice == '2':
            try:
                year = int(input("Enter the year of birth: "))
                students = list_students_by_year(data, year)
                if not students.empty:
                    print(f"Students born in {year}:")
                    print(students)
                else:
                    print("No students found for this year.")
            except ValueError:
                print("Please enter a valid year!")
        
        elif choice == '3':
            branch = input("Enter the branch (e.g., CS, DS, AI): ")
            students = list_students_by_branch(data, branch)
            if not students.empty:
                print(f"Students in branch {branch}:")
                print(students)
            else:
                print(f"No students found in branch {branch}.")
        
        elif choice == '4':
            gender = input("Enter the gender (M/F): ")
            students = list_students_by_gender(data, gender)
            if not students.empty:
                print(f"Students of gender {gender}:")
                print(students)
            else:
                print(f"No students found for gender {gender}.")
        
        elif choice == '5':
            top_student = get_student_with_highest_sgpa(data)
            print("Student with the highest SGPA:")
            print(top_student)
        
        elif choice == '6':
            low_student = get_student_with_lowest_sgpa(data)
            print("Student with the lowest SGPA:")
            print(low_student)
        
        elif choice == '7':
            top_5 = get_top_5_students(data)
            print("Top 5 students of the class:")
            print(top_5)
        
        elif choice == '8':
            print("Exiting. Bye!")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
