print('==============================================================')
import sys
allSystemPath = sys.path
index = 0
for variablePath in allSystemPath:
    print(f"{index+1}: {variablePath}")
    index+=1
# Please note we can append custom path to sys path, thus we can access
# our custom made modules directly from anywhere
print('==============================================================')