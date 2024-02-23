import json

def makeJson(name,x,y,z,r,j1,j2,j3,j4,mode,actuator):
    data = {}
    data['x'] = x
    data['y'] = y
    data['z'] = z
    data['r'] = r
    data['j1'] = j1
    data['j2'] = j2
    data['j3'] = j3
    data['j4'] = j4
    data['mode'] = mode
    data['actuator'] = actuator
    with open(f'{name}.json', 'w') as file:
        json.dump(data, file)
    print('Json file created')
    return data

def readJson(name):
    with open(f'{name}.json', 'r') as file:
        data = json.load(file)
    return data