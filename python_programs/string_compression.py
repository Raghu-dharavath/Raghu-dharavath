def compress_string(s):
    if not s:
        return s
    compressed_string = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i]==current_char:
            count +=1
        else:
            compressed_string.append(current_char)
            compressed_string.append(str(count))
            current_char = s[i]
            count = 1

    compressed_string.append(current_char)
    compressed_string.append(str(count))
    compressed_string = ''.join(compressed_string)

    if len(compressed_string)<len(s):
        return compressed_string
    else:
        return s


my_string = 'aabbbcaaa'
result = compress_string(my_string)
print(result)