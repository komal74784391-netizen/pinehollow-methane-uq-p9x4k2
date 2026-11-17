import argparse, numpy as np
from src.uq_calibration import split_conformal

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--alpha', type=float, default=0.1)
    args = parser.parse_args()
    residual = np.abs(np.random.normal(0, 12, 800))
    q = split_conformal(residual, args.alpha)
    print('conformal quantile', round(q, 2), 'ppb')

if __name__ == '__main__':
    main()
