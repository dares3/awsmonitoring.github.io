import ftplib
 
ftp = ftplib.FTP(host = "10.10.17.134", user = "bawean" ,passwd = "xxxxxx")
ftp.encoding = "utf-8"

home = ftp.pwd()
ftp.cwd('{}/data/'.format(home))

# Enter File Name with Extension
filename = "jumanji.txt"

# Read file in binary mode
with open(filename, "rb") as file:
	# Command for Uploading the file "STOR filename"
	ftp.storbinary(f"STOR {filename}", file)

ftp.quit()

