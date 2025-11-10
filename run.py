import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x jfg')
    os.system('./jfg')
elif bit == '32bit':
    os.system('chmod +x jfg32')
    os.system('./jfg32')
else:
    print('device not supported')
