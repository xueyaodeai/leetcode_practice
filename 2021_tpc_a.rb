# frozen_string_literal: true

case_num = $stdin.readline.to_i
case_num.times do
  # pp $stdin.readline.split(' ').map(&:to_i)
  _, race = $stdin.readline.split(' ').map(&:to_i)
  solved = $stdin.readline.split(' ').map(&:to_i)
  unknown = $stdin.readline.split(' ').map(&:to_i)
  solved[0] += unknown[0]
  best_race = solved.sort.reverse.find_index(solved[0])
  if best_race < race
    puts 'Yes'
  else
    puts 'No'
  end
end
