import hashlib
import smtplib

print("Hello to File Integrity Monitor, please enter the file path of the thing you want to monitor\n")
filePath = input("Enter file path(ex. /home/downloads/passwords):\n")

print("adding file:"+ filePath +" \n" )

def getHash(filePath):
    md5 = hashlib.md5()
    with open(filePath,'rb') as file:
        hash = file.read()
        md5.update(hash)
        return md5.hexdigest()

baseline = getHash(filePath)
print("[+] Just calculated your baseline Hash for %s" % filePath)
print("[+] File Integrity Checking Online ")


while True:
    check = getHash(filePath)
    if check != baseline:
        baseline = check
        print("[+] Someone edited the file")

