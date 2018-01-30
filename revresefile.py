#python script to reverse the file 
#this is useful while doing CTF if a file is reversed
# Author solo2-0

file1 = open("evidence", "r")
inp = file1.read() #read the file 
rev = inp[::-1] # reverse it
out = open("output","w") 
out.write(rev) # write into new file

