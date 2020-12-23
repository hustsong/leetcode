def max_substr(a,  b):
    m, n = len(a), len(b)
    mtrx = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_len = 0
    max_str = ''
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a_c, b_c = a[i - 1], b[j - 1]
            if a_c != b_c:
                continue
            else:
                curr_substr_len = mtrx[i - 1][j - 1] + 1
                if curr_substr_len > max_len:
                    max_len = curr_substr_len
                    max_str = a[i - curr_substr_len:i]
                mtrx[i][j] = curr_substr_len

    return max_str


a = 'awfjawehfabcdefgrfhaaiaaavaf4'
b = 'zjrfoehjgq4ghrfhaa23rpjofnvahabcdefgw'
print(max_substr(a, b))
