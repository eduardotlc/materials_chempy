import binascii

# Load the contents of both files
with open("/home/eduardotc/ghidra/AuNd_Chloroform_650.txt", "r") as text_file:
    text_data = text_file.read()

with open("/home/eduardotc/ghidra/AuNd_Chloroform_650.FS", "rb") as hex_file:
    hex_data = hex_file.read()



# Step 2: Try to XOR the hex-encoded data with the text data
decoded_data = []
for i in range(len(hex_data)):
    xor_result = hex_data[i] ^ ord(text_data[i])
    decoded_data.append(xor_result)

# Step 3: Convert the decoded data to a readable text format
try:
    decoded_text = "".join(chr(x) for x in decoded_data)
    print("Decoded text:", decoded_text)
except Exception as e:
    print("Unable to decode using XOR:", e)
    exit()

# Step 4: Analyze the decoded text
# You can now analyze the decoded text to see if it makes any sense. You might need to perform additional steps
# like frequency analysis, pattern recognition, or trying different encodings to get meaningful data.

# For example, you can analyze the frequency of characters in the decoded text to look for patterns.

def character_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

decoded_text_freq = character_frequency(decoded_text)
print("Character frequency in decoded text:")
print(decoded_text_freq)

# Step 5: Further analysis
# Depending on the results of the initial analysis, you may need to try different techniques or encodings to fully
# decode the data.

# Step 6: Iterate and refine
# Continue to iterate and refine your analysis and decoding techniques until you obtain meaningful results.

# Remember that breaking an unknown encoding can be a complex and time-consuming process, and success is not guaranteed. This script provides a basic starting point for analysis and experimentation.

