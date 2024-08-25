# region Quest
#<p>Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.</p>
#<p>A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.</p>
#<p>For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.</p>
#<p>Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.</p>
#<p>Your task has been made easy, as the encryption key consists of three lower case characters. Using <a href="resources/documents/0059_cipher.txt">0059_cipher.txt</a> (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.</p>

# endregion

#ord('A')
#chr(107)

from itertools import combinations

def openTxt(filename):                      #### opens an txt-file and returns a list of the strings with lower cases and sorted
    with open(filename, 'r') as datei:
        return [wert for wert in datei.read().split(',')]

#### get CodeASCCI
CodeASCCI = []
for value in openTxt('0059_cipher.txt'):
    CodeASCCI.append(int(value))


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#### get ASCCI KEY 
for keyword in combinations(chars*3, 3):

    KeyASCCI = [ord(digit) for digit in keyword]*(int(len(CodeASCCI)/3))


    #### get TextASCCI
    TextRich = []
    ASCCIsum = 0
    for i in range(0,len(CodeASCCI)):
        TextASCCI = CodeASCCI[i]^KeyASCCI[i]
        ASCCIsum += TextASCCI
        TextRich.append(chr(TextASCCI))


    TextRichJoint = ''.join(TextRich)

    if " the " in TextRichJoint or " The " in TextRichJoint:
        print(f'\n{ASCCIsum}:\n {TextRichJoint}')
