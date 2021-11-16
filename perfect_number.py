# -*- coding: utf-8 -*-
"""
Perfect number is a positive integer that is equal to the sum of 
its positive divisors.
"""

class Perfect_Number:
    
    def __init__(self, number):
        self.number = number
        
    def isPerfectNumber(self, number):
        if number < 1:
            return False
        
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                divisor = i
                print(f'Divisor = {divisor}')
                sum += divisor
        print(f'Sum = {sum}')
        if number != sum:
            return False
        
        return True
    
    
# %%
while True:
    try:
        number = int(input('Enter the integer number >>> '))
        perfect_number = Perfect_Number(number)
        is_perfect_number = perfect_number.isPerfectNumber(number)
        print(f'Is perfect number? {is_perfect_number}')
        break
    except:
        print('Wrong value.')