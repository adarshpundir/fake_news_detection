csv_file = input()
txt_file = input()

try:
    my_input_file = open(csv_file, "r")
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

if not my_input_file.closed:
    text_list = [];
    for line in my_input_file.readlines():
        line = line.split(",", 1)
        text_list.append(" ".join(line))
    my_input_file.close()

try:
    my_output_file = open(txt_file, "w")
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

if not my_output_file.closed:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')
    my_output_file.close()
