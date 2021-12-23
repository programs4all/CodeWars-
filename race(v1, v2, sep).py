'''
def convert(v):
    return v / 60 / 60 


def race(v1, v2, sep):
    # your code
    # v1 = 720 f/h or 0.2 f/s
    speed1 = 1 # convert(v1) # f/s
    speed2 = 2 # convert(v2) # f/s
    # print(speed1, speed2)
    if v1 >= v2: return None
    
    dis1 = sep
    dis2 = 0
    secs = 0
    while dis1 >= dis2:
        secs += 1 

        dis1 += speed1
        dis2 += speed2
        print("seconds:", secs, '\n', "1:", dis1, "2:", dis2)
            
    return secs


a = race(720, 850, 70)
b = race(80, 91, 37)
c = race(820, 81, 550)
print(a)
'''

def race(v1, v2, seperation):
    # your code
    if v1 >= v2: return None
    difference_in_speed = v2 - v1
    time_h = seperation / difference_in_speed

    hours, minutesH = str(time_h).split('.')

    minutesH = '0.' + minutesH
    minutes = float(minutesH) * 60
    minutes, secondsM = str(minutes).split('.')

    secondsM = '0.' + secondsM
    seconds = round(float(secondsM) * 60)

    return [int(hours), int(minutes), int(seconds)]

    # minutes, seconds = minutes.split('.')
    # print(minutes, seconds)



a = race(720, 850, 70)
b = race(80, 91, 37)
c = race(820, 81, 550)
print(a)
print(b)
print(c)