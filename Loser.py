import os,platform
os.system('git pull')
LA=platform.architecture()[0]
if LA=="32bit":
    __import__("A32")
elif LA=="64bit":
    __import__("A64")