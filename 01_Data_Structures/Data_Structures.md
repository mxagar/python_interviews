# Software Engineering Interview Questions in Python: Data Structures

This repository deals with data structures, algorithms, software design & Co. in python.

I created it while following the learning path [Ace the Python Coding Interview](https://www.educative.io/path/ace-python-coding-interview) in [educative.io](educative.io).

The path is divided in 7 modules:

1. Data Structures
2. Algorithms
3. Recursion
4. Dynamic Programming
5. Object Oriented Design
6. System Design
7. Concurrency

This file deals with the first module: **Data Structures**.

Mikel Sagardia, 2022.
No guarantees

## Overview of Contents:

1. Lists
2. Linked lists
3. Stacks and Queues
4. Trees
5. Tries
6. Graphs
7. Heaps
8. Hash Tables


## 1. Lists

### Lists: Definition

- Sequences of elements of ddifferent type
- Slicing: inclusive start, exclusive end
- For loops on lists
- Concatenation

```python
l = [1, 2, 3, 4, 5]
l1 = l[0:2] # [1, 2, 3]
l2 = l[2:4] # [4, 5]
l3 = l1 + l2 # [1, 2, 3, 4, 5]
for i in l:
	print(i)
```

### Challenge 1: Remove Even Integers from List

Solution 1: By Hand, `O(n)`

```python
def remove_even(lst):
    l = []
    for val in lst:
        if val % 2 != 0:
            l.append(val)
    return l
```

Solution 2: List Comprehensions, `O(n)`. This is is the preferred one, because it's more pythonic

```python
def remove_even(lst):
	# newList = [expression(i) for i in oldList if filter(i)]
	# squared_x = [x**2 for x in lst if x % 2 != 0]
    return [number for number in lst if number % 2 != 0]
```

### Challenge 2: Merge Two Sorted Lists

#### Solution 1 (Mine)

My first **wrong** solution: It's not enough to compare elements pairwise - each element needs to be compared against a subset of elements of the other list!

```python
def merge_lists(lst1, lst2):
    if len(lst1) == 0:
        # lest is empty, return the other list
        return lst2
    if len(lst2) == 0:
        return lst1
    else:
        # None of the lists is empty
        # Create an new one that marges both
        m = []
        different_length = False
        # Get shortest list: lstA
        if len(lst1) != len(lst2):
            different_length = True
            if len(lst1) < len(lst2):
                lstA, lstB = lst1, lst2
            else:
                lstA, lstB = lst2, lst1
        else:                
            lstA, lstB = lst1, lst2                            
        # Traverse shortest list (lstA)
        # and compare items to longest
        for i in range(len(lstA)):
            if lstA[i] < lstB[i]:
                m.append(lstA[i])
                m.append(lstB[i])
            else:
                m.append(lstB[i])
                m.append(lstA[i])
        # Rest of longest list needs to be concatenated
        if different_length:
            remainder = lstB[(len(lstA)):]
            m = m + remainder
    return m
```

#### Solution 2 (Mine)

My second **correct** solution: It has some mistakes/improvements:
- I don't need to detect the longest list.
- The complexity is `O(n*m)`, not that good.

```python
def merge_lists(lst1, lst2):
    if len(lst1) == 0:
        # lest is empty, return the other list
        return lst2
    if len(lst2) == 0:
        return lst1
    else:
        # None of the lists is empty
        # Create an new one that marges both
        m = []
        differece_length = abs(len(lst1) - len(lst2))
        # Get shortest list: lstA
        if differece_length > 0:
            if len(lst1) < len(lst2):
                lstA, lstB = lst1, lst2
            else:
                lstA, lstB = lst2, lst1
        else:                
            lstA, lstB = lst1, lst2                            
        # Traverse shortest list (lstA)
        # compare items to longest (lstB)
        # and instert the shortest (A) into the longest (B)
        # Last insertion in lstB
        last_insertion_B = -1
        # Copy lstB, to be merged
        m = lstB
        for i in range(len(lstA)):
            # Traverse rest of lstB/m (longest)
            for j in range(last_insertion_B + 1, len(m)):
            	# if current A item is smaller, insert it
                if lstA[i] <= m[j]:
                    m.insert(j, lstA[i])
                    last_insertion_B = j
                    # Break, otherwise inserted for the rest again!
                    break
 				# Edge case: we are at the end of m
                elif j == len(m) - 1:
                    m.append(lstA[i])
                    last_insertion_B = len(m) - 1

    return m
```

#### Solution 3 (Provided)

Provided Solution 1:  Time complexity is `O(m(n+m))`, because both lists are not traversed separately.

```python
# Merge list1 and list2 and return resulted list
def merge_lists(lst1, lst2):
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(lst1)+len(lst2)):
        result.append(i)
    # Traverse Both lists and insert smaller value from arr1 or arr2
    # into result list and then increment that lists index.
    # If a list is completely traversed, while other one is left then just
    # copy all the remaining elements into result list
    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if (lst1[index_arr1] < lst2[index_arr2]):
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1
    while (index_arr1 < len(lst1)):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while (index_arr2 < len(lst2)):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result

print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))
```

#### Solution 4 (Provided)

Provided Solution 2: Time complexity is `O(m(n+m))`, because both lists are not traversed separately. Also, note that `insert()` can be quadratic. However, the `extend()` function in `O(n)`.

```python
def merge_arrays(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1

print(merge_arrays([4, 5, 6], [-2, -1, 0, 7]))
```

### Challenge 3: Find Two Numbers that Add up to `k`

Given a list and a number `k`, find two numbers from the list that sum to `k`.

#### Solution 1 (Mine)

My **first** solution. It iterates the list in two (nested) for-loops, so it's `O(n^2)`:

```python
def find_sum(lst, k):
    for i in lst:
        r = k - i
        for j in lst:
            if r == j:
                return [i,j]
```

#### Solution 2 (Mine)

Another solution, suggested in the course: sort and perform a binary search! Note that:
- `.sort()` is used; since most optimal sorting functions take `O(nlogn)`, we assume it here, too
- Binary search takes `O(logn)`
- Thus: total time: `O(nlogn)`

The following is my approach for binary seach after sorting. I made a **huge mistake**: I forgot checking whether the searched item is in the left or right part of the list (which is why I sort and perform binary search!). Now it's corrected.

```python
# O(logn)
def binary_search(lst_sorted, item):
	length = len(lst_sorted)
	span = int(length / 2) # floor
	found = False
	if span < 2:
		# length = 1 | 2 | 3
		# span = 0 | 1
		if lst_sorted[0] == item:
			found = True
		if span == 1 and (item > lst_sorted[0]):
			# We have already checked lst_sorted[0]
			# Now we check lst_sorted[1], lst_sorted[2]
			found = binary_search(lst_sorted[1:], item)
	else:
		# length > 3
		# span > 1
		if item <= lst_sorted[span]:
			found = binary_search(lst_sorted[:(span+1)], item)
		else:	
			found = binary_search(lst_sorted[(span+1):], item)
	return found

def find_sum(lst, k):
	# We assume sort() works at O(nlogn)
	lst.sort() # inplace, returns None; sort() wort return a sorted list
	# lst_sorted = sort(lst)
	for i in lst:
		r = k - i
		found = binary_search(lst, r)
		if found:
			return [i, r]
```

### Solution 3 (Provided)

The following solution provided in the course uses sorting + binary search; while ny approach used recursion, this approach uses an iterative method.
This approach returns additionally the index where the item is found.

```python
def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2 # integer/floor division
        if a[mid] == item:
            index = mid
            found = True
        else:
        	# Take the boundaries of the list half
        	# that can contain item
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1

def find_sum(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k -lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k -lst[j]]
    
print(find_sum([1, 5, 3], 2))
print(find_sum([1, 2, 3, 4], 5))
```

#### Solution 4 (Provided)

Provided solution, using moving indices after having ordered the list. The list is traversed start->end and end<-start simultaneously. Since th elist is ordered, we can compute the sum of the items at each step and move indices accordingly. This solution is `O(nlogn)`: sorting `O(nlogn)` and traversing `O(n)`. However, it's not the optimal approach; the optimal approach consists in using hashing (see Challenge 8).

```python
def find_sum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))
```

### Challenge 4

Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.

#### Solution 1: Naive approach (Mine)

```python
def find_product(lst):
    arr = []
    for i in range(len(lst)):
        item = 1
        for j in range(len(lst)):
            if j != i:
                item *= lst[j]
        arr.append(item)
    return arr
```

#### Solution 2: Keeping Track of Previous Products (Mine)

```python
def find_product(lst):
    arr = list(range(len(lst)))
    previous_non_zero = -1
    for i in range(len(lst)):
        item = 1
        if previous_non_zero != -1:
            # arr[previous_non_zero] != 0 by definition
            # lst[i] != 0 if previous_non_zero != -1
            item = lst[previous_non_zero] * (arr[previous_non_zero] / lst[i])
        else: # previous_non_zero == -1
            for j in range(len(lst)):
                if j != i:
                    if lst[j] != 0:
                        item *= lst[j]
                    else:
                        item = 0
                        break
        arr[i] = item
        if item != 0:
            previous_non_zero = i
    return arr
```

#### Solutuon 3: Left Side Product Tracked (Provided)

We track the prodcut of the left side and compute for each item the product of the right side.  
Thus, we have two for loops: a loop fpr all items and a loop for the items on the right side.

The complexity is `O(n^2)`.

```python
def find_product(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result
```

#### Solution 4: Product from Left Multiplied by Product from Right (Provided)

Very nice solution: first the products from the left are computed by tracking them; then the sam eis done from the right!

We just traverse 2x the list, without nested for loops; thus, the time complexity is `O(n)`!

```python
def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product
```

### Challenge 5: Find Minimum Value in List

Given a list of `n` integers, find the minimum value in the list.
