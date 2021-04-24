def nextPermutation(nums):
        keep = True
        i = len(nums) - 2
        if len(nums) >= 2:
            while keep == True:
                temp = nums[i:] #look at i th index of list to last index of list(window). I will move start point of window to left sequentially.
                #if we have seen all part of the list and still keep == True, it implies that list is sorted in reverse(e.x. [4,3,2,1]) -> sort it and stop iterating
                if i < 0:
                    nums.sort()
                    keep = False
                #elif temp list is sorted in reverse order, there is nothing to change -> let's move window to left
                elif temp == sorted(temp, reverse = True):
                    i -= 1
                #if there is something to change.. 
                else:
                    del nums[i:]
                    a = temp.pop(0)
                    b = min([x for x in temp if x > a])
                    b_i = temp.index(b)
                    temp[b_i] = a
                    temp.sort()
                    nums.append(b)
                    nums = nums + temp
                    keep = False
        return nums
