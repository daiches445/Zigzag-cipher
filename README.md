# Zigzag-cipher

<h3>My solution to the Zigzag/Railfence cipher </h3>
<hr>
<h3>Description</h3>
the Railfence cipher is a classical type of transposition cipher.<br>
In the rail fence cipher, the plaintext is written downwards diagonally on successive "rails" of an imaginary fence, then moving up when the bottom rail is reached, down again when the top rail is reached, and so on until the whole plaintext is written out. The ciphertext is then read off in rows.<br>
<br>
For example, to encrypt the message 'WE ARE DISCOVERED. RUN AT ONCE.' with 3 "rails", write the text as:
<br>
W . . . E . . . C . . . R . . . U . . . O . . . <br>
. E . R . D . S . O . E . E . R . N . T . N . E <br>
. . A . . . I . . . V . . . D . . . A . . . C . 

(Note that spaces and punctuation are omitted.) Then read off the text horizontally to get the ciphertext:

WECRUO ERDSOEERNTNE AIVDAC <br>
