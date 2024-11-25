import numpy as np

# Step 1: Load the CSV file
def load_data(file_name):
    # Skip the header row and load numeric data
    data = np.genfromtxt(file_name, delimiter=',', skip_header=1, usecols=(2, 3, 4))
    return data

# Step 2: Calculate statistics for a given array
def calculate_statistics(data, label="Exam"):
    print(f"\nStatistics for {label}:")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Median: {np.median(data):.2f}")
    print(f"Standard Deviation: {np.std(data):.2f}")
    print(f"Minimum: {np.min(data):.2f}")
    print(f"Maximum: {np.max(data):.2f}")

# Step 3: Calculate pass/fail counts for each exam
def calculate_pass_fail(data):
    passed = np.sum(data >= 60)
    failed = np.sum(data < 60)
    return passed, failed

# Step 4: Main function
def main():
    # Load grades.csv
    file_name = 'grades.csv'
    data = load_data(file_name)
    
    # Print the first few rows to understand the structure
    print("First few rows of the dataset:")
    print(data[:5])
    
    # Calculate statistics for each exam
    num_exams = data.shape[1]  # Number of columns (exams)
    total_passed = 0
    total_grades = data.size  # Total number of grades in the dataset
    
    print("\nPer-exam statistics:")
    for i in range(num_exams):
        exam_data = data[:, i]
        calculate_statistics(exam_data, label=f"Exam {i + 1}")
        
        # Pass/Fail counts
        passed, failed = calculate_pass_fail(exam_data)
        total_passed += passed
        print(f"Passed: {passed}, Failed: {failed}")
    
    # Calculate overall statistics
    print("\nOverall statistics for all exams combined:")
    calculate_statistics(data.flatten(), label="All Exams Combined")
    
    # Overall pass percentage
    overall_pass_percentage = (total_passed / total_grades) * 100
    print(f"\nOverall pass percentage: {overall_pass_percentage:.2f}%")

main()
