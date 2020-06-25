def create_dictionary(file1, file2, file_out):
    counter = 0
    counter2 = 0

    f1_in = open(file1, 'r')
    f2_in = open(file2, 'r')
    
    for line1 in f1_in:
        counter += 1

    for line2 in f2_in:
        counter2 += 1

    if counter != counter2:
        return "The input files are not compatible."

    else:
        with open(file1) as f1_in,\
             open(file2) as f2_in,\
             open(file_out, 'w') as file_out:

           
            xlines = f1_in.readlines()
            ylines = f2_in.readlines()
            
            for line1, line2 in zip(xlines, ylines):
                file_out.write("{}:{}\n".format(line1.rstrip(), line2.rstrip()))
        return "Successfully created file."
        
print(create_dictionary('english.txt', 'spanish.txt', 'english-spanish.txt')) # "Successfully created file.
print(create_dictionary('english.txt', 'korean.txt', 'english-korean.txt')) # "The input files are not compatible."