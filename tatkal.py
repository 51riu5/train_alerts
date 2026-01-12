from datetime import datetime, timedelta

AC_CLASSES = ["1A", "2A", "3A", "CC", "EC"]
NON_AC_CLASSES = ["SL", "2S"]

def calculate_tatkal_time(journey_date, travel_class):
    tatkal_date = journey_date - timedelta(days=1)

    if travel_class in AC_CLASSES:
        tatkal_time = datetime.combine(
            tatkal_date,
            datetime.strptime("10:00", "%H:%M").time()
        )
    elif travel_class in NON_AC_CLASSES:
        tatkal_time = datetime.combine(
            tatkal_date,
            datetime.strptime("11:00", "%H:%M").time()
        )
    else:
        raise ValueError("Invalid class")

    return tatkal_time
