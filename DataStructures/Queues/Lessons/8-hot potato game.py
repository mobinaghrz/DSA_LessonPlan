def main():
    print("first name takes potato and starts the game.")
    que = input("Enter players name in white space as delimeter: ").split(" ")

    while len(que) != 1:
        counter = int(input("enter counter: "))

        for _ in range(counter):
            dequeued_player = que.pop(0)
            que.append(dequeued_player)

        print(f"{que.pop(0)} got hot potato")

    print(f"last person standing: {que[0]}")

if __name__ == "__main__":
    main()