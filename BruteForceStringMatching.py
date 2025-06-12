def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1
if __name__ == "__main__":
    text = "hello world"
    pattern = "world"
    result = brute_force_string_match(text, pattern)
    
    if result != -1:
        print(f"Pattern found at index {result}")
    else:
        print("Pattern not found")