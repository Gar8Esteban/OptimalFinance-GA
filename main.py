import BlackBox as bX
import Sequences as sQ
import numpy as np
from geneticalgorithm import geneticalgorithm as ga


def f(X):
    dim = len(X)
    p = [0, 1, 2]
    sec = sQ.Sequences(p).combinations()
    if dim == 6:
        #print(X)
        array_a = np.array([X])
        array_x = np.append(sec, array_a.transpose(), axis=1)
        if sum(X) == 21:
            transactions = bX.BlackBox().transfers(np.round(array_x).tolist())
            return transactions + 1
        else:
            return 10000


if __name__ == '__main__':

    varConstraints = np.array([[1, 10],
                               [0, 10],
                               [1, 10],
                               [5, 10],
                               [5, 10],
                               [0, 10]])

    algorithm_param = {'max_num_iteration': 1000,
                       'population_size': 500,
                       'mutation_probability': 0.1,
                       'elit_ratio': 0.01,
                       'crossover_probability': 0.5,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': None}

    model = ga(function=f, dimension=6, variable_type='int', variable_boundaries=varConstraints,
               algorithm_parameters=algorithm_param)
    model.run()

    print(f([8, 0, 3, 5, 5, 0]))

