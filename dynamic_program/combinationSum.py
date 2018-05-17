def combinationSum(a, sum):
    a = sorted(set(a))    
    re = [[] for i in range(sum+1) ]
    
    for el in a:
        for i in range(el, sum+1):
            if i == el:
                re[i] += [[str(el)]]
            else:
                for com in re[i-el]:
                    re[i] += [com + [str(el)]]

    if not re[sum]:
        return "Empty"
    
    output = []
    for com in re[sum]:
        output += ["(" + " ".join(com) + ")"]
    return "".join(sorted(output))