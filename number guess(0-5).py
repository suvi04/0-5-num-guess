print("I can guess what number ur thinking of bw 0-5")
print("Lets start")
oen=input("Is ur no. even(e) or odd(o) or neither(n) ")
if oen =="n":
    print("your no. is **  ZERO  ** ")
if oen =="e":
    e_psq=input("Is the number a perfect square? y/n ")
    if e_psq=="y":
        print("your number is **  FOUR  **")
    if e_psq=="n":
        print("your number is ** TWO  **")
if oen=="o":
    o_psq=input("Is your number a perfect square ? y/n ")
    if o_psq=="y":
        print("your number is **  ONE  **")
    if o_psq=="n":
        fibo=input("Is your number part of the fibonacci series ? y/n ")
        if fibo=="y":
            print("your number is **  THREE  **")
        if fibo=="n":
            print("your number is ** FIVE  **")