
"""
Any character is entered through the keyboard, write a program to determine whether the character entered is a capital letter, 
a small case letter, a digit or a special symbol.
The following table shows the range of ASCII values for various characters.
"""

char=input("Enter the character : ")

if len(char) !=1:
    print("please enter only one character ")
else:
    ascii_value=ord(char)

    if 65 <= ascii_value <=90:
        print("capital letter")
    elif 95< ascii_value <=122:
        print("small letter ")
    elif 48 <ascii_value<=57:
        print("digit")
    else:
        print("special symbol ")