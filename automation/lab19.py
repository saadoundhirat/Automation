from faker import Faker
import re
import shutil

## read the file data from the file "contacts"

# filename variables
filename = 'file.txt'
newfilename = 'result.txt'

# read the file
if os.path.exists(filename):
        data = open(filename,'r')
        bulkemails = data.read()
else:
        print "File not found."
        raise SystemExit

# regex = something@whatever.xxx
r = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
results = r.findall(bulkemails)
emails = ""
for x in results:
        emails += str(x)+"\n"

# function to write file
def writefile():
        f = open(newfilename, 'w')
        f.write(emails)
        f.close()
        print ("File written.")