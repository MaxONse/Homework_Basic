wl = input("Enter text:").split()
wr = input(str.lower("Enter reserved words:")).split()
outlist = []
for a in wl:
    if a not in wr:
        outlist += [a]
    elif a in wr:
        outlist += [a.upper()]
    else:
        print("Typing ERROR")
        break
print(' '.join(outlist))

import time
print("There is some text.....")
time.sleep(3)
print("-------------------------------------------------")
mystr = str("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tempus et augue aliquet efficitur.\n"
            " Sed blandit quam nec est tempor lobortis. Sed malesuada ipsum quis viverra egestas. Nulla vitae augue\n"
            " viverra, faucibus mauris ut, aliquam metus. Aliquam sollicitudin, dui eget malesuada malesuada, risus\n"
            " nisl faucibus velit, vel pulvinar est eros vitae magna. Fusce et velit sed sem dapibus mattis. Morbi\n"
            " venenatis ut leo at venenatis. Curabitur volutpat venenatis quam, et sodales lacus semper sed. Praesent\n"
            " pharetra lacinia sodales. Etiam scelerisque massa lectus, ut interdum nisl porta vitae. Duis ultrices\n"
            " sollicitudin auctor. Nulla sit amet odio in nunc eleifend eleifend. Morbi pulvinar, erat sit amet\n"
            " condimentum eleifend, sapien dolor interdum lorem, non feugiat neque sapien id est. Nunc faucibus dolor\n"
            " ut eros faucibus, a rhoncus erat pretium. Donec molestie, libero quis viverra cursus, urna justo cursus\n"
            " velit, non tincidunt ipsum justo et sapien. Mauris sodales nisl ut ligula euismod tempor.")
print(mystr)
time.sleep(3)
print("-------------------------------------------------")
print("How many sentences do you think are in this text?")
time.sleep(3)
print("-------------------------------------------------")
print(" There is..........")
time.sleep(3)
print("-------------------------------------------------")
print(len([a for a in mystr.split('.')]))