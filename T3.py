def find_unmeasured(samples, measurements):
    measured_ids = set()
    for record in measurements:
        measured_ids.add(record["sample_id"])
    result = []
    for s in samples:
        sample_id = s["sample_id"]
        if sample_id not in measured_ids:
            result.append(sample_id)
    return result

samples = [
    {"sample_id": "A"},
    {"sample_id": "B"},
    {"sample_id": "C"},
    {"sample_id": "D"},
]

measurements = [
    {"sample_id": "A", "value": 10},
    {"sample_id": "C", "value": 20},
    {"sample_id": "A", "value": 14},
]
print(find_unmeasured(samples, measurements))