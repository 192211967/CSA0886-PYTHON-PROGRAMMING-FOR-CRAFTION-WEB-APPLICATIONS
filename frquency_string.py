def character_frequency(ip):
    frequency = {}
    for ch in ip:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    return frequency
ip = "hello world"
frequency = character_frequency(ip)
print(frequency)
