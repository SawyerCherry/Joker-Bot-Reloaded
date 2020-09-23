from random import choice
import sys

def get_answer_to_first_question(user_response):

    bot_response_no = ["Are you sure? I'll give you another chance", "Who wouldn't want to hear a joke", "Eventually you'll have to say yes, you know that right?"]

    bot_response_yes = ["My friend thinks he is smart. He told me an onion is the only food that makes you cry, so I threw a coconut at his face.", "Can a kangaroo jump higher than the Empire State Building? Of course. The Empire State Building can't jump.", "Why couldn't the leopard play hide and seek? Because he was always spotted.", "Did you hear about the kidnapping at school? It's okay. He woke up.", "When life gives you melons, you're dyslexic.", "I was addicted to the hokey pokey, then I turned myself around."]
    
    if user_response == "yes":

        return choice(bot_response_yes)

    elif user_response == "no":
        
        confirmation_no = input("Are you sure, doofus? (yes/no):")

        if confirmation_no == "yes":
            return choice(bot_response_no)
        else:
            return choice(bot_response_yes)
            
    else:

        print("wrong input")
        
# get_answer_to_first_question(user_response)
print("Hello, my  name is Arthur. I was built to be funny.")

user_response = ""

while True:
    
    
    user_response = input("Do you want to hear jokes? (yes/no): ")
    
    bot_response = get_answer_to_first_question(user_response)

    print(bot_response)

    if user_response == 'done':
        print('See Ya')
        sys.exit()
        