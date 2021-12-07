def selection_sort(arr)
  arr.length.times do |i|
    min_index = i
    (arr.length - i).times do |j|
      if arr[j + i] < arr[min_index]
        min_index = j + i
      end
    end
    arr[i], arr[min_index] = arr[min_index], arr[i]
    pp arr
  end
end

arr = [6, 7, 4, 3, 1, 7, 10, 9]
selection_sort(arr)
arr_2 = [1, 0]
selection_sort(arr_2)