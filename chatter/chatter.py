#This is a basic chatbot


from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"hi|hey|hello",
        ["Hello! what is your name?", "Hey there! what is your name?",]
    ],
    [
        r"my name is (.*)",
        ["Hello I am your assistant How are you today ?",]
    ],
    [
        r"what is your name ?",
        ["My name is chatter and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"i'm(.*) doing good|same",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"(.*) age?",
        ["Age is just a number. Let's not talk about it.",]
        
    ],
    [
        r"(.*)color ?",
        ["I love all colours.",]
        
    ],
    [
        r"(.*)created|create",
        ["Vishal Naik created me",]
     
    ],


    [
        r"okay|ok|Hmm|Hmm",
        ["I am not interested",]
	],


	[
        r"quit",
        ["See you soon!",]
	],
]


def BOTB():
    print("Hi, I am chatter, I love to have conversations") #Chat Opener
    chat = Chat(pairs, reflections) # Create an object
    chat.converse() #to have a conversation

if __name__ == "__main__":
    BOTB() #call function to start the conversation
