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
        user_word_list_null = "-" * len(word)  # ------
        user_used = []    # [-,-,-,-,-,-]
        user_list = list(user_word_list_null)
        print(user_word_list_null)
