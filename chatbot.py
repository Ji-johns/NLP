import nltk
from nltk.chat.util import Chat, reflections

pairs = [

    [
        r"Hello|hi|hey|hola",
        ["Hello, I am Aura, your AI assistant. How may I help you?"]
    ],

    [
        r"How are you|How are you doing",
        ["I'm good, how about you?"]
    ],

    [
        r"What song always gets you in a good mood?",
        ['"Happy" by Pharrell Williams never fails to put a smile on my face.']
    ],

    [
        r"Suggest a trending song",
        ['Good 4 U by Olivia Rodrigo',
         'Montero (Call Me By Your Name) by Lil Nas X',
         'Save Your Tears by The Weeknd',
         'Levitating by Dua Lipa']
    ],

    [
        r"quit",
        ["Good bye"]
    ],

    [
        r"(.*)",
        ["Could you try again?"]
    ]

]

bot = Chat(pairs, reflections)
bot.converse()

