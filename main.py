from agent import ask_ai
from tools import write_file, read_file, list_files

messages = []

def handle_tools(user_input):
    """
    Tool format:

    WRITE filename
    content...

    READ filename

    LIST
    """

    if user_input.startswith("WRITE "):
        try:
            _, rest = user_input.split(" ", 1)
            file, content = rest.split("\n", 1)
            return write_file(file.strip(), content.strip())
        except:
            return "❌ Invalid WRITE format"

    if user_input.startswith("READ "):
        file = user_input.replace("READ ", "").strip()
        return read_file(file)

    if user_input.strip() == "LIST":
        return list_files()

    return None


print("🤖 AI Coder Started (type 'exit' to quit)\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    tool_result = handle_tools(user)
    if tool_result:
        print("\nTool:\n", tool_result, "\n")
        continue

    messages.append({"role": "user", "content": user})

    reply = ask_ai(messages)

    messages.append({"role": "assistant", "content": reply})

    print("\nAI:\n", reply, "\n")
