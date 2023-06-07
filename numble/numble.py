import timeit
import numpy as np

setup = "import numpy as np; import random; operations = [np.add, np.subtract, np.multiply, np.divide]; target = 967; rancomp = [2,4,7,10,25,100]; sol = False"
testcode = '''
while not sol:
    np.random.shuffle(rancomp)
    ranop = [random.choice(operations), random.choice(operations), random.choice(operations), random.choice(operations), random.choice(operations)]
    b = ranop[4](ranop[3](ranop[2](ranop[1](ranop[0](rancomp[0], rancomp[1]), rancomp[2]), rancomp[3]), rancomp[4]), rancomp[5])
    if b == target:
        print("solution found")
        print(rancomp)
        print(ranop)
        sol = True
'''

print(np.mean(timeit.repeat(stmt=testcode, setup=setup, repeat=10)))