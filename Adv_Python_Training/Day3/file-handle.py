print('==============================================================')
import os
print(f'The present working directory is **{os.getcwd()}**')
fp = None
try:
    fp = open('lines.txt', 'r')  # mode r w r+ rb+
    for line in fp:
        print(line)
except Exception as error:
    print('|||ERROR||| System Said ===>',error,' <===')
finally:
    if fp != None:
        fp.close()
print('==============================================================')
