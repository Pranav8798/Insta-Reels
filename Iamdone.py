import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

def type_text(text, speed=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

lyrics = [
    "I am done..... 🥀",
    "Dil Mein Ab Koi Khayal Bhi Nahin Hai",
    "Tere Jaane Ka Malaal Bhi Nahin Hai",
    "Muntazir Main Tha Jo Tere Aane Ka",
    "Ab Toh Tera Intezaar Hi Nahin Hai",
    "Mann Mein Mere Ab Sawaal Hi Nahin Hai",
    "Hua Ye Koyi Kamaal Hi Nahin Hai",
    "Jeet Gaya Tujhe Bhool Kar Main Aise Jaise",
    "Zindagi Mein Koi Haar Hi Nahin Hai",
    "Ab Toh Tera Intezaar Hi Nahin Hai",
    "Ab Toh Tera Intezaar Hi Nahin Hai",
    "I AM DONE 💔"
]

delays = [1,1.2,1.4,1.3,1.2,1.3,1.2,1.4,1.2,1.1,1.1,2]

type_text("I AM DONE // @ranav.learning\n", 0.08)
time.sleep(1)

for i, line in enumerate(lyrics):
    type_text(line, 0.06)
    time.sleep(delays[i])
