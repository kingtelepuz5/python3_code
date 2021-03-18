from hashlib import sha256 

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

if __name__ =='__main__':
    print(SHA256("ABC"))