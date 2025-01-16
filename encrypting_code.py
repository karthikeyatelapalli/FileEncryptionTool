# Encrypting code
# Description:
'''
This program specifies a function that reads text data from an input file, encrypts it with a
chosen encryption key, and then writes the result to an output file. The encryption code is a
dictionary that associates a sign with each letter and some characters. Each character in the
input file is iterated through by the function, which then writes the encrypted content to the
output file and, if the corresponding symbol from the encryption code is discovered, replaces
the original character with it.
'''
def encryption_file():
    # the alphabetic dictionary of the vocabulary used to create encryption

    Encryption_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
     'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
     'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
     'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
     'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
     'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
     'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
     'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
     'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
     '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
     '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
     '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
     ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
     "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
     '{':'[','[':'{','}':']',']':'}'}
     
    input_text_file = input("Enter the name of the input file (including the extension): ")
    output_text_file = input("Enter the name of the output file (including the extension): ")
    
    # Opens input text file for reading the file     
    with open(input_text_file, 'r') as input_text:
        contents = input_text.read()
    
    encrypted_content = ''
    # If a character appears in the Encrypt_Code dictionary, iterate through the input file's characters and encode it.

    for char in contents:
        if char in Encryption_Code:
            encrypted_content += Encryption_Code[char]
        else:
            # Retain the spaces by checking if the character is a space using isspace()
            if char.isspace():
                encrypted_content += char
            else:
                encrypted_content += ' '
    
    # Create an output file with the encrypted information in it.
    with open(output_text_file, 'w') as output_text:
        output_text.write(encrypted_content)

# Example of use:
encryption_file()
