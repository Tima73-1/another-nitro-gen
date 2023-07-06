import random
import string

f = open('codes.txt', 'a')
print('How many codes?')
print ('')
amount = int(input(">"))
print ('')
print ('Generating')
print ('')

fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discordapp.com/gifts/"
    f.write("https://discordapp.com/gifts/" + code + '\n')
    discord_code = discord_url + code
    print('Link: ' + discord_code)
    fix += 1
print ('\nMost of codes are not working. Try all of generated codes, maybe you get working code!')
print("Press Enter to exit")
input()