def numToEng(n):
    _ = {
        '001':['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'],
        '010':['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    }
    if len(str(n)) == 1:
        return _['001'][n]

    elif len(str(n)) == 2:
        if str(n).startswith('1'):
            return _['001'][n]
        else:
            for i in range(2,10):
                if str(n).startswith(str(i)):
                    output = _['010'][int(str(n)[0])]
            if not str(n).endswith('0'):
                output += '-' + _['001'][int(str(n)[-1])]
            
            return output

    elif len(str(n)) == 3:
        numbers = [int(i) for i in str(n)]; output = ''
        output += _['001'][numbers[0]] + ' hundred '
        if numbers[1] == 1:
            output += _['001'][int(str(numbers[1]) + str(numbers[2]))]
        else:
            for i in range(2,10):
                if numbers[1] == i:
                    output += _['010'][numbers[1]]

            if numbers[2] != 0:
                if numbers[1] != 0:
                    output += '-' + _['001'][numbers[2]]
                else: output += _['001'][numbers[2]]
        return output


def cap_space(txt):
    output = ""
    for i in enumerate(txt):
        if i[1] == i[1].upper() and i[1].isalpha():
            output += i[1].replace(i[1], f" {i[1].lower()}")
        else:
            output += i[1]
    
    return output


def input_type(value):
    if value.isnumeric():
        return 'integer'
    elif value.replace('.', '', 1).isdigit():
        return 'double'
    elif not (value.isdigit() and value.isnumeric()) and type(value) is str:
        return 'string'


def most_frequent_element(arr):
    most = {0:0}
    for i in enumerate(arr):
        if arr.count(i[1]) > list(most.values())[0]:
            most.pop(list(most.keys())[0])
            most.update({i[1]:i[0]})

    return list(most.keys())[0]


def delete_element_in_array(arr, index):
    arr.pop(index); return arr

def sort_array(array):
    return sorted(array)

def sort_array(array, type_):
  if 'S':
    return sorted(array)
  else:
    return sorted(array, reverse=True)


def factorial(number):
  for i in range(1,number):
    number *= i
  return number


def primes_nums(array):
    arr = []
    for n in array:
        if n <= 1: continue
        for _ in range(2,n):
            if (n % _) != 0:
                arr.append(n)
                continue
  
    return arr


def word_repeat(word, n):
    return (f' {word}' * n)[1:]



def match_arrays(array1, array2):
    if sorted(array1) == sorted(array2):
        return True
    else:
        return False

def numbers_range(number):
  n = ''
  for i in range(number+1):
    n += (str(i) + ' ')
  return n[:len(n)-1]

def exponent_x(number, exponent):
  return number ** exponent

def countDown(number):
    op = ""
    for i in sorted(range(number+1), reverse=True):
        op += f" {str(i)}"
    return op[1:]

def Decimal_places(num):
  if len(num.split('.')) == 2: return len(num.split('.')[1])
  return 0

def date_formating2(date):
    date = date.split('-')
    return '-'.join([date[2], date[1], date[0]])

def date_formating(date):
    x = date.split('-')
    return str(x[2]+ '-' + x[1] + '-' + x[0])


def reverse_case(string):
    output = ''
    for i in string:
        if i.isupper():
            output += i.lower()
        elif i.islower():
            output += i.upper()
        else:
            output += i
    return output

def date_format(date):
    bOrInG = date.replace('"',"").split('/')
    # "2020/1/1 | 2020-1-1 | 1/1/2020"
    return '"{}/{}/{} | {}-{}-{} | {}/{}/{}"'.format(
        bOrInG[0],bOrInG[1],bOrInG[2],
        bOrInG[0],bOrInG[1],bOrInG[2],
        bOrInG[2],bOrInG[1],bOrInG[0],
    )

def bin_to_oct(b):
    if (len(b) % 3) != 0:
        while (len(b) % 3) != 0:
            b = '0' + b
    
    BIN = []
    b = str(b)
    while b != '':
        BIN.append(b[:3])
        b = b[3:]

    print(BIN)
    OCT = ''
    for binary in BIN: 
        o = 0
        if binary[0] == '1': o += 4; print(o)
        if binary[1] == '1': o += 2; print(o)
        if binary[2] == '1': o += 1; print(o)
        OCT += str(o)

    return OCT



def countWords(txt):
	return len(txt.split(' '))
    
def oddsVsEvens(num):
    odd = 0; even = 0
    for n in range(1,num):
        if n % 2 == 0: even += 1
        else: odd += 1
    print(odd, even)
    if odd == even: return 'equal'
    elif odd > even: return 'odd'
    elif odd < even: return 'even'

#print(oddsVsEvens(463))


def ww(num):
    odd = 0
    even = 0
    for i in range(len(str(num))):
        if (int(str(num)[i]) % 2) == 0:
            even += int(str(num)[i])
        else:
            odd += int(str(num)[i])
    if odd == even:
        return 'equal'
    elif odd > even:
        return 'odd'
    elif even > odd:
        return 'even'


def remove_duplicate(arr):
    for i in sorted(arr):
        if arr.count(i) > 1:
            arr.remove(i)

    return arr

def factorial(number):
  return number ** number

def left_digit(_):
  for i in _.strip():
    if i.isdigit():
        return i

def missingLetter(txt):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    if txt in abc:
        return 'No Missing Letter'
    else:
        p = []
        for i in range(len(txt)):
            p.append(abc.find(txt[i]))

        for x in range(p[0], p[-1]+1):
            if x not in p:
                return abc[x]

def root_check(sqr, num):
  square_root = sqr**(1/2)
  if square_root == num: return int(square_root)
  else: return 0



def sum_two_smallest_nums(arr):
  _ = min(arr)
  arr.remove(_)
  return min(arr) + _


def removeSpecialCharacters0(txt):
    _ = '~!@#$%^&*()+={}][|\\`,/?;:\'\"<>'
    output = ''

    # generate new text without special characters
    for i in txt:
        if not i in _:
            output += i
    
    # filters
    while output.endswith(' '):
        output = output[:len(output)-1]

    while output.startswith(' '):
        output = output[1:]

    return output.replace('  ', ' ')

def removeSpecialCharacters(txt):
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_ '
    for i in txt:
        if i not in abc:
            txt = txt.replace(i, '')
    txt = txt.replace('  ', ' ')
    return txt



def raduis(circumference):
	return (circumference / (2 * 3.14))

def longestZero(txt):
    return max([i for i in str(txt).split('1')])

def addStrNums(num1, num2):
    def getDigits(txt):
        for i in txt:
            if i.isdigit():
                yield int(i)
    output = 0
    for x,y in zip(getDigits(num1),getDigits(num2)):
        output += (x+y)
    
    if output == 0: return '-1'
    else: return str(output)


def cumulative_sum(arr):
    for i in enumerate(arr):
        pass
def squares(num):
	return float(
        (
            num ** (1/2)
            )
    )

def cubes(num):
	return float(
        (
            num ** (1/3)
            )
    )


def primes_nums(array):
    lst = list()
    for num in array:
        if num > 1 and type(num) is int():
            flag = True
            for i in range(2,num):
                if (num % i) == 0:
                    flag = False
                    break
        else:
            flag = False

        if flag:
            lst.append(i+1)

    return lst

def primes_nums(array):
    lst = list()
    for num in array:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                lst.append(num)
    return lst

def oct_to_bin(octal):
	return bin(int(str(octal), 8)).replace('0b','')

def oct_to_hex(octal):
    return hex(int(str(round(octal)), 8))[2:].upper()


def number_sum(num):
  return sum([i for i in range(num+1)])

def remove_duplicate(arr):
    _ = list()
    [_.append(i) for i in arr if i not in _]
    return _



def get_duplicate_elements(arr):
    output = list()
    for _ in arr:
        if arr.count(_) > 1 and _ not in output:
            output.append(_)
    return output

def merge_sort(node1, node2):
    return sorted(node1 + node2)

def isEmpty(txt):
	return False if len(txt) > 0 else True



def math_expr(txt):
    symbols = ['+', '-', '*', '^', '%', '/']
    
    for i in txt[1:-1]:
        if i in symbols:
            return True
    return False    
        

def stringCheck(value):
    return True if len(value) == value.count(value[0]) else False


def convertPercent(p):
	return float(int(p.split('%')[0])/100)

def search(word, character):
    return word.find(character)

def unique(arr):
    return [i for i in arr if arr.count(i) == 1]


def clean_array(arr):
    return [i for i in arr if i is not None]

def array_root(arr):
	return [(i**(1/2)) for i in arr]
    # [44, 23, 546]
    # [6.6332495807108, 4.795831523312719, 23.366642891095847]
def cone_volume(radius, height):
  return (1/3) * radius * height

def cone_volume(radius, height):
  return (1/3) * (radius ** 2) * height * 3.14

def calculate_circumference(radius):
    return 3.14 * (radius * 2)

def find_circle_area(radius):
  return (radius ** 2) * 3.14

def sortByLength(txt):
    return " ".join(i for i in sorted([i for i in txt.split(' ')], key=len))


def middle_char(word):
    i = (len(word) - 1) // 2
    return word[i:-i] or word

def hashtag_it(arr):
  return ' '.join(['#' + i for i in arr])


def date_format(date):
  # "2020/1/1 | 2020-1-1 | 1/1/2020"	
  if '/' not in date: date = str(date).split('-')
  else: date = str(date).split('/')  
  date = [i for i in date]
  return '{}/{}/{} | {}-{}-{} | {}/{}/{}'.format(
      date[0], date[1], date[2],
      date[0], date[1], date[2],
      date[2], date[1], date[0]
  )

def date_formating(date):
	return '-'.join(i for i in reversed(date.split('-')))
