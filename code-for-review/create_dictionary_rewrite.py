def create_dictionary(input1, input2, output):
    # step 1
    file1 = open(input1, 'r')
    file2 = open(input2, 'r')

    # step 2
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    file1.close()
    file2.close()

    # step 3, 4
    if len(lines1) != len(lines2):
        return "Fail Message"
    
    # step 5
    output_file = open(output, 'w')
    for i in range(len(lines1)):
        output_file.write("{}:{}\n".format(lines1[i].rstrip(), lines2[i].rstrip()))

    output_file.close()
    return "Success Message"

print(create_dictionary('a.txt', 'b.txt', 'a-b.txt'))
print(create_dictionary('a.txt', 'c.txt', 'a-c.txt'))
