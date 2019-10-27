# inp_text = 'ababac'
# repl_in ='ab'
# repl_on = 'ba'
inp_text = str(input())
repl_in = str(input())
repl_on = str(input())

for i in range(1001):
    if i == 1000:
        print('Impossible')
        break
    else:
        if repl_in in inp_text:
            inp_text = inp_text.replace(repl_in, repl_on)
        else:
            print(i)
            break

