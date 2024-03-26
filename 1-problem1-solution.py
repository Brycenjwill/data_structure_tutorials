def reverse_string(word):
    stack = [] #Initialize the stack
    length = len(word) #Get the length of the word thats passed in
    
    for i in range(length): #Add the items from the word to the stack
        stack.append(word[i])
    word = "" #Reset the word so that we can start from the beginning
    
    for i in range(len(stack)): #Remove each item from the end of the stack, and add it to the word to return
        letter = stack.pop()
        word += letter #add the letter on top of stack to the word
    return word

print(reverse_string("elppa")) #Should print apple