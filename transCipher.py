# Transposition Cipher Encryption

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    
    ciphertext = encryptMessage(myKey, myMessage)
    
    print(ciphertext)

def encryptMessage(key, message):
    # Create the key size grid.
    ciphertext = [''] * key
    
    # Loop through each text column:
    for column in range(key):
        currentIndex = column
        
        # Keep looping through the message. Jump the index based on the keylength.
        while currentIndex < len(message):
            # Creating the ciphertext by placing the current index of the message and inserting it into the correct column.
            ciphertext[column] += message[currentIndex]
            # Move currentIndex over based on keylength.
            currentIndex += key

    # Converting the ciphertext list into a single string value.
    return ''.join(ciphertext)

main()