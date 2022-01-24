command = ""
while command != "quit":
    command = input(">").lower()
    if command == "start":
        print("the car started")
        if command == "stop":
            print("the car has stopped")
            if command == "help":
               print("""
               start - start the engine
               stop - stop the engine
               quit
               """)
else:
    print("quit = break")


