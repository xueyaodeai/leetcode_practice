# @param {String} command
# @return {String}
def interpret(command)
  command.gsub('()', 'o').gsub('(al)', 'al')
end