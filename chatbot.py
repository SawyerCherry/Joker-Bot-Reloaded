from random import choice

print("Hello, my  name is Arthur. I am a sentient AI Chatbot.")

user_response = ""

bot_response_no = ["python", "doofus", "you dont follow instructions"]

bot_response_yes = ["ok", "let\'s enter into the unknown", "okayyyyy"]

while True:
    
    user_response = input("Are you ready to begin a series of Matrix trivia questions?")
    
    if user_response == 'done':

        break


def get_answer_to_first_question(user_response):

    if user_response == "yes":

        return choice(bot_response_yes)

    elif user_response == "no":
        
        confirmation_no = input("are u sure, doofus (y/n)")

        if confirmation_no == "y":
            return choice(bot_response_yes)
        else:
            return choice(bot_response_no)
            
    else:
        pass
        
get_answer_to_first_question(user_response)












#'This is your last chance. After this, there is no turning back. You take the no option– the story ends, you restart the program and try      again. You take the no option – you stay in Wonderland and I show you how deep the rabbit-hole goes. - Morpheus (Probably)'