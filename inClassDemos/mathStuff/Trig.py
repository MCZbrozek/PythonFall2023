from math import sin, radians

def calc_sin(angle_degrees):
    angle_radians = radians(angle_degrees)
    
    return angle_radians

angle_degrees = 50 #degrees °
sin_of_angle = sin(angle_radians)

print(f"Angle in radians is: {calc_sin(angle_degrees)}")
print(f"sin is: {sin_of_angle}")