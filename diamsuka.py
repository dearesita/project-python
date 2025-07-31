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
    time.sleep(delay)
    animate_text(lyric, speed)
    
def sing_song():
    lyrics = [
        ("Dan sebenarnya aku tak diam", 0.08),
        ("Seraya perhatikan jejak langkahmu", 0.10),
        ("Walau terlihat diriku", 0.20),
        ("Tak'da di dekatmu", 0.13),
        ("Semakin kau indah", 0.13),
        ("Memperjelas setiap kelemahanku", 0.12),
        ("Walau kau berharga", 0.13),
        ("Sekarang bukan untuk berdua", 0.20)
    ]
    
    delays = [0.7, 4.2, 8.5, 14.3, 17.2, 19.3, 23.0, 27.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        if i < len(delays):
            t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
            threads.append(t)
            t.start()
        
    for t in threads:
        t.join()
    
if __name__ == "__main__":
    sing_song()