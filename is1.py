# Program to store the string "helloworld" and perform logical operations
# like AND, OR, and XOR between each character of the string and 127.

str1 = "helloworld"  # Make sure the string matches the desired input

for ch in str1:
    s1 = ord(ch) & 127
    s2 = ord(ch) | 127
    s3 = ord(ch) ^ 127

    print(f"{ch} & 127 : {chr(s1)}\t"
          f"{ch} | 127 : {chr(s2)}\t"
          f"{ch} ^ 127 : {chr(s3)}")
