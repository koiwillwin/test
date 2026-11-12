def average_by_sample(measurements):
    dt = {}
    for record in measurements:
        sample_id = record["sample_id"]
        value = record["value"]
        if value is None:
            continue
        if sample_id not in dt:
            dt[sample_id] = []
        dt[sample_id].append(value)
    averages = {}
    for sample_id, values in dt.items():
        averages[sample_id] = sum(values) / len(values)
    return averages

measurements = [
    {"sample_id": "A", "value": 10},
    {"sample_id": "B", "value": 20},
    {"sample_id": "A", "value": 14},
    {"sample_id": "B", "value": None},
    {"sample_id": "C", "value": None},
]

print(average_by_sample(measurements))
    # {"A": 12.0, "B": 20.0}