import re
print('==============================================================')
inputString = """
    My name is Sahasrangshu I'm 31 year old
    My name is Manali I'm 28 year old
    My name is Ratna I'm 61 year old
    I came from a family which is 200 year old
"""
ages = re.findall(r'\d{1,2}', inputString)
print(ages)
# printing ['31', '28', '61', '20', '0'] don't know why, i don't like regex
print('==============================================================')
