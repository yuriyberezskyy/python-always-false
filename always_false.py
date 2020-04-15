# Write your always_false function here:

# Uncomment these function calls to test your always_false function:
#
# should print False
# print(always_false(-1))
# should print False
# print(always_false(1))
# should print False


def always_false(num):
    if(num <= 0 or num >= 0):
        return False


print(always_false(0))
print(always_false(-1))
print(always_false(1))
