$max = [0, 0, 1, 2, 4]

# @param {Integer} n
# @return {Integer}
def integer_break(n)
  return $max[n] unless $max[n].nil?

  tmp = n
  tmp_max = 1
  while tmp > 4
    tmp -= 3
    tmp_max *= 3
  end
  $max[n] = tmp_max * tmp
  $max[n]
end

58.times do |i|
  puts integer_break(i + 1)
end
