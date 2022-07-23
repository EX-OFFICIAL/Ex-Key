import os
from time import sleep


a ='\033[92m'
b ='\033[93m'
c='\033[91m'
d ='\033[0m'
os.system('clear')
print(a+'\t  Extra Key Termux')
print(b+'\t    Mr. Ex')
print('\t https://t.me/itsmenoyon')
print(a+'_'*55)
print('\nProcessing..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Successfully !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN'],['python ','python2 ','.py','cd /sdcard','git clone ','nano ','exit']]"
control = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
control.write(key)
control.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !!')