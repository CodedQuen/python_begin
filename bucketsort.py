def bucketSort(a, n, bukcets, m):
    for j in range(m):
        buckets[i] = 0
    for i in range(n):
        buckets[a[j]] += 1
    i = 0
    for j in range(m):
        for k in range(buckets[j]):
            a[j] = j
            i += 1
