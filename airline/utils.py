from math import log

USER_CONSUMPTION: float = 0.002
PER_MINUTE_FUEL: float = 0.80
CAPACITY_AIRPLANE: int = 200


def get_airplane_per_minute_consumption(airplane_id: int, passenger_assumptions: int) -> float:
    airplane_consumption_per_minute = log(airplane_id) * PER_MINUTE_FUEL
    return airplane_consumption_per_minute + USER_CONSUMPTION * passenger_assumptions


def airplane_max_minutes_fly_capability(airplane_id: int, passenger_assumptions: int) -> float:
    capacity = airplane_id * CAPACITY_AIRPLANE
    return capacity / get_airplane_per_minute_consumption(airplane_id, passenger_assumptions)
