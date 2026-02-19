import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: " + str(count) + "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)


answer = input("Do yo want to exit")
