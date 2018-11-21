def main():
    groupFlag  = False
    repFlag    = False
    group      = {}
    # Get name of input file.
    # Open the input file and read the text.
    input_file = open(r'C:\Users\grspence\Google Drive\HTC\CCIS1501-Fundamentals of Programming\Session 09 - Dictionaries and Sets\svn_access.txt', 'r')
    textLine = input_file.readline()
    while textLine != '':
        if '[groups]' in textLine:
            groupFlag = True
            textLine = input_file.readline()
            continue                          ## Skip to next iteration
        if r':/' in textLine:
            groupFlag = False
            repFlag   = True

        if groupFlag == True:
            words = textLine.split()
            if words != []:                  ##Blank line    - Ignore
                if words[0][0] != '#':       ##Comment lines - Ignore
                    group[words[0]] = words[2:]       ## Create dictionary entry for group and use list of userids
                   # print(words[0],group[words[0]])

        textLine = input_file.readline()


    # Create set of unique words. (Page 463 – use the words list!)
    # Close the file.
    input_file.close()

    for keys,values in group.items():
        print(keys, values)




# Call the main function.
main()
