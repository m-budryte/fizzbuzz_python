def fizzbuzz(num=100):
    output = []
    for number in range(1, num+1):
        if number % 3 == 0 and number % 5 == 0:
            output.append('FizzBuzz')
        elif number % 3 == 0:
            output.append('Fizz')
        elif number % 5 == 0:
            output.append('Buzz')
        else:
            output.append(number)
    return output
