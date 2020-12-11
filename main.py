from pynput.keyboard import Listener
import os
def on_press(key):
    try:
        print(str(key.char),end="",flush=True)
    except AttributeError:
        print(" "+str(key).split(".")[1],end=" ",flush=True)
def start_listen():
    os.system('clear') # clean up the terminal
    with Listener(on_press=on_press) as listener:
        listener.join()
if __name__ == '__main__':
    start_listen()
