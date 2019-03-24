

def user_points(correct):
    points=correct
    return correct

def helper_points(solved,doubts):
    points=solved*10
    points+=(doubts-solved)*5
    

def group_pool(ob,questions):
    if ob==1:
        time=questions*10
        points=questions*5
    else:
        time=questions*17
        points=questions*10
    return time,points


def group_points(users,time_all,time_used,points):
    if time_used<=time_all:
        each_user_points=int(points/users)
    elif time_used<(1.5*time_all):
        each_user_points=int((points/users)*0.75)
    elif time_used<(2.0*time_all):
        each_user_points=int((points/users)*0.5)
    return each_user_points

    