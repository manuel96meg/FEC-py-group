def palindromo(word):
    word = word.lower()
    
    wordPalin = word
    wordPalin = list(wordPalin)
    wordPalin.reverse()
    while wordPalin.__contains__(' '):
        wordPalin.remove(' ')
    
    word = list(word)
    while word.__contains__(' '):
        word.remove(' ')
    return word == wordPalin 

word = str(input('ingresar palabra: '))
print(palindromo(word))
