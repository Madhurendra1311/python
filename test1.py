def listAdder(op1, op2):
    num1,num2 = 0,0
    for i in range(len(op1)):
        num1 = num1*10 + op1[i]

    for i in range(len(op2)):
        num2 = num2*10 + op2[i]

    ans = list()
    sum = num1+num2
    while sum:
        ans.append(sum%10)
        sum //= 10

    ans = reversed(ans)
    return ans

if __name__ == '__main__':
 
    # input lists
    op1 = [10, 2, 3]
    op2 = [4, 5, 6]

    ans = listAdder(op1, op2)
    for i in ans:
        print(str(i) + " ")

    print("\n")