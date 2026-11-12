def validate_plans(plans, limits):
    result = []
    for plan in plans:
        cur_error = []
        for name in limits:
            if name not in plan:
                cur_error.append(f'{name}: missing')
            else:
                value = plan[name]
                low, high = limits[name]
                if not isinstance(value, (int, float)):
                    cur_error.append(f'{name}: not a number')
                if value < low or value > high:
                    cur_error.append(f'{name}: out of range')
        if not cur_error:
            result.append(['Correct'])
        else:
            result.append(cur_error)
    return result

plans = [
    {"temperature": 80, "duration": 15},
    {"temperature": 120},
    {"temperature": 20, "duration": 3},
]

limits = {
    "temperature": (20, 100),
    "duration": (5, 30),
}

print(validate_plans(plans, limits))
