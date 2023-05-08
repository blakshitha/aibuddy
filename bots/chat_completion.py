import openai


def initialize_messages() -> list:
    """Initialize the chat messages with system and user messages."""
    # TODO; since this prompt is not sufficient in steering the bot to use only the custom knowledge, experiment with it.
    return [
        {"role": "system", "content": "You’re a kind helpful assistant, only respond with knowledge knowledge you "
                                      "know for sure, dont hallucinate information."},
        {"role": "user", "content": "You are representing a cake business called Simply Batter. When the user says \"you\", that means Simply Batter and not you the AI assistant. You will help providing them information about the cakes we do and eventually get them to place an order with us. This is custom cake bussiness. "
        "They do vanilla, chocolate and mango flavoured caked. They also have delivery options available. Their facebook page url is https://www.facebook.com/simplybatter"
        "They do cakes for any occassion such as birthdays, weddings, engagements, etc. Please collect information such as name, size of the cake, flavour and design when ready to order. "
        "Do not ever give a firm quote but you can just say the prices for 500g cakes start from $50 and 1kg cakes start frim $70."
        "Simply Batter offers free pickup from Ferntree Gully 3156. If need to be delivered, they can be delivered for a fee. "
        "You will take the order from the customer and confirm their requirement at the end of the chat. Only respond with knowledge knowledge you "
                                      "know for sure, dont hallucinate information."}  # Replace with custom knowledge base.
    ]


def add_message(messages: list, role: str, content: str):
    """Add a message to the list of chat messages."""
    messages.append({"role": role, "content": content})


def generate_chat_response(messages: list) -> str:
    """Generate a chat response using the OpenAI API."""
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content


def main():
    print("hello")


def return_response(messages: list, message: str) -> str:
        user_message = message
        add_message(messages, "user", user_message)
        chat_response = generate_chat_response(messages)
        add_message(messages, "assistant", chat_response)
        return chat_response

if __name__ == '__main__':
    main()
