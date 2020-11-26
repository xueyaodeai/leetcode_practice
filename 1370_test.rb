# @param {String} s
# @return {String}
def sort_string(s)
	# 生成统计字母出现次数的 hash
  keys_count = {}
  s.split('').each do |key|
    if keys_count[key].nil?
      keys_count[key] = 1
    else
      keys_count[key] += 1
    end
  end
  sorted_keys = keys_count.keys.sort()
  reverse_sorted_keys = sorted_keys.reverse()

	# 进行顺序和逆序的遍历，循环直至两个字符串长度相等
  result = []
  origin_length = s.length
  while result.length != origin_length
    sorted_keys.each do |key|
      if keys_count[key] > 0
        result.append(key)
        keys_count[key] -= 1
      end
    end
    reverse_sorted_keys.each do |key|
      if keys_count[key] > 0
        result.append(key)
        keys_count[key] -= 1
      end
    end
  end

  return result.join('')
end

pp sort_string 'leetcode'