text = "This is imutable!"
print(text[5:7])

text = text[:5]+"blah"+text[7:] #This makes a new string in memory, constructed from pieces of the previous sentance. 
print(text)