import numpy as np

def split_conformal(scores, alpha=0.1):
    scores = np.sort(np.asarray(scores))
    n = len(scores)
    rank = int(np.ceil((n + 1) * (1 - alpha))) - 1
    return float(scores[min(rank, n - 1)])

def empirical_coverage(intervals, targets):
    inside = [(lo <= t <= hi) for lo, hi, t in intervals]
    return sum(inside) / len(inside)
