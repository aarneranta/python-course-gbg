# https://www.youtube.com/watch?v=Ns4TPTC8whw
# sorterar listan m och retunerar därefter densamma.
def selection(m):
    for i in range(len(m)):
        min_index = i
        for j in range(i,len(m)):
            if m[j] < m[min_index]:
                min_index = j

        m[min_index], m[i] = m[i], m[min_index]
    return m

# https://www.youtube.com/watch?v=lyZQPjUT5B4
# sorterar listan m och retunerar därefter densamma.
def bubble(m):
    for _ in range(len(m)):
        for i in range(1,len(m)):
            if m[i-1] > m[i]:
                m[i-1], m[i] = m[i], m[i-1]
    return m

# uniq([1,3,2,2,3]) == [1,3,2]
def uniq(m):
    seen = []
    for n in m:
        if n not in seen:
            seen.append(n)
    return seen
