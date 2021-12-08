def parse_game_nr():
    with open('solo.txt', 'r') as f1, open('data/test.txt','a') as f2:
        for i in f1:
            x= f1.readline(17)
            y= x.split("][")
            str1= str(y)[1:-1]
            str2 = str1[1:-1]
            new = str2.replace('GameNr', '')
            new1 = new.replace('[', '')
            new2 = new1.replace(']', '')
            new3 = new2.replace('"', '')

            if not new3.strip():
                continue
            if new3:
                f2.write(new3 + '\n')

parse_game_nr()
