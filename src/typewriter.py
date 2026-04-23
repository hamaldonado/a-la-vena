import time
import playsound


def main():
    text = "Capítulo 1: El Inicio."

    for letter in text:
        
        playsound.playsound("src/sounds/keystroke_02.mp3", 
                            block=False)
        
        print(letter, end="", flush=True)
        time.sleep(0.20)

    print("")


if __name__ == "__main__":
    main()


