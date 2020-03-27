sh = input('enter your working hours: ')
sr = input('enter rate: ')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, plz enter numeric input')
    quit()

print(fh, fr)
if fh > 40 :
    print('Overtime')
    reg = fh * fr
    otp = (fh - 40)*(fr * 1.5)
#. print(reg,otp)
    xp = reg + otp
else:
    print('Regular')
    xp = fh * fr
print('pay: :', xp)