# (c) 2021 - 2023 Open Risk (https://www.openriskmanagement.com)

obligor = {
    "id": 1,
    "name": "Genericom",
    "incorporation date": '1915-05-07',
    "previous names": ["Genco", "General Corp", "Gen Brothers"],
    "statements": ''
}

portfolio = {
    "metadata": {
        "as of date": '2015-05-07',
    },
    "obligor1": {
        "id": 1,
        "name": "Genericom",
        "incorporation date": '1915-05-07',
    },
    "obligor2": {
        "id": 2,
        "name": "ExpoCo",
        "incorporation date": '1815-05-07',
    }
}

obligor1 = {
    "id": 1,
    "name": "Genericom",
    "incorporation date": '1915-05-07',
    "previous names": ["Genco", "General Corp", "Gen Brothers"],
    "statements": ''
}
obligor2 = {
    "id": 2,
    "name": "ExpoCo",
    "incorporation date": '1815-05-07',
    "previous names": [],
    "statements": 'Missing'
}

portfolio2 = [obligor1, obligor2]
# >> > portfolio2[1]['name']
# 'Genericom'
