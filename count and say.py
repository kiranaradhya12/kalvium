def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    prev_str = countAndSay(n-1)
    result = ""
    count = 1
    for i in range(len(prev_str)):
        # If the current digit is the same as the next digit
        if i < len(prev_str)-1 and prev_str[i] == prev_str[i+1]:
            count += 1
        else:
            # Append the count and digit to the result string
            result += str(count) + prev_str[i]
            count = 1
    return result
print(countAndSay(5))