def longestPath(fileSystem):
    tokens = fileSystem.split("\f")
    print(tokens)
    
    if len(tokens) == 1:
        if "." in tokens[0]:
            return len(tokens[0])
        else:
            return 0

    cur_dir = [tokens[0]]
    longest = 0
    exp_lvl = 1
    for token in tokens[1:]:
        cur_lvl = 0
        for i in range(len(token)):
            if token[i:i+1] == "\t":
                cur_lvl += 1
            else:
                if cur_lvl == exp_lvl:
                    cur_dir.append(token[i:])
                    exp_lvl += 1
                else:
                    if "." in cur_dir[-1]:
                        temp_str = "/".join(cur_dir)
                        print(temp_str)
                        longest = max(longest, len(temp_str))
                    cur_dir = cur_dir[:cur_lvl]
                    cur_dir.append(token[i:])
                break
                    
    if "." in cur_dir[-1]:
        temp_str = "/".join(cur_dir)
        longest = max(longest, len(temp_str))
    
    return longest

