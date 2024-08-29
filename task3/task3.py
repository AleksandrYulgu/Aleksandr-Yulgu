import json

with open('values.json') as values:
    data = json.load(values)
    values.close()
    data = data['values']

with open('tests.json') as tests:
    test = json.load(tests)
    tests.close()

with open('report.json', 'w') as report:
    json.dump(test, report, indent=4)
    report.close()

with open('report.json', 'r') as report:
    repor = json.load(report)
    report.close()



def ide(data, i, index):
    for j in data:
        if(j['id'] == i['id']):
            repor['tests'][index]['value'] = j['value']
            with open('report.json', 'w') as report:
                json.dump(repor, report, indent=4)
            break

def idek(data, i, index, idx):
    for j in data:
        if(j['id'] == i['id']):
            repor['tests'][index]['values'][idx]['value'] = j['value']
            with open('report.json', 'w') as report:
                json.dump(repor, report, indent=4)
            break


def ideke(data, i, index, idx, ix):
    for j in data:
        if(j['id'] == i['id']):
            repor['tests'][index]['values'][idx]['values'][0]['values'][ix]['value'] = j['value']
            with open('report.json', 'w') as report:
                json.dump(repor, report, indent=4)
            break


for index, i in enumerate(repor['tests']):
        try:
            b = i['values']
            ide(data, i, index)
            for idx, el in enumerate(b):
                try:
                    c = el['values']
                    idek(data, el, index, idx)
                    e = c[0]['values']
                    for ix, g in enumerate(e):
                        ideke(data, g, index, idx, ix)
                except:
                    idek(data, el, index, idx)
        except KeyError:
            ide(data, i, index)