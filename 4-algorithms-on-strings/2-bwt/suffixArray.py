# python3
text = input()
suffix_arr = [[text[i:], i] for i in range(len(text))]
suffix_arr.sort(key = lambda x : x[0])

print(' '.join(str(y) for x, y in suffix_arr))
