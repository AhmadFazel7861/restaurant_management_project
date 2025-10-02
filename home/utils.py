from datetime import datetime, time

def is_restaurant_open():
    """
    check if the resturant is currently open based on operating hours
    returns:
        bool: True if open, False if closed.
    """

now = datetime.now()
current_day = now.weekday()
current_time = now.time()


if current_day < 5:
    open_time = time(9, 0)
    close_time = time(22, 0)
else:
    open_time = time(10, 0)
    close_time = time(23, 0)

return open_time <= current_time <= close_time        