# txt = "We are the so-called "Vikings" from the north."


# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

txt1 = 'It\'s alright'
print(txt1)

txt2 = "This will insert one \\ (backslash)."
print(txt2) 

txt3 = "Hello\nWorld!"
print(txt3) 

txt4 = "Hel\rloWorld!"
print(txt4) 

txt5 = "Hello\tWorld!"
print(txt5) 


#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
