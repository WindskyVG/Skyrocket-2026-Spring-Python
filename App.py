import cohere
from collections import deque

# 设置保存最近 N 轮对话
N = 5

def main():
    # Initialize Cohere client
    co = cohere.Client('dq3YZTeLugYIRR8YdrYVNS9D06mHTb9FdxFatBmd')

    print("🤖 Cohere Chatbot - Terminal Version")
    print("Type 'quit', 'exit', or 'bye' to end the conversation")
    print("Type 'history' to view recent conversation history")
    print("-" * 50)

    # 使用 deque 保存对话历史，最多 N 轮
    history = deque(maxlen=N)

    while True:
        # Get user input
        user_input = input("\nYou: ").strip()

        def main():
            try:
                while True:
                    user_input = input("\nYou: ").strip()

                    if user_input.lower() in ["exit", "quit"]:
                        print("Bye!")
                        break

                    print("Bot:", user_input[::-1])
            except KeyboardInterrupt:
                print("\n检测到 Ctrl+C，程序安全退出。")

        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
            print("👋 Goodbye!")
            break

        # 查看历史记录
        if user_input.lower() == 'history':
            if not history:
                print("📜 No conversation history yet.")
            else:
                print("\n📜 Recent Conversation History:")
                for i, (u, b) in enumerate(history, start=1):
                    print(f"{i}. You: {u}")
                    print(f"   Bot: {b}")
            continue

        # Skip empty inputs
        if not user_input:
            continue

        try:
            # Call Cohere API
            print("🤔 Thinking...")
            response = co.chat(
                model='command-a-03-2025',
                message=user_input,
                max_tokens=300,
                temperature=0.9
            )

            bot_reply = response.text.strip()
            print(f"\n🤖 Bot: {bot_reply}")

            # 保存到历史
            history.append((user_input, bot_reply))

        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

