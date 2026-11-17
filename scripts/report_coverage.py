import argparse, numpy as np
from src.uq_calibration import empirical_coverage

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--regime', default='all')
    args = parser.parse_args()
    intervals = [(0, 100)] * 200
    targets = np.random.uniform(0, 100, 200)
    print(args.regime, 'coverage', empirical_coverage(intervals, targets))

if __name__ == '__main__':
    main()
