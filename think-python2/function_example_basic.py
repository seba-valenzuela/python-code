def print_twice(input):
    print(input)
    print(input)

def combine_words(word1, word2): #THESE word1 and word2 are local variables
    result = word1 + word2       # to the function
    print_twice(result)

word1 = 'hello '
word2 = 'there!'

combine_words(word1, word2)