import random
print("HANGMAN")
print("The game will be available soon.")
words = ['python', 'javascript', 'html', 'java']
start = 0
letters = list("qwertyuiopasdfghjklzxcvbnm")
while (start != 'exit'):
    if start == "play":
        count = 0
        word = random.choice(words)  # python
        word_list = list(word)  # [p,y,t,h,o,n]
        user_word = "-" * len(word)  # ------
        user_used = []    # [-,-,-,-,-,-]
        user_list = list(user_word)
        print(user_word)
        while (count != 8):
            count += 1
            answer = str(input('Input a letter:'))
