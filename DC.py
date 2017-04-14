############## This is the Divide And Conquer Algorithm we were working on...without using the classes I used in the Menu and other files



def findMinAndMax(n, i, j, min, max):
    #i = int(i)
    #j = int(j)
    ################### checks to see if i = j (same spot in list)
    if i == j:
        max = n[i]
        min = n[i]
    ################### checks to see if i and j are next to each other (list has been broken down into a pair)
    elif (i == (j - 1)):
        if n[i] <= n[j]:
            max = n[j]
            min = n[i]
        else:
            max = n[i]
            min = n[j]
    else:
        # if n is not small enough, divide until smaller
        mid = int((i + j)/2)
        midPoint = int(mid + 1)
        max1 = n[midPoint]
        min1 = n[midPoint]
        findMinAndMax(n, i, mid, min, max)
        findMinAndMax(n, midPoint, j, min1, max1)
        if max < max1:
            max = max1
            ######### supposed to compare the newly found max/min to the earlier max/min and switch if needed
        if min > min1:
            min = min1 #########
    print(max)
    print(min)

findMinAndMax([1, 2, 3, 4, 5], 0, 4, 1, 1) ##the call to the function