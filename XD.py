import os,time,platform,sys
os.system("xdg-open https://facebook.com/groups/peaky009/")
os.system('clear')
print('[>] Checking Updates')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
 print("Found 64 bit")
 time.sleep(0.5)
 import Ai
else:
 print('\033[1;31mOnly For 64 bit Device')
 sys.exit()
