text = '1+2+3+4+5'
result = text.split('+')
print(result)

line_of_data = "123.4, August Earning, 123456"
element = line_of_data.split(',')
print(element)
elements_formated = [float(element[0]), element[1].strip(), int(element[2])]
print(elements_formated)

tab_delimited = '12.3\tAugust Earnings\t12345'
print(tab_delimited)
elements_from_tab = tab_delimited.split('\t')
print(elements_from_tab)

simple_text = "This is a sentence"
simple_text_words = simple_text.split()
print(simple_text_words)