# reviewing the week 7 lectures
# opening and working with files

#with open ( ".\lectureredo.txt", "w") as f:
 #   print ("fingers crossed")

with open ("Textfile", "rt") as f :
    data = f.read ()
    print (data)



with open ("Textfile", "rt") as f :
    data = f.read (4)
    print (data)