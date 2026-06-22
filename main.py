# Choose ONE provider by importing it:

#Change groq --> hf to use hugging face API
#Change hf --> groq to use groq API
from groq import generate_response

def prompt_engineering_activity():
    print("Welcome to the Prompt Engineering Tutorial")

    vague = input("Enter a vague prompt:")
    print("\nAi's response to a vague prompt")
    print(generate_response(vague))

    specific = input("Now make it more specific:")
    print("\nAi's response to a specific prompt")
    print(generate_response(specific))

    context = input("Now add context to your specific prompt: ")
    print("\nAi's response to contextual prompt")
    print(generate_response(context))

    print("\n-----Reflection-----")
    print("1. How did the AI's response change when the prompt was made more specific?")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produced the most relevant and tailored response? Why?")

if __name__ == "__main__":
    prompt_engineering_activity()