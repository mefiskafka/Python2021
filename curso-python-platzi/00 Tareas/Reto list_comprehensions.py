def run():

    squares = [i for i in range(1, 1000000) if i%36==0 and len(str(i))<6]

    print(squares)

if __name__ == '__main__':
    run()   

