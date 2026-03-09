# Main Voice Assistant Application

class VoiceAssistant:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, I am {self.name}, your assistant!'

    def respond(self, query):
        responses = {
            'how are you?': f'I am doing well, thank you! How can I assist you today?',
            'what is your name?': f'My name is {self.name}.',
            'bye': 'Goodbye! Have a great day!'
        }
        return responses.get(query.lower(), "I'm sorry, I don't understand that.")

if __name__ == '__main__':
    assistant = VoiceAssistant('Jessie')
    print(assistant.greet())
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'bye':
            print(assistant.respond(user_input))
            break
        print('Assistant:', assistant.respond(user_input))