# File Encryption Tool

This Python program reads text from an input file, encrypts it using a predefined encryption dictionary, and writes the encrypted text to an output file. It retains spaces in the input and replaces other characters based on the encryption key.

---

## **Features**
1. **Custom Encryption Dictionary**:
   - The program uses a dictionary that maps each character (letters, numbers, and symbols) to its encrypted counterpart.

2. **File Input and Output**:
   - Reads the content from a user-specified input file.
   - Writes the encrypted content to a user-specified output file.

3. **Character Handling**:
   - Encrypts characters that exist in the encryption dictionary.
   - Retains spaces and substitutes unsupported characters with a blank space (`' '`).

---

## **How to Run**

### **Requirements**
- Python 3.x
- Input and output files must be accessible in the working directory.

### **Steps**
1. Save the program as `file_encryption_tool.py`.
2. Place the input file in the same directory as the program or provide the full path.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the program.
5. Run the program:
   ```bash
   python3 file_encryption_tool.py
