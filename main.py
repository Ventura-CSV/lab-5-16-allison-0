import random

##################################################
# Make your lambda function here
# return greater value between x and y
greater = lambda x, y: x if x > y else y
# lambda function to filter values greater than 50 from a list
filter50 = lambda mylist: list(filter(lambda x: x > 50, mylist))
##################################################



def main():
    print(greater(10, 20))
    print(greater(20, 10))
    print(greater(100, 20))

    numbers = [random.randint(0, 100) for i in range(10)]
    print('original list', numbers)
    print('filter 50', filter50(numbers))


if __name__ == '__main__':
    main()
