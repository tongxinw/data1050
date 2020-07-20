def insertion_sort(a):
    i = 1
    while i < len(a):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            j = j - 1
        i = i + 1
    return a


def test_insertion_sort():
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([6,5,3,1,8,7,2,4]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert insertion_sort([0,0]) == [0,0]
    print("All tests pass!")
test_insertion_sort()
