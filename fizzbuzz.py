def fizzbuzz(num=100):
    list = range(1,num+1)
    output = []
    for number in list:
        if number % 15 == 0:
            output.append('FizzBuzz')
        elif number % 3 == 0:
            output.append('Fizz')
        elif number % 5 == 0:
            output.append('Buzz')
        else:
            output.append(number)

    return output
