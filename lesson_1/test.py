import keyboard as keyboard


def control():
    global IsWork
    if IsWork:
        IsWork = False
        print("завершил")
    else:
        IsWork = True


keyboard.add_hotkey('a', control)

IsWork = False
while True:
    if keyboard.is_pressed("a"):
        while IsWork:
            print("работаю")
            time.sleep(1)