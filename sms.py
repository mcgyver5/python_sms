zero = ['0',' ']
one = ['.',',','\'','?','!','-','(',')','@','/',':']
two = ['a','b','c','2']
three = ['d','e','f','3']
four = ['g','h','i','4']
five = ['j','k','l','5']
six = ['m','n','o','6']
seven = ['p','q','r','s','7']
eight = ['t','u','v','8']
nine = ['w','x','y','z','9']
star = ['@','//',':','_',';','+','&','%','*','[',']','{','}']
command = [' ',' ']
keymap = {'1':one,'2':two,'3':three,'4':four,'5':five,'6':six,'7':seven,'8':eight,'9':nine,'0':zero,'*':star,'c':command}
"""

#define N7110_KEYPAD_ZERO_ABC_CHARS  " 0"
#define N7110_KEYPAD_ONE_ABC_CHARS   ".,'?!\"1-()@/:"
#define N7110_KEYPAD_TWO_ABC_CHARS   "abc2"
#define N7110_KEYPAD_THREE_ABC_CHARS "def3"
#define N7110_KEYPAD_FOUR_ABC_CHARS  "ghi4"
#define N7110_KEYPAD_FIVE_ABC_CHARS  "jkl5"
#define N7110_KEYPAD_SIX_ABC_CHARS   "mno6"
#define N7110_KEYPAD_SEVEN_ABC_CHARS "pqrs7"
#define N7110_KEYPAD_EIGHT_ABC_CHARS "tuv8"
#define N7110_KEYPAD_NINE_ABC_CHARS  "wxyz9"
#define N7110_KEYPAD_STAR_ABC_CHARS  "@/:_;+&%*[]{}"
#define N7110_KEYPAD_HASH_CHARS N7110_IME_METHODS

"""

fh = open("sms3.csv")

kpress = ''
old_value = ''
curr = ''
old_stamp = 0
timestamp = 0

for line in fh:
    line = line.strip()
    values = line.split(",")
    timestamp = int(values[0])
    kpress = values[1]
    if kpress == '10':
        kpress = '*'
    if int(kpress) > 12:
        kpress = 'c'
    print(timestamp - old_stamp)
    timediff = timestamp - old_stamp
    #if diff > 700, assume it is a new character
    if timediff < 700 and kpress == old_value:
        #still part of same character
        curr = curr + kpress
    else:
        keychar = curr[0]
        i =  len(curr)
        c = keychar[i]
        curr = kpress
    print(curr)
    old_stamp = timestamp
    old_value = kpress

