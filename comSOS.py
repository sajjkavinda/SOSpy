import os, platform, subprocess
import datetime, time, sys, contextlib

print ("Platform:" + platform.platform())

a = platform.system()
#b = os.system('ls /Users/sajjkavinda')

if (a == "Darwin"):

    os.chdir("/Users/sajjkavinda/Downloads")
    #print (os.listdir())

    shell = subprocess.run(["ls" , "-l"])
    print (shell)

elif (a == "Windows"):
    file = open(r'C:\Users\Sajana\Desktop\entries_win.log', "w")
    #sys.stdout = open(r'C:\Users\Sajana\Desktop\entries_win.log', "w")
    x = datetime.datetime.now()
    timeW1 = x.strftime("%d" "-" "%b" "-" "%y")
    timeW2 = x.strftime("%I" ":" "%M" " " "%p")
    print(timeW1  + "\n" + timeW2 +"\n")
    file.write(timeW1  + "\n" + timeW2 +"\n")


    os.chdir(r"C:\\Windows\system32")

    #n = os.system('cmd /k "dir C:\Windows\system32\*.exe"')
    
    #print(n)
    
    #f1.write(os.system('cmd /k "dir C:\Windows\system32\*.exe"'))

    #with open (r'C:\Users\Sajana\Desktop\entries_win.log', "w") as f:
    #  with contextlib.redirect_stdout(f):
    #     os.system('cmd /k "dir C:\Windows\system32\*.exe"')

    det = os.popen('dir C:\Windows\system32\*.exe')
    
    for e in det:
        print(e)
        file.write(e)
    file.close()
    

    os.system('cmd /k "dir C:\\Windows\system32\*.exe"')

elif (a == "Linux"):

    os.chdir(r"/usr/lib")
    shell = subprocess.run(["dir", "/usr/lib/*.bin"])
    print (shell)
