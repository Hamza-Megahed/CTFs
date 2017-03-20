#!/usr/bin/python

from subprocess import PIPE, Popen
import subprocess
import sys

def cmdline(command):
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return err

def combinations(words, length):
    if length == 0:
        return []
    result = [[word] for word in words]
    while length > 1:
        new_result = []
        for combo in result:
            new_result.extend(combo + [word] for word in words)
        result = new_result[:]
        length -= 1
    return result

def main():
    words = [line.strip() for line in open('/usr/share/wordlists/rockyou.txt')]
    s = b'writing RSA key\r\n';
    print("\n")

    res = combinations(words, 1)
    c = len(res)-1
    for idx, result in enumerate(res):
        str1 = "openssl aes-256-cbc -d -md sha256 -in /media/root/new/ToAlice.csv.enc -out /root/Desktop/ouut.txt -pass pass:"+result[0]
        if cmdline(str1) == "":
            print("\nKey Found! The key is: "+result[0])
            sys.exit()
        print(str(idx)+"/"+str(c))
    print("\n")
if __name__ == '__main__':
    main()
