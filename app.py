from kiro import Agent

# Create Kiro agent using custom local context
agent = Agent(context_file="product.md")

print("Welcome to the Local Guide (Delhi Edition)")
print("Ask me about food, slang, or local culture.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = agent.run(user_input)
    print("Local Guide:", response)
