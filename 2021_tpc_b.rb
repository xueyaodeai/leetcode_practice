# frozen_string_literal: true

case_num = $stdin.readline.to_i
case_num.times do
  _, heap_num = $stdin.readline.split(' ').map(&:to_i)
  heap_cards = Array.new(heap_num)
  max_length = 0
  heap_num.times do |inx|
    length, *heap_cards[inx] = $stdin.readline.split(' ').map(&:to_i)
    max_length = length if length > max_length
  end

  max_length.times do |inx|
    test_arr = heap_cards.map { |heap_card| heap_card[inx] }
    pp test_arr
  end

  pp 'end'
end
