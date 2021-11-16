def eval_loop():
    evaluated = 0
    data = input("Enter a string to evaluate. Type 'done' when finished: ")
    while data != 'done':
        evaluated = eval(data)
        print(evaluated)
        data = input("Enter a string to evaluate. Type 'done' when finished: ")
    
    print("Your last result was: " + str(evaluated))
    
eval_loop()