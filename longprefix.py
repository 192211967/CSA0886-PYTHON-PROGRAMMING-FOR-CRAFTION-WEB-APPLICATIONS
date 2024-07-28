def prefix(strs):
    if not strs:
        return ""
    min_length = min(len(s) for s in strs)
    lcp = ""
    for i in range(min_length):
        current_char = strs[0][i]
        if all(s[i] == current_char for s in strs):
            lcp += current_char
        else:
            break

    return lcp
print(prefix(["flower", "flow", "flight"]))
print(prefix(["dog", "racecar", "car"]))    
