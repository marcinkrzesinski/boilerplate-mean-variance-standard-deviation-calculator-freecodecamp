import numpy as np

def calculate(list):
    list = np.array(list)
    if list.size < 9:
        raise ValueError("List must contain nine numbers.")
    list = list.reshape(3,3)
    
    # DICT
    calculations = {
        'mean': [list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), list.mean().tolist()],
        'variance': [list.var(axis=0).tolist(), list.var(axis=1).tolist(), list.var().tolist()],
        'standard deviation': [list.std(axis=0).tolist(), list.std(axis=1).tolist(), list.std().tolist()],
        'max': [list.max(axis=0).tolist(), list.max(axis=1).tolist(), list.max().tolist()],
        'min': [list.min(axis=0).tolist(), list.min(axis=1).tolist(), list.min().tolist()],
        'sum': [list.sum(axis=0).tolist(), list.sum(axis=1).tolist(), list.sum().tolist()]
    }

    return calculations