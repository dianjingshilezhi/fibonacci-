class Fibonacci():
    @staticmethod
    def of(n):
        i = 1
        j = 0
        for a in range(n):
            number = i + j
            print('Fibonacci({})={}'.format(a+1,number))
            i = j
            j = number
if __name__ == '__main__':
    Fibonacci.of(200)

