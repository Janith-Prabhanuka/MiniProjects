import os
os.chdir('D:\\Projects')
i=1
for file in os.listdir():
    src=file
    dst="2"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

