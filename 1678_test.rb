# @param {String} command
# @return {String}
def interpret(command)
  command.gsub('()', 'o').gsub('(al)', 'al')
end

pp interpret('(al)G(al)()()G')
