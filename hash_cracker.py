import hashlib

file_name = "wordlist.txt"
target_hash = "124ef0adfe8381a3a87420423bf8113954b7e06090583470136c20dd7d907e0b"

try:
    with open(file_name, "r") as wordlist:
        content = wordlist.read().split()
        print(f"Wordlist loaded. Total words: {len(content)}")
except FileNotFoundError:
    content = []

def hash_cracker():
    found = False
    for word in content:
        hashed_value = hashlib.sha256(word.encode()).hexdigest()

        if hashed_value == target_hash:
            found = True
            print(f"Match found! The password is: {word}")
            break
            
    if not found:
        print("Password not found in the wordlist.")

if content:
    hash_cracker()
