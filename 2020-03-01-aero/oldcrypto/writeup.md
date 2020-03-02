# Old Crypto (100)

AES ECB encryption breaks plaintexts in 16 character chunks and encrypts them with a magic function. If any 16 character chunks are the same, they will encrypt to the same thing, which is where this cipher's flaw lies.

The server in this problem is given in main.py. The only relevant function is get_server_secret. It allows the user to concatenate a string to a secret, which gets encrypted by AES ECB.

To discover the first bit, we need to send a string of `'a' * 15 + random bit + 'a' * 15`. The reason is once the function concatenates the secret to that, AES ECB will divide the string into 16 chunks. Therefore, if we hit a correct random bit, we will get `('a' * 15 + first_bit) + ('a' * 15 + first_bit) + secret's[second_bit:last bit]` encrypted, and the resulting ciphertext's first two 16 chunk blocks will be the same.

There were some eventual nuances in this problem. Eventually, if we want to discover the second block, we need to use the discovered first block as part of evil string. You can't just pad the offset with a's. In addition, the flag length isn't perfectly divisible by 16. Finally, the server dropped connection strings every now and then so I had to use an infinite loop trick. You can read the code to pretty easily figure out what I did in each case.

This problem was identical to Cryptopals 12.

