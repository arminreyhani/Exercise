import msvcrt
import time

counter = 1

print("Press the A key to stop the program")

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key == b'a' or key == b'A':
            print("\nThe A key was pressed, and the program stopped.")
            break
        else:
            print("\nWrong key. Press only the A key.")

    print(f"{counter}: The program is running...")
    counter = counter + 1
    time.sleep(1)