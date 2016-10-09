def fizzbuzz(num):
    """
    The function fizzbuzz receives a single argument and returns a value based on the following rules:
        - 'Fizz' if the argument is divisible by 3 only
        - 'Buzz' if the argument id divisible by 5 only
        - 'FizzBuzz' if the argument is divisible by both 3 and 5
        - otherwise, returns the arg passed

    :param: num: Numerical value
    
    :return: value depending on the rules above
    """
    if num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 5 == 0 and num % 3 != 0:
        return 'Buzz'
    elif num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    else:
        return num
