import random
history = []

qualifiers = ['Why do you say that?',
              'Why do you believe that ' ]
replacement = {'i': 'me', 'me': 'you', 'you': 'I'}
hedges = ['Go on', 'I would like to hear more about that']

def reply(sentence):
    prob = random.randint(1,5)
    if prob in (1,2):
        answer = random.choice(hedges)
    elif prob == 3 and len(history) > 3:
        answer = 'Earlier you said that: ' + \
            changePerson(random.choice(history))
    else:
        answer = random.choice(qualifiers) + changePerson(sentence)
    history.append(sentence)
    return answer

def changePerson(sentence):
    words = sentence.split()
    replyWords  = []
    for word in words:
        replyWords.append(replacement.get(word, word))
    return " ".join(replyWords)

def main():
    print("Good Morning, I Hope you are well today")
    print("What can I do for you?: ")
    while True:
        sentence = input('\n>> ')
        if sentence.upper() == "QUIT":
            print("Have a nice Day!")
            break
        print(reply(sentence))
if __name__ == "__main__":
    main()
