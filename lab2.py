jug1 = int(input("Enter the capacity of the first jug: "))
jug2 = int(input("Enter the capacity of the second jug: "))

target = int(input("Enter the target volume: "))
def water_jug_problem(jug1, jug2, target):
    if target % gcd(jug1, jug2) != 0 or target > jug1 :
        print("Target volume cannot be reached.")
        return

    j1, j2 = 0, 0
    count = 1
    print(j1,j2)
    while j1 != target and j2 != target:
        if j1 == 0:
            j1 = jug1
            count += 1
            print(j1,j2)
        elif j2 == jug2:
            j2 = 0
            count += 1
            print(j1,j2)
        else:
            pour = min(j1, jug2 - j2)
            j1 -= pour
            j2 += pour
            count += 1
            print(j1,j2)
    print(j1,0)
    print("Minimum number of steps to reach the target:", count)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

water_jug_problem(max(jug1,jug2),min(jug1,jug2), target)
