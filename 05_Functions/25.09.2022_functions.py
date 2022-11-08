import math

golosni = ("aeuio")
alphabet = ("qwertyuioplkjhgfdsazxcvbnmASFDHQYERIOPLMNBVCZXHgsyeoiwekdfds")
def count_golosni():
    print("Golosnih: ", sum(map(alphabet.count, golosni)))
count_golosni()

#----------------------------------------------

text = ( " Don’t let the noise of others’ opinions drown out your own inner voice. " )
author = "Steve Jobs"
probel = ' '
def formatted_text():
    halftext = text.split()
    first = math.ceil((len(halftext)//2)+1)
    print('"', " ".join(halftext[:first]), "\n", " ".join(halftext[first:]),'"', "\n", 29*probel, author)
formatted_text()

#----------------------------------------------

number = input("Enter 6 digit number:")
def lucky_number(number):
    a = [int(i) for i in number]
    if sum(a[:3]) == sum(a[3:]):
        print("Lucky number")
    else:
        print("Unlucky number")
lucky_number(number)