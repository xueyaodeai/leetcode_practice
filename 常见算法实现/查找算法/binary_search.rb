def binary_search(sorted_arr, search_value)
  low, high = 0, sorted_arr.length - 1
  while low <= high
    mid = (low + high) / 2
    if search_value == sorted_arr[mid]
      return mid
    elsif search_value < sorted_arr[mid]
      high = mid - 1
    else
      low = mid + 1
    end
  end
  return nil
end

arr = [1, 3, 6, 9, 11]
puts binary_search(arr, 4)
puts binary_search(arr, 6)
