# frozen_string_literal: true

def get_winner(serial, k)
  winner = nil
  win_times = 0
  # 考虑到收尾连续的情况，serial*2 进行遍历
  (serial * 2).each_with_index do |num, inx|
    if winner == num
      win_times += 1
    else
      winner = num
      win_times = 1
    end
    # 胜利次数超过 k 次时直接打印获胜结果并返回
    if win_times >= k
      puts "#{inx + 1} #{winner}"
      return nil
    end
  end
  # 遍历结束，说明胜利次数还小于 k，考虑两种情况：
  # 1. 胜利次数大于等于 serail 的长度，说明一直都是同一个人赢，打印获胜结果
  # 2. 胜利次数小于 serail 的长度，再循环也不可能超过 k，打印 INF
  if win_times < serial.length
    puts 'INF'
  else
    puts "#{k} #{winner}"
  end
end

case_num = $stdin.readline.to_i
case_num.times do
  _, k = $stdin.readline.split(' ').map(&:to_i)
  serial_n = $stdin.readline.split(' ').map(&:to_i)
  get_winner(serial_n, k)
end
