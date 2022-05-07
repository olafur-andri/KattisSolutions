def binary_search(array, x):
  # Repeat until the pointers low and high meet each other
  low = 0
  high = len(array) - 1
  while low <= high:
    mid = low + (high - low)//2
    if array[mid] == x:
      return mid
    elif array[mid] < x:
      low = mid + 1
    else:
      high = mid - 1
  return -1