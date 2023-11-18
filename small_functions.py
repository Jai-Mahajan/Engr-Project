# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Jai Mahajan
# Section: 519
# Assignment: Lab 9
# Date: 29 October 2023
#
#
# YOUR CODE HERE
#

# a) Sphere volume
def parta(r_sphere, r_hole):
    from math import pi

    if r_hole >= r_sphere:
        return 0  
    elif r_hole == 0:
        return round(4/3*pi, 6)
    
    volume_bead = ((4 / 3) * pi) * (((r_sphere**2)-(r_hole**2))**(3/2))
    return round(volume_bead, 6)


# b) consecutive odd integers
def partb(n):
    for i in range(1, n):
        consecutive_sum = 0
        j = i
        while consecutive_sum < n:
            consecutive_sum += j
            j += 2

        if consecutive_sum == n:
            sqrt_n = int(n**0.5)
            if sqrt_n * sqrt_n == n:
                return [sqrt_n-1, sqrt_n+1]
            if i % 2 == 0:
                return False
            else:
                return list(range(i, j, 2))

    return False




# c) business card
def partc(border_char, name, company, email):
    max_length = max(len(name), len(company), len(email)) + 4
    side_stars = border_char * 13
    top_bottom_stars = border_char * (max_length + 2)
    
    card = f"{top_bottom_stars}\n" \
           f"{border_char} {name.center(max_length - 2)} {border_char}\n" \
           f"{border_char} {company.center(max_length - 2)} {border_char}\n" \
           f"{border_char} {email.center(max_length - 2)} {border_char}\n" \
           f"{top_bottom_stars}"

    return card





# d) Min, med, max
def partd(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    median = sorted_numbers[length // 2] if length % 2 != 0 else (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2

    return sorted_numbers[0], median, sorted_numbers[-1]

# e) Velocity 
def parte(times, distances):
    velocities = [(distances[i + 1] - distances[i]) / (times[i + 1] - times[i]) for i in range(len(times) - 1)]
    return velocities

# f) 2027 Whoop!
def partf(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 2027:
                return numbers[i] * numbers[j]

    return False
