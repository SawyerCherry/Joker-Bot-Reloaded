from random import choice


def get_answer_to_first_question(user_response):

    bot_response_no = ["Are you sure? I'll give you another chance", "Who wouldn't want to hear a joke", "eventually you'll have to say yes, you know that right?"]

    bot_response_yes = ["ok", "let\'s enter into the unknown", "okayyyyy"]

    if user_response == "yes":

        return choice(bot_response_yes)

    elif user_response == "no":
        
        confirmation_no = input("are u sure, doofus (yes/no)")

        if confirmation_no == "yes":
            return choice(bot_response_yes)
        else:
            return choice(bot_response_no)
            
    else:

        print("wrong input")
        
# get_answer_to_first_question(user_response)
print("Hello, my  name is Arthur. I am a sentient AI Chatbot.")

user_response = ""

while True:
    
    
    user_response = input("Are you ready to begin a series of Matrix trivia questions?(yes/no)")
    
    bot_response = get_answer_to_first_question(user_response)

    print(bot_response)

    if user_response == 'done':
        print('see ya')

        break