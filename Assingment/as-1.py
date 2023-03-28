n = [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
position = 0
while position < len(n):
    if position > 0 and n[position] < n[position - 1]:
        print(position)
    position += 1

def test_location(cards, mid):
    if mid > 0 and n[mid] < n[mid - 1]:
            if mid-1 >= 0 and n[mid-1] == n[mid]:
                return 'left'
            else:
                return 'found'
    
    elif n[mid] < n[mid -1]:
        hi = mid - 1
    elif n[mid] > n[lo]:
        lo = mid + 1

def locate_card(cards):
    lo = 0
    hi = len(n) - 1

    while lo <= hi:
        mid = (lo + hi)//2
        
        result = test_location(n, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

results = locate_card(n)
print(results)

