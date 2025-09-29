from groq import Groq
client = Groq(api_key="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",timeout=60)
print("chatbot (Groq Streaming): Type 'quit', 'exit', 'bye' to stop\n")


while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("\n chatbot: Goodbye!")
        break
    print("chatbot: ",end="", flush=True)

    stream = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": user_input}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()       
