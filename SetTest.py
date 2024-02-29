# Challenge: write a function merge_arrays(), that takes two lists of integers as inputs,
#           combines them, removes duplicates, sorts the combined list and returns it


def merge_array(arrayA, arrayB):
    return sorted(set(arrayA + arrayB))  #sorted function return any iterable into List

    # arrayD = list(set(arrayA + arrayB))
    # arrayE = sorted(arrayD)
    # return arrayE

def test():
    tests = {
        1: [1,2,3,4,5] == merge_array([5,1,2,3], [1,4,3,1]),
        2: [3,4,5] == merge_array([5,4,3], [5,4,3]),
        3: [2,7,11] == merge_array([2,2,2,2], [7,11])
    }

    if all(tests.values()):
        print('Tests passed!')
    else:
        print('Tests failed!')


if __name__ == '__main__':
    test()
 