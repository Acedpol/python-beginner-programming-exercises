# ✅↓ Write your code here ↓✅
def estribillo(n):
    lyrics = ""
    for i in range(1,n+1):
        lyrics += "let it be,\n"
    return lyrics

def sing():
    lyrics = ""
    lyrics += estribillo(4)
    lyrics += "there will be an answer,\n"
    lyrics += estribillo(5)
    lyrics += "whisper words of wisdom, let it be"
    return lyrics

print(sing())

