'''
Reading E-book
'''

print("*** Reading E-Book ***")
txt,highlight = input("Text , Highlight : ").split(",")
for i in range(len(txt)):
    if txt[i]==highlight:
        print("[{0}]".format(txt[i]),end="")
    else:
        print(txt[i],end="")

'''
*** Reading E-Book ***
Text , Highlight : ABAbaBab,b
ABA[b]aBa[b]
'''