example_input = '/Users/friedrichtenhagen/coding/advent_of_code2024/day2/example_input.txt'
input = '/Users/friedrichtenhagen/coding/advent_of_code2024/day2/input.txt'

def is_level_difference_valid(level_difference):
    if abs(level_difference) < 1 or abs(level_difference) > 3:
        return False
    else:
        return True

def calculate_report_safety():
    # Open the file in read mode ('r')
    with open(input, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        print(content)
        reports = content.split('\n')
        reports = [[int(level) for level in report.split()] for report in reports]
        print(reports)


        
        # The levels are either all increasing or all decreasing.
        # Any two adjacent levels differ by at least one and at most three.
        report_status_index = []
        for report_index, report in enumerate(reports):
            level_change_status = None # increasing or decreasing
            report_status = None # safe or unsafe

            for level_index in range(len(report)-1):
                print(report[level_index])
                level1 = report[level_index]
                level2 = report[level_index + 1]
                # compare levels
                level_difference = level1 - level2

                if level_difference > 0:
                    # decreasing
                    if level_change_status is None:
                        # initial setting of level_change_status
                        level_change_status = 'decreasing'
                    if level_change_status == 'increasing':
                        # change of level_change_status is not valid
                        report_status = 0
                        break
                elif level_difference < 0:
                    # increasing
                    if level_change_status is None:
                        # initial setting of level_change_status
                        level_change_status = 'increasing'
                    if level_change_status == 'decreasing':
                        # change of level_change_status is not valid
                        report_status = 0
                        break
                else: 
                    # level_difference == 0
                    report_status = 0
                    break
                if is_level_difference_valid(level_difference):
                    report_status = 1
                else:
                    report_status = 0
                    break

            report_status_index.append(report_status)
            print(report_status_index)
            print(sum(report_status_index))
        return sum(report_status_index)
                    
if __name__ == "__main__":
    calculate_report_safety()