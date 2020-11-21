import hashlib # For SHA-256
import random # For the random DH parameters
import string # Encode


def first_10_set(hash_bytes):
    set_bits = [] * 10
    count = 0

    to_test = int.from_bytes(hash_bytes, 'big')

    while(count < 10):
            
        set_bits.append(to_test & 1)
        to_test >> 1
        count += 1
    
    for bit in set_bits:
        if bit != 0: return -1

    return 1

# Returns a nonce with
# the first 10 bits set
#######################
def gen_proof_of_work(quote_bytes, prev_hash):
    
    running = prev_hash
    nonce = 0

    ten_set = 0

    random.seed()
    
    while ten_set == 0:
        nonce = random.randint(1023, 2147483647)
        running += nonce.to_bytes(4, 'big') # not right
        running += quote_bytes

        running = hashlib.sha256(running).hexdigest()

        if first_10_set(bytearray.fromhex(running)): 
            ten_set = 1
       

    print(running)
    return nonce

def main():

    quote = "This is my quote"
    quote = quote.encode()

    prev_hash = b"old hash"

    print(gen_proof_of_work(quote, prev_hash))

    return 0

if __name__ == "__main__":
    main()