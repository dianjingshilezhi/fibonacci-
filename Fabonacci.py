class Fabonacci():
    @staticmethod
    def of(n):
        i = 1
        j = 0
        for a in range(n):
            number = i + j
            print('Fabonacci({})={}'.format(a+1,number))
            i = j
            j = number
if __name__ == '__main__':
    Fabonacci.of(200)

