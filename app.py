import cohere


def main():
   # Initialize Cohere client
   co = cohere.Client('aDiCo9ONmUp6RHnCF6Mp1YRN9yxBBDXd5ScmQPLy')

   print("🤖 Cohere Chatbot - Terminal Version")
   print("Type 'quit', 'exit', or 'bye' to end the conversation")
   print("-" * 50)

   while True:
       # Get user input
       user_input = input("\nYou: ").strip()

       # Check for exit commands
       if user_input.lower() in ['quit', 'exit', 'bye']:
           print("👋 Goodbye!")
           break

       # Skip empty inputs
       if not user_input:
           continue

       try:
           # Call Cohere API
           print("🤔 Thinking...")
           response = co.chat(
               model='command-a-03-2025',
               message=user_input,
               max_tokens=30000000000000000,
               temperature=0.1
           )

           # Display response
           print(f"\n🤖 Bot: {response.text}")

       except Exception as e:
           print(f"❌ Error: {e}")


if __name__ == "__main__":
   main()

