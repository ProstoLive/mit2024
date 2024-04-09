def fib(n):
    fib_process = [0, 1]
    print(fib_process[0])
    print(fib_process[1])
    for i in range(n-2):
        res = fib_process[-1] + fib_process[-2]
        print(res)
        fib_process.append(res)



fib(int(input("Enter n:")))