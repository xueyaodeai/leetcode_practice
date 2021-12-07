# @param {Integer[]} nums
# @param {Integer} n
# @return {Integer[]}
def shuffle(nums, n)
  shuffle_arr = []
  n.times do |inx|
    shuffle_arr.push(nums[inx], nums[n + inx])
  end
  shuffle_arr
end
