import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print() 
        
def sing_lyric(lyric, delay, speed):
    time.sleep(delay)  # Wait for the specified delay before singing the lyric
    animate_text(lyric, speed)  # Animate the text with the specified speed
    
def sing_song():
    lyrics = [
        ("\nBukan kar'na makeup di wajahmu", 0.09),
        ("Atau lipstik merah itu (di bibirmu)", 0.09),
        ("Lembut hati tutur kata", 0.08),
        ("Terciptalah cinta yang kupuja", 0.10),
        ("Tak peduli langit menertawakanku", 0.09),
        ("Kau mencuri mencuri hatiku, mimpiku, semua rinduku", 0.12),
        ("Kar'na kamu cantik", 0.09),
        ("'Kan kuberi s'galanya apa yang kupunya", 0.09),
        ("Dan hatimu baik", 0.10),
        ("Sempurnalah duniaku saat kau di sisiku\n", 0.10),
    ]
    
    delays = [0.3, 3.4, 7.4, 10.5, 14.5, 18.0, 21.9, 24.4]
    
    threads = []  # Corrected variable name
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)  # Append to the correct list
        t.start()
        
    for t in threads:  # Use the correct variable name
        t.join()  # Wait for all threads to finish
        
if __name__ == "__main__":
    sing_song()