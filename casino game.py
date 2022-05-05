def main():
    balanceamt = None
    amt = None
    no = None
    dice = None
    playername = str(['\0' for _ in range(80)])
    ch = None
    clrscr()
    Globals.draw_line(60, '=')
    print("\n\n\n\n\t\tCASINO GAME\n\n\n\n", end = '')
    Globals.draw_line(60, '=')
    print("\n\n\nEnter Your Name  :", end = '')
    gets(playername)
    print("\n\n\Enter Deposit amount to play game :", end = '')
    cin>> balanceamt
    condition = True
    while condition:
        clrscr()
        Globals.rules()
        print("\n\nYour current balance is Rs.", end = '')
        print(balanceamt, end = '')
        condition = True
        while condition:
            print("\n\n", end = '')
            print(playername, end = '')
            print(" enter money to bet", end = '')
            cin>> amt
            if amt> balanceamt:
                print("Your betting amount is more than your current balance\n\nRe-enter data\n ", end = '')
            else:
                break
            condition = 1
        condition = True
        while condition:
            print("Enter your lucky number to bet between 1 to 12 :", end = '')
            cin>> no
            if no<=0 or no>12:
                print("Please check the number!! should be between 1 to 12\n\nRe-enter data\n ", end = '')
            else:
                break
            condition = 1
        randomize()
        dice = random(12)+1
        if dice == no:
            print("\n\nGood Luck!! You won Rs.", end = '')
            print(amt *10, end = '')
            balanceamt = balanceamt+amt *10
        else:
            print("Bad Luck this time !! You lose Rs.", end = '')
            print(amt, end = '')
            balanceamt = balanceamt-amt
        print("\n\nThe winning number was : ", end = '')
        print(dice, end = '')

        print("\n\n\t", end = '')
        print(playername, end = '')
        print(" You have Rs. ", end = '')
        print(balanceamt, end = '')
        print("\n", end = '')
        print("\n\n-->Do you want to play (y/n)? ", end = '')
        cin>> ch
        condition = ch == 'Y' or ch == 'y'
    clrscr()
    print("\n\n\n", end = '')
    Globals.draw_line(70, '+')
    print("\n\n\t\THANKS FOR COME TO CASINO YOUR BALANCE AMOUNT IS RS.", end = '')
    print(balanceamt, end = '')
    print("\n\n", end = '')
    Globals.draw_line(70, '+')
    print("\n\nGame developed by ANIKET RAJPUT\n", end = '')
    Globals.draw_line(70, '+')
    getch()
