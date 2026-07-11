# Choose ONE provider by importing it:
# - Change `groq` --> `hf` to use Hugging Face API
# - Change `hf` --> `groq` to use Groq API
from hf import generate_response  # <-- switch this line as needed


def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    print("You will try three versions of the same idea: vague, specific, and with context.\n")

    # 1. Vague prompt
    vague = input("Enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague))

    # 2. More specific
    print("\nNow make it more specific (add details like audience, format, or goal).")
    specific = input("Enter your more specific prompt: ")
    print("\nAI's response to specific prompt:")
    print(generate_response(specific))

    # 3. With context
    print("\nNow add context (your situation, constraints, or background).")
    context = input("Enter your prompt with context: ")
    print("\nAI's response to contextual prompt:")
    print(generate_response(context))

    # Reflection
    print("\n--- Reflection ---")
    print("1. How did the AI's response change when the prompt was made more specific?")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produced the most relevant and tailored response? Why?")


if __name__ == "__main__":
    prompt_engineering_activity()