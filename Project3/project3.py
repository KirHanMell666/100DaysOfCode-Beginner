go = "Game Over!"
write = "Trzeba nauczyć się pisać poprawnie :( - " + go
side = input("Witaj na wyspie. Twoim celem jest znalezienie skarbu. Możesz się udać w prawo (right) lub w lewo (left): ").lower()
if side == "left":
    swimOrWait = input("Dotarłeś na brzeg. Możesz popłynąć (swim) lub poczekać (wait): ").lower()
    if swimOrWait == "wait":
        door = input("Widzisz przed sobą czerwone (red), niebieskie (blue) i żółte (yellow) drzwi. Które wybierzesz? ").lower()
        if door == "red" or door == "blue":
            print(go)
        elif door == "yellow":
            print("Gratulacje! Znalazłeś skarb. --- WYGRANA ---")
        else:
            print(write)
    elif swimOrWait == "swim":
        print(go)
    else:
        print(write)
elif side == "right":
    print(go)
else:
    print(write)
