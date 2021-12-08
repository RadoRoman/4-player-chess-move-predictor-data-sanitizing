def merge_game_nr():
    # Creating a list of filenames
    filenames = ['data/gameNr_solo.txt', 'data/gameNr_ffa.txt']

    # Open file3 in write mode
    with open('data/mergedGameNr.txt', 'a+') as outfile:
        # Iterate through list
        for names in filenames:
            # Open each file in read mode
            with open(names) as infile:
                # read the data from file1 and
                # file2 and write it in file3
                outfile.write(infile.read())

            # Add '\n' to enter data of file2
            # from next line
            outfile.write("\n")

    with open('data/mergedGameNr.txt', 'r') as f1, open('../data/merge_game_nr.txt', 'w') as f2:
        # first get all lines from file
        lines = f1.readlines()

        # remove spaces
        lines = [line.replace(' ', '') for line in lines]

        # finally, write lines in the file
        f2.writelines(lines)
            #f2.write(re.sub(r"^\s+|\s+$", "", line), sep='')

merge_game_nr()
