import argparse
import re

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_logs', required=True)
    args = parser.parse_args()
    
    with open(args.train_logs) as f:
        data = f.read()
    data = data.split('\n')
    
    accuracyLines = [s for s in data if 'Accuracy for LwF' in s]
    accuracy = []
    for i in range(0, len(accuracyLines), 2):
        accuracy.append(
            '.'.join(re.findall(r'\d+', accuracyLines[i]))
        )
    accuracy = np.array([float(i) for i in accuracy])
    
    plt.plot(range(len(accuracy)), accuracy, '-', label='Accuracy for LUCIR baseline')
    plt.legend()
    plt.savefig(args.train_logs.replace('train.log', 'train.png'))

    print('Mean Accuracy %s, FM %s' %(accuracy.mean(), accuracy[0] - accuracy[-1]))

    import ipdb;ipdb.set_trace()    
