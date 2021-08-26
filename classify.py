#! python3
import os,sys,shutil,datetime

for file in os.listdir():
    if file == os.path.basename(sys.argv[0]):
        continue
    mtime = (datetime.datetime.fromtimestamp(os.path.getmtime(file)))
    dirdate = mtime.strftime('%Y%m%d')
    if not os.path.exists(dirdate) :
        os.makedirs(dirdate)
    if os.path.isdir(dirdate):
        shutil.move(file,dirdate)
    else :
        print (dirdate + 'is a file. Cannot create a directory')




