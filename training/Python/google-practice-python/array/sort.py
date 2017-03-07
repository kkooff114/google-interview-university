#  fast sort start
def partition(list, left, right):
    pivotKey = list[left]

    while left < right:
        print "=====%d====%d" %(left, right)
        print(list)
        while left < right and pivotKey <= list[right]:
            right -= 1

        list[left] = list[right]

        while left < right and pivotKey > list[left]:
            left += 1

        list[right] = list[left]

    list[left] = pivotKey

    return left


def fastSort(list, left, right):
    if(left >= right):
        return

    pivotPos = partition(list, left, right)

    fastSort(list, left, pivotPos -1)
    fastSort(list, pivotPos + 1, right)

#  fast sort end

if __name__ == "__main__":
    list = [1,2,3,5,3,9,3,1]
    fastSort(list, 0, len(list) -1)
    print(list)
