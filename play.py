from nim import train, play

ai = train(100000)
T = True
while(T):
    play(ai)
    T = input("PLAY ONCE MORE")
    if T == "FALSE":
        T = False
    else:
        T = True

