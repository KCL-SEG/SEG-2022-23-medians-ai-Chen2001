while True: 
    try: 
        print("Enter a list of numbers separated by commas: ") 
        numbers = [float(value) for value in input().split(",")] 
    except ValueError: 
        print("Some input could not be converted to a number!") 
    else: 
        a=len(numbers); 
        result=(numbers[a//2-1]+numbers[a//2])/2 if a%2==0 else numbers[a//2] 
        break 
print(result)