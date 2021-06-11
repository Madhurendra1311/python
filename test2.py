class Parent:
    def addition(self):
        num1 = input('Enter first number: ')
        num2 = input('Enter second number: ')
        sum = float(num1) + float(num2)
        print(sum)

    def substraction(self):
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        sub = num1 - num2
        print(sub)

    def multiplication(self):
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        mul = num1 * num2
        print(mul)

    def division(self):
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        div = num1/num2
        if(num2==0):
            print("illegal operation")
        else:
            print(div)

    def addition_set(self):
        num1 = {1 , 2, 3}
        num2 = {3, 4, 5}
        sum = (num1) | (num2)
        print(sum)

    def substraction_set(self):
        num1 = {1, 2, 3}
        num2 = {3, 4, 5}
        sub = num1 - num2
        print(sub)


    def division_set(self):
        num1 = {1, 2, 3}
        num2 = {3, 4, 5}
        div = num1 & num2
        print(div)

    def multiplication_matrix(self):
        X = [[1,2,3],
            [4 ,5,6],
            [7 ,8,9]]
 
        Y = [[9,8,7],
            [6,5,4],
            [3,2,1]]
 
 
        result = [[0,0,0],
                [0,0,0],
                [0,0,0]]
 
        # iterate through rows
        for i in range(len(X)):  
        # iterate through columns
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]

        for r in result:
            print(r)

    def substraction_matrix(self):
        matrix1 = [[10, 11, 12],
	                [13, 14, 15],
	                [16, 17, 18]]
        matrix2 = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        rmatrix = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]
        for r in rmatrix:
            print(r)
 

class Child(Parent):
    def func2(self):
        print('this is a child function')

if __name__ == "__main__":
    Ob = Child()
    # Ob.addition()
    # Ob.substraction()
    # Ob.multiplication()
    # Ob.division()
    # Ob.addition_set()
    # Ob.substraction_set()
    # Ob.multiplication_set()
    # Ob.division_set()
    Ob.multiplication_matrix()
    Ob.substraction_matrix()
    Ob.func2()