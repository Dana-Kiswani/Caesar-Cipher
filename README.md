# *Caesar Cipher in Cryptography*

*by : Dana Kiswani*

*References* :
[Alphabet range in Python](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)

> ***The Caesar Cipher technique*** *is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.*

> *The science of writing secret codes is called `cryptography`. For thousands of years cryptography has made secret messages that only the sender and recipient could read, even if someone captured the messenger and read the coded message. A secret code system is called a cipher. The cipher used by the program in this chapter is called the Caesar cipher.*


***Feature Tasks and Requirements***

* *Create an `encrypt` function that takes in a plain text phrase and a numeric shift.*

  - the phrase will then be `shifted` that many letters.
    - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘acb’, 10) would return ‘klm’
  - shifts that exceed 26 should wrap around
    - E.g. encrypt(‘abc’,27) would return ‘bcd’
* *Create a `decrypt` method that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form* ***as long as correct key is supplied.***

* ***Break*** *the cipher so that an encrypted message can be transformed into its original state ***WITHOUT*** access to the key.*

* *Devise a method for the computer to determine if code was broken with minimal human guidance.*

> *Use `poetry` to create `caesar-cipher` project.*

