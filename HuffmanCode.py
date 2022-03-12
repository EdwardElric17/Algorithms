s = str(input())
letters = dict()
letter_list = list()
letter_list_bin = list()
def custom_key(letters): 
    return letters[1]
# coded_elems = dict()
# coded_str = ''
# start = '0'
for elem in s:
    if elem not in letters:
        letters[elem] = []
    letters[elem] = s.count(elem)
for key, value in letters.items():
    letter_list.append([key, value])
letter_list.sort(key=custom_key)
while len(letter_list) != 2:
    letter_list.append([letter_list[0], letter_list[1], letter_list[0][1] + letter_list[1][1]])
    letter_list.remove(letter_list[0])
    letter_list.remove(letter_list[1])
print(letter_list)
# for letter in letters:
#     coded_elems[letter] = []
#     coded_elems[letter] = start
#     start = '1' + start
# for item in s:
#     coded_str += coded_elems[item]
# print(len(letters), len(coded_str))
# for key, value in coded_elems.items():
#     print(f'{key}: {value}')
# print(coded_str)