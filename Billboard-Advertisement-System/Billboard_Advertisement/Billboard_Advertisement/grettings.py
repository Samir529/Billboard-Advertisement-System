import datetime

def give_grettings(request):
    currentTime = datetime.datetime.now()
    if 5 <= currentTime.hour < 12:
        time = 'morning'
    elif 12 <= currentTime.hour < 17:
        time = 'afternoon'
    elif 17 <= currentTime.hour < 21:
        time = 'evening'
    else:
        time = 'night'

    return {
        'time': time
    }



