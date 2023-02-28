import random
import string
import os

def text():
    print(""">
>                Saintt
> $$\   $$\ $$\   $$\ $$$$$$$\  $$$$$$$\  
> $$ |  $$ |$$ |  $$ |$$  ____| $$  ____| 
> $$ |  $$ |$$ |  $$ |$$ |      $$ |      
> $$$$$$$$ |$$$$$$$$ |$$$$$$$\  $$$$$$$\  
> \_____$$ |\_____$$ |\_____$$\ \_____$$\ 
>       $$ |      $$ |$$\   $$ |$$\   $$ |
>       $$ |      $$ |\$$$$$$  |\$$$$$$  |
>       \__|      \__| \______/  \______/ 
>    """)

def menu():
    os.system("cls||clear")
    text()
    print(""">
> [1] String Generator
> [2] Class Generator 
> [3] Full Stack Generator(soon)
>   """)
    secim = int(input("> "))
    if secim == 1:
        os.system("cls||clear")
        text()
        print("> How Many Random Strings Should Be Created")
        sayi = int(input("> "))
        os.system("cls||clear")
        stringgen(sayi)
        input("\n> Press enter to return to the main menu...")
        menu()
    elif secim == 2:
        os.system("cls||clear")
        text()
        print("> How Many Random Classes Should Be Created")
        sayi = int(input("> "))
        os.system("cls||clear")
        classgen(sayi)
        input("\n> Press enter to return to the main menu...")
        menu()
    else:
        os.system("cls||clear")
        text()
        print("> Looks like you made the wrong choice.")
        input("> Press enter to return to the main menu")
        menu()


def string1():
    base = "var"
    intt = random.randint(99999999,9999999999999)
    asciistr = ''.join(random.choice(string.ascii_letters) for x in range(35))
    print(f"{base} {asciistr} = {intt};")


def string2():
    base2 = "var"
    intt2 = random.randint(99999999,9999999999999)
    intt3 = random.randint(99999999,9999999999999)
    intt4 = random.randint(99999999,9999999999999)
    asciistr2 = ''.join(random.choice(string.ascii_letters) for x in range(35))
    print(f"{base2} {asciistr2} = {intt2} == {intt3} + {intt4};")

def stringgen(adet):
    for i in range(adet):
        strings = ["string1()", "string2()"]
        stringsayi = random.randint(0,1)
        exec(strings[stringsayi])


def classgen(adet):
    for i in range(adet):
        main = "public class"
        main2 = "void"
        classascii = ''.join(random.choice(string.ascii_letters) for x in range(35))
        voidascii = ''.join(random.choice(string.ascii_letters) for x in range(15))
        strascii1 = ''.join(random.choice(string.ascii_letters) for x in range(50))
        strascii2 = ''.join(random.choice(string.ascii_letters) for x in range(50))
        strascii3 = ''.join(random.choice(string.ascii_letters) for x in range(50))
        strascii4 = ''.join(random.choice(string.ascii_letters) for x in range(50))
        a = "{"
        b = "}"
        symb = ["+","-","="]
        symbsayi = random.randint(0,2)
        randsymb = symb[symbsayi]
        print(f'{main} {classascii}{a}\n     {main2} {voidascii}(){a}\n          string {strascii1} = "{strascii2}";\n          string {strascii3} {randsymb} {strascii4};\n   {b}\n{b}')
menu()