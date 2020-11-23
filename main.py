import hashlib # For SHA-256
import random # For the random DH parameters
import string # Encode


def first_10_set(hash_bytes):
 
    #print(hash_bytes.hex())
    for i in range(2):
        for j in range(8):
            #print("Checking " + str((hash_bytes[i] >> (7 - j)) & 1))
            
            if ((hash_bytes[i] >> (7 -j)) & 1) != 0:
                return -1

            if i == 1 and j == 1:
                return 1

# Returns a nonce with
# the first 10 bits set
#######################
def gen_proof_of_work(quote_bytes, prev_hash):

    nonce = 0
    ten_set = 0
    random.seed()
    
    while ten_set == 0:
        
        nonce = random.randint(1023, 2147483647)
        running = bytearray(0)
        running += prev_hash
        running += nonce.to_bytes(4, 'big')
        running += quote_bytes

        final = hashlib.sha256(running).hexdigest()
        
        if first_10_set(bytearray.fromhex(final)) == 1: 
            ten_set = 1

    print(final)
    return nonce

def main():

    quote = "Simple things should be simple. Complex things should be possible. -- Alan Kay"
    quote = quote.encode()

    prev_hash = bytearray.fromhex("0001104ff3d8167569a620c033ad4f728635490c6af84a7f7a1108bb68418f47")

    print ("Quote hex: " + quote.hex())
    print ("Prev Hash: " + prev_hash.hex())
    print(gen_proof_of_work(quote, prev_hash))

    return 0

if __name__ == "__main__":
    main()
