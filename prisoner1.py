from random import shuffle
def find_num():
    boxes = {}
    nums = [i for i in range(1, 101)]
    shuffle(nums)
    for i, num in enumerate(nums):
        boxes[i + 1] = num
    for prisoner in range(1, 101):
