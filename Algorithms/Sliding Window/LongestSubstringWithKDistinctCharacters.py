def Longest_Substring_with_K_Distinct_Characters(string, k):
    window_start = 0
    max_length = 0
    char_freq = {}

    for window_end in range(len(String)):
        right_char = string[window_end]

        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
    
        while len(char_freq) > k:
            left_char +=
