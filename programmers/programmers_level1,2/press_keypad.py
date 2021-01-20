def getDistance(hand, number):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    number = str(number)
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    return abs(x_hand - x_number) + abs(y_hand - y_number)


def solution(numbers, hand):
    result = ''
    leftHand = '*'
    rightHand = '#'

    for number in numbers:
        if number in [1, 4, 7]:
            result += 'L'
            leftHand = str(number)
            continue
        if number in [3, 6, 9]:
            result += 'R'
            rightHand = str(number)
            continue
        if number in [2, 5, 8, 0]:
            leftDistance = getDistance(leftHand, number)
            rightDistance = getDistance(rightHand, number)
            if leftDistance > rightDistance:
                result += 'R'
                rightHand = str(number)
            if leftDistance < rightDistance:
                result += 'L'
                leftHand = str(number)
            if leftDistance == rightDistance:
                if hand == 'right':
                    result += 'R'
                    rightHand = str(number)
                else:
                    result += 'L'
                    leftHand = str(number)
    return result