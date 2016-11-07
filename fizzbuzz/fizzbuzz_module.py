import sys

def fizzbuzz(x):
        
        if x % 15 == 0:
            return ("FizzBuzz")
        else:
            if x % 3 == 0:
                return ("Fizz")
            if x % 5 == 0:
                return ("Buzz")
        return x
    
   


def main():

    number = []
    for i in range(1,101):
        x=fizzbuzz(i)
        
        number.append(x)
    print(number)

    return


if __name__ == '__main__':
    main()
