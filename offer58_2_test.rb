# @param {String} s
# @param {Integer} n
# @return {String}
def reverse_left_words(s, n)
  tmp_arr = Array.new(s.length)
  s.split('').each_with_index do |char, inx|
      tmp_arr[inx-n] = char
  end
  return tmp_arr.join('')
end

pp reverse_left_words("abcdefg", 2)