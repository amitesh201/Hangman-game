import random,logo,words, os

stage = logo.stage

#choose a word from list 
word_list = words.word_list
word = random.choice(word_list)
#generate blanks 
length = len(word)
print(" _ "*length)
blanks_list = list("_"*length)
chances = 0
guessed_word=[]
print(logo.hangman_sign)
#collect input 
def take_guess():
    guess = input("Guess a word: ").lower()
    #checks if the word is not guessed
    if guess not in guessed_word:
        #adds the word to the list
        guessed_word.append(guess)
        #loops through the word's alphabets
        for i in range(length):
            #checks if guess matches the word
            if guess == word[i]:
                blanks_list[i] = guess
        if guess in blanks_list:
            print("Correct Guess ", f"{' '.join(blanks_list)}")
            return True
        else:
            print("Please, try another letter")
            os.system('clear')
            return False
    else:
        print("You have already guessed this word")
        return True

while "_" in blanks_list:
        if chances< len(stage):
            status = take_guess()
            if status== False:
                print(stage[chances])
                chances +=1
        elif chances>=len(stage):
            print("You lose to guess the word, the word was",word)    
            break
        
if "_" not in blanks_list:
    print("You win and the correct word was", word)