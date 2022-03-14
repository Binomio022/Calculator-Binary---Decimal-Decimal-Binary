import os
import sys

def system():
    my_os=sys.platform
    return my_os

def num(n):
    # define the number and separate it
    digits = [int(x) for x in str(n)]
    return digits

def around(digits):
    # turn around the arrays of digits
    anti_digits = digits[::-1]
    return anti_digits

def cal(anti_digits):
    # final result
    resul = 0
    # accountant for know what digit is the next
    cont2 = 0
    # accountant for know how much we have to multiply
    cont = 2
    for digit in anti_digits:
        # conditional for know if is a 0 or a 1, this is 0
        if digit == 0:
            # conditional for know if is the first number
            if cont2 == 0:
                resul = resul
            else:
                cont = cont * 2
        # conditional for know if is a 0 or a 1, this is 1
        elif digit == 1:
            if cont2 == 0:
                resul = resul + 1
            else:
                resul = resul + (cont * digit)
                cont = cont * 2
        else:
            resul = str("The number enter is not a binary")
        cont2 = cont2 + 1
    return resul

def end():
    # unify all last defs for know the result and printed
    return cal(around(num(int(input("Enter the number: ")))))

def bina(decimal):
    # define a empty variable
    binario = ""
    while decimal // 2 != 0:
        # put a 1 or a 0 depending on the remainder
        binario = str(decimal % 2) + binario
        # divides the number in 2
        decimal = decimal // 2
    # return the binary + the rest of the decimal that is always 1
    return str(decimal) + binario

#clear the cmd
if system() == "win32":
    os.system("cls")
else:
    os.system("clear")

print("Calculator Binary - Decimal & Decimal - Binary\n")
print("                 By Aphrodite")
print("    .___. ")
print("    {o,o} ")
print("    /)__) ")
print("    -\"-\"-")

# make a menu and take the option u want to use
print("What u want to make")
print("1 - Pass decimal to binary")
print("2 - Pass binary to decimal")
a = input()
#define the option
if a == "1":
    print("DECIMAL >>>>> BINARY")
    num = int(input("Enter the number: "))
    print("Your number is - "+bina(num))
elif a == "2":
    print("BINARY >>>>> DECIMAL")
    print("Your number is - "+str(end()))
else:
    print("That's not an option")