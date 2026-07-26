def get_grade(score):
    """
    Validates the score and determines the letter grade.
    Returns the grade string, or None if the score is invalid.
    """
    # Validate that the score is within the allowed range
    if score < 0 or score > 100:
        return None
        
    # Determine the grade using conditional logic
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# Main block to manage input, call the function, and format output
if __name__ == "__main__":
    # Take input from the user and convert to an integer
    user_score = int(input("Enter student score (0-100): "))
    
    # Process the grade calculation
    grade = get_grade(user_score)
    
    # Check if the function returned None (invalid score) or a grade
    if grade is None:
        print("Error: Score must be between 0 and 100.")
    else:
        print(f"Grade: {grade}")