example_input = '/Users/friedrichtenhagen/coding/advent_of_code2024/day3/example_input.txt'
input = '/Users/friedrichtenhagen/coding/advent_of_code2024/day3/input.txt'
import re

def calculate_report_safety():
    # Open the file in read mode ('r')
    with open(input, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        pattern = r"mul\(\d+,\d+\)"
        matches = re.findall(pattern, content)
        print(matches)
        total_sum = 0
        for multiplic in matches:
            num1 = multiplic.split('(')[1].split(',')[0]
            num2 = multiplic.split('(')[1].split(',')[1].replace(')', '')
            print(num1, num2) 
            product = int(num1) * int(num2)
            print(product)
            total_sum += product
        print(total_sum)
if __name__ == "__main__":
    calculate_report_safety()