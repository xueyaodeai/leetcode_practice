# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  # 1. 暴力解题思路
  # 对字符串 s 进行两次循环，遍历所有长度子串，找到不重复的最长子串
  str_length = s.length
  max_sub_length = 0
  str_length.times do |i|
    str_length.times do |j|
      puts s[i...j].length
      max_sub_length = s[i...j].length if s[i...j].length > max_sub_length
      break if s[i...j].include?(s[j])
    end
  end
  return max_sub_length
end

puts length_of_longest_substring(" ")