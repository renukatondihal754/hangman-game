import  random
WORDS=["hello","henuka","chinnu","chinnam","helogen"]
GIVEN=['c','h']

def pickword():
    return random.choice(WORDS)
#print(pickword)

def getDashedWord(word):
    res=''
    for letter in word:
        if letter in GIVEN:
            res+=letter

        else:
            res+='-'

    return res 

# print(pickword())
# print(getDashedWord(WORDS))
def main():
    word=pickword()
    tries=7
    while tries:
        print(f"number of tries you have {tries}")
        dashed_word=getDashedWord((word))
        print(dashed_word)
        if dashed_word==word:
            print("you are winner")
            break
        user_input=input("enter a letter\n")
        GIVEN.append(user_input)
        tries+=letterInWord(word,user_input)

    else:
            print("you are loser")

        

def letterInWord(word,letter):
    return 0 if letter in word else -1

main()