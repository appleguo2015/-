import random
import time
print('\033[33mBy AppleGUO\033[0m')
def coin():
    good_result = input('good_result: ')
    bad_result = input('bad_result: ')
    print(f"\033[1mIf coin is face up, you {good_result}.\033[0m")
    print(f"\033[1mIf coin is back face up, you {bad_result}.\033[0m")
    time.sleep(0.5)
    print()
    for i in range(25):
        print("\r\033[33m0\033[0m",end="")
        time.sleep(0.08)
        print("\r\033[33m1\033[0m",end="")
        time.sleep(0.08)
    coin = random.randint(0,1)
    if coin == 1:
        print("\r\033[33m1\033[0m",end="\n")
        print("FACE UP!!!")
        time.sleep(0.08)
        print(f"\033[32mYou can {good_result}\(O v O)/\033[0m")
        time.sleep(0.08)
    elif coin == 0:
        print("\r\033[33m0\033[0m",end="\n")
        print("BACK FACE UP!!!")
        time.sleep(1)
        print(f"\033[31mYou must {bad_result}<(\ _ /)>\033[0m")
        time.sleep(1)
#bY aPpLEgUO
#aNtI-CoUNterFeItIng mARk