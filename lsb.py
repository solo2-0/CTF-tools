#Image file is LSB are flipped with ascii data and converted to pixels again 
#This script will revert that operation and print the ascii 
#Author solo2-0



from PIL import Image
import re
def lsb(value):
	return str(bin(value))[-1] #return the string binary value that is present at that pixel value. 

def binToAscii(binary): #here the re is to find all 8 bit length binary divisions.
	return ''.join(chr(int(byte, 2)) for byte in re.findall(8*'.',binary)) # this is just opposite of the Ascii to bin funct

def extract(img):
	# Header and trailer are used to identify start and end of data to be extracted known from the encrypt file..
	header, trailer = 2*"11001100",2*"0101010100000000"
	binary, data = "", "" #Empty strings
	pixels, mode = list(img.getdata()), img.mode # This will give the list of RGB pixel values. 
	flag=False
	#print list(img.getdata())
	#print img.mode

	for i in range(len(pixels)):
		binary += lsb(pixels[i][i%len(mode)]) #append the least significant bit is parsed because it was tampered.
		#print len(mode) 
		if not flag and len(binary) == len(header): # if the binary and  the header then nothing is present in the lsb pixel data.
			if binary != header:
				print "Null"
				break
			else:
				flag,binary = True,"";
		if binary.endswith(trailer):
			print " Data extracted: "
			break
	
	data = binToAscii(binary)[:-4] # else convert the binary data added to the empty string to Ascii which will give the result.
	#print data
	return data
	#return binary

	

def main():
	img=Image.open("Secret.png") # Image is a module present in the pill library and this can be used to red the image files.
	print extract(img) # calling the function extract  and passing the value as image file.

if __name__ == "__main__":
	main()
	


		
	
