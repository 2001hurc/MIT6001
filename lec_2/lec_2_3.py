an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print('Give me an' + char + '!' )
