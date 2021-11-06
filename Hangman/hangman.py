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
            if answer in user_used:
                print("You've already guessed this letter")
                count -= 1
                print(''.join(user_list))
                continue
            user_used.append(answer)
            if answer in word_list:
                if word_list.count(answer) >= 2:
                    index = word_list.index(answer)
                    user_list[index] = answer
                    word_list[index] = '-'
                index = word_list.index(answer)
                user_list[index] = answer
                count -= 1
            elif answer not in letters:
                print("Please enter a lowercase English letter")
                count -= 1
                continue
            elif len(answer) >= 2:
                print("You should input a single letter")
                count -= 1
                continue
            elif answer not in (word and word_list):
                print("That letter doesn't appear in the word")
            print(''.join(user_list))
        word_list = list(word)
  