import random
import string
def passwordgen():
    for i in range (8):
        a= ''.join([random.choice(string.ascii_letters + string.digits + "!@#$%^&*()?]") for n in range(8)])
    print (a)
    return 


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
