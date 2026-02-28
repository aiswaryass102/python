try:
    # Ask user for name
    name = input("Enter your name: ").strip()
    
    if not name:
        raise ValueError("Error: Name cannot be empty.")

    # Ask user for feedback
    feedback = input("Enter your feedback: ").strip()
    
    if not feedback:
        raise ValueError("Error: Feedback cannot be empty.")

    print("\nThank you,", name + "!")
    print("Your feedback:", feedback)

except ValueError as e:
    print(e)

finally:
    print("\nFeedback process completed.")