import time
def animation(x = 10):
    for x in range(x):
        symbols = (chr(92), chr(124), chr(47))
        for y in symbols:
            print(y*3, end="\r")
            time.sleep(0.5)
            #print(chr(124)*3, end="\r")
            #time.sleep(0.5)
            #print(chr(47)*3, end="\r")
            #time.sleep(0.5)
    return()
animation()