def run():

    squares = {}
    for i in range(1, 101):
        if i%3 != 0:
            squares[i]=i**3

    print(squares)

if __name__ == '__main__':
    run()   