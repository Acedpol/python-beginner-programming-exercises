def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(100):
        n = i + 1
        if(n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif(n % 3 == 0):
            print("Fizz")
        elif(n % 5 == 0):
            print("Buzz")
        else:
            print(n)
    return i
        

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
