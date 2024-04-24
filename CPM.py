def CPM(tasks):
    critical_path = []

    for task in tasks:
        last = task['last']
        if not last:
            es = 0
            ef = task['time']
        elif last:
            el_list = [d['ef'] for d in tasks if d['task'] in last]
            es = max(el_list)
            ef = es + task['time']
        task['ef'] = ef

    for idx, ak in enumerate(reversed(tasks)):
        if not idx:
            ak['lf'] = ak['ef']
        else:
            items = [item for item in tasks if ak['task'] in item['last']]
            durations = []
            for i in items:
                durations.append(i['ls'])
            ak['lf'] = min(durations)
        ak['ls'] = ak['lf'] - ak['time']
        ak['slack'] = ak['lf'] - ak['ef']

    for i in tasks:
        if not i['slack']:
            critical_path.append(i['task'])
    return critical_path, ef


tasks = [
    {"task": "A", "time": 3, "last": []},
    {"task": "B", "time": 4, "last": ["A"]},
    {"task": "C", "time": 2, "last": ["A", "B"]},
    {"task": "D", "time": 5, "last": ["A", "B", "C"]},
    {"task": "E", "time": 1, "last": ["C", "D"]},
    {"task": "F", "time": 2, "last": ["C"]},
    {"task": "G", "time": 4, "last": ["D", "E"]},
    {"task": "H", "time": 3, "last": ["F", "G"]},
    {"task": "I", "time": 5, "last": ["H"]},
    {"task": "J", "time": 7, "last": ["I"]},
    {"task": "K", "time": 9, "last": ["J"]},
    {"task": "M", "time": 2, "last": ["J", "K"]},
    {"task": "N", "time": 6, "last": ["J", "M"]},
]

path, time = CPM(tasks)
print(f'Znaleziona ścieżka krytyczna: {path}')
print(f'Czas trwania: {time}')
