num= (input('type random amount of letters and words but put spaces in the middle:'))

numb=[]
for word in num.split():
    if word.isdigit():
        numb.append(int(word))
print('so your numbers are ',numb)
