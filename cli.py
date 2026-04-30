import argparse
import sys
import json # Import json module

def generate_quiz(args):
    """
    Generates structured JSON output of Multiple Choice Questions (MCQs) for a given subject.

    This function is responsible for interfacing with an external Language Model 
    (e.g., via LM Studio) to create a set of mock test questions based on the provided subject.

    Args:
        args: An object containing arguments parsed from the CLI, expected to have 'subject' attribute.
              The value of args.subject is the topic for which the quiz should be generated.
    """
    print(f"Generating quiz for subject: {args.subject}")
    # TODO: Call LM Studio to generate structured JSON output of MCQs.
    # TODO: Implement basic AI self-critique validation on the generated set.

def take_quiz(args):
    """
    Takes and scores a mock test from a previously generated JSON file.

    This function reads the quiz from the specified JSON file, presents questions 
    interactively to the user, collects answers, and calculates the final score.

    Args:
        args: An object containing arguments parsed from the CLI, expected to have 'file' attribute.
              The value of args.file is the path to the quiz JSON file.
    """
    try:
        with open(args.file, 'r') as f:
            quiz_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Quiz file not found at '{args.file}'")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file '{args.file}'. Please ensure it is a valid JSON format.")
        return

    if not isinstance(quiz_data, list) or not quiz_data:
        print("Error: The quiz file structure is invalid or empty. Expected a list of questions.")
        return

    score = 0
    total_questions = len(quiz_data)
    print("\n" + "="*50)
    print("🚀 STARTING MOCK TEST")
    print("="*50)

    for i, question in enumerate(quiz_data):
        print(f"\n--- Question {i+1}/{total_questions} ---")
        print(f"Q: {question.get('question', 'No question text provided.')}")
        options = question.get('options', [])
        
        # Display options and map them to letters A, B, C, D...
        option_map = {}
        for j, option in enumerate(options):
            letter = chr(ord('A') + j)
            print(f"  [{letter}] {option.get('text', 'N/A')}")
            option_map[letter] = option.get('correct_answer') # Store the correct answer key for validation

        # Get user input
        while True:
            user_input = input("Your answer (Enter A, B, C, etc.): ").strip().upper()
            if user_input in option_map:
                break
            else:
                print("Invalid selection. Please enter the letter corresponding to an option.")

        # Check answer
        correct_answer_key = option_map[user_input]
        if correct_answer_key == question.get('correct_answer'): # Assuming 'correct_answer' in JSON is the key (e.g., 'A')
            print("✅ Correct!")
            score += 1
        else:
            # For better feedback, we should ideally know what the correct answer *is* from the structure.
            # Since I don't know the exact structure for validation beyond just checking if it matches a key, 
            # I will assume the JSON has a 'correct_answer' field that is the letter (A, B, C...).
            print(f"❌ Incorrect. The correct answer was {question.get('correct_answer', 'Unknown')}.")


    print("\n" + "="*50)
    print("🎉 QUIZ COMPLETED! 🎉")
    print(f"Your final score is: {score} out of {total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.2f}%")
    print("="*50)


def main():
    parser = argparse.ArgumentParser(
        description="AI-Powered Mock Test Generator CLI",
        epilog="An Adaptive Learning Companion."
    )

    subparsers = parser.add_subparsers(title="commands", dest="command", help="Available commands")
    # subparsers.required = True (optional in python 3.7+ if dest is required, but explicit is better)

    # Generate command
    parser_generate = subparsers.add_parser('generate', help='Generate a mock test for a specific subject')
    parser_generate.add_argument('subject', type=str, help='The subject or topic name (e.g., "Quantum Entanglement")')
    parser_generate.set_defaults(func=generate_quiz)

    # Take command
    parser_take = subparsers.add_parser('take', help='Take a previously generated mock test')
    parser_take.add_argument('file', type=str, help='Path to the quiz JSON file')
    parser_take.set_defaults(func=take_quiz)

    # Parse arguments
    args = parser.parse_args()

    # Execute the appropriate function
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
