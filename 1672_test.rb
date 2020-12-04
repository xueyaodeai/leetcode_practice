# @param {Integer[][]} accounts
# @return {Integer}
def maximum_wealth(accounts)
    accounts_total = accounts.map { |account| account.reduce(:+) }
    return accounts_total.max
end