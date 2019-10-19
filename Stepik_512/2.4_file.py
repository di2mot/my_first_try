text = list()

with open('test.txt', 'r') as read_text, open('text_exit.txt', 'w') as write_text:
    for line in read_text:
        text.append(line)
    print(text)
    text.reverse()
    #text[0] = text[0] + '\n'
    write_text.write(''.join(text))