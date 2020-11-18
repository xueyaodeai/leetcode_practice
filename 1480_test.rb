# @param {Integer[]} nums
# @return {Integer[]}
def running_sum(nums)
  for i in 1...nums.length
    nums[i] = nums[i-1] + nums[i]
  end
  return nums
end

puts running_sum([1,2])