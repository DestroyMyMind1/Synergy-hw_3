# less 1

a = int(input())

if a % 2 != 0 and a / 2 > 0:
    print("положительное нечетное число")
elif a % 2 == 0 and a / 2 > 0:
    print("положительное четное число")
elif a % 2 != 0 and a / 2 < 0:
    print("отрицательное нечетное число")
elif a % 2 == 0 and a / 2 < 0:
    print("отрицательное четное число")
elif a / 2 == 0:
    print('нулевое число')

# less 2

word = input().lower()
vowel_letters = ['a', 'e', 'i', 'o', 'u']

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for i in word:
    if i in vowel_letters[0]:
        a_count += 1
    elif i in vowel_letters[1]:
        e_count += 1
    elif i in vowel_letters[2]:
        i_count += 1
    elif i in vowel_letters[3]:
        o_count += 1
    elif i in vowel_letters[4]:
        u_count += 1

all_count = a_count + e_count + i_count + o_count + u_count

if a_count > 0 and e_count > 0 and i_count > 0 and o_count > 0 and u_count > 0:
    print(f'a = {a_count}')
    print(f'e = {e_count}')
    print(f'i = {i_count}')
    print(f'o = {o_count}')
    print(f'u = {u_count}')
    print(f'Гласных:', all_count)
    print(f'Согласных:', len(word) - all_count)
else:
    print(False)

# aeiou

# less 3

min_investment = int(input('min_investment: '))
mike = int(input('mike money: '))
ivan = int(input('ivan money: '))

if mike >= min_investment and ivan >= min_investment:
    print(2)
elif mike >= min_investment and ivan < min_investment:
    print('Mike')
elif mike < min_investment and ivan >= min_investment:
    print('Ivan')
elif mike + ivan >= min_investment:
    print(1)
else:
    if mike < min_investment and ivan < min_investment and mike + ivan < min_investment:
        print(0)







