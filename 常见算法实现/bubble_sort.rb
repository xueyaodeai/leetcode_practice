def bubble_sort(arr)
  (arr.length - 1).times do |i|
    (arr.length - 1 - i).times do |j|
      arr[j],  arr[j + 1] = arr[j + 1], arr[j] if arr[j] > arr[j + 1]
    end
  end
end

arr = [6, 7, 4, 3, 1, 7, 10]
bubble_sort(arr)
pp arr