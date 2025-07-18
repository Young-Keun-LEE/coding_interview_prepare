test = ["***", "* *", "***"]
target = []
target.extend(test * 3)
target.extend(test * 3)
target.extend(test * 3)

print('\n'.join(test))
print('\n'.join(target))