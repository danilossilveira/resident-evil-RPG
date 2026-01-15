import time

def averiguador():

    for i in range(10):
        
        print(f'Contando até {i}', end ='\r')
        if i == 10:
            print(f'TU É GAY', end ='\r')
        time.sleep(0.5)

def main():
    averiguador()

if __name__ == '__main__':
    main()
