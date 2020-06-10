import numpy as np
from parser import parameter_parser
from models.EncoderConv1D import EncoderConv1D
from models.EncoderWeight import EncoderWeight
from models.EncoderAttention import EncoderAttention
from preprocessing import get_graph_feature, get_pattern_feature

args = parameter_parser()


def main():
    graph_train, graph_test, graph_experts_train, graph_experts_test = get_graph_feature()
    pattern_train, pattern_test = get_pattern_feature()

    graph_train = np.array(graph_train)  # The training set of graph feature
    graph_test = np.array(graph_test)  # The testing set of graph feature

    # The training set of patterns' feature
    pattern1train = []
    pattern2train = []
    pattern3train = []
    pattern4train = []
    for i in range(len(pattern_train)):
        pattern1train.append([pattern_train[i][0]])
        pattern2train.append([pattern_train[i][1]])
        pattern3train.append([pattern_train[i][2]])

    # The testing set of patterns' feature
    pattern1test = []
    pattern2test = []
    pattern3test = []
    pattern4test = []
    for i in range(len(pattern_test)):
        pattern1test.append([pattern_test[i][0]])
        pattern2test.append([pattern_test[i][1]])
        pattern3test.append([pattern_test[i][2]])

    pattern_train = np.array(pattern_train)
    pattern_test = np.array(pattern_test)

    # The ground truth label of certain contract in training set
    y_train = []
    for i in range(len(graph_experts_train)):
        y_train.append(int(graph_experts_train[i]))
    y_train = np.array(y_train)

    # The label of certain contract in testing set
    y_test = []
    for i in range(len(graph_experts_test)):
        y_test.append(int(graph_experts_test[i]))
    y_test = np.array(y_test)

    if args.model == 'EncoderConv1D':
        model = EncoderConv1D(graph_train, graph_test, pattern_train, pattern_test, y_train, y_test)
    elif args.model == 'EncoderWeight':
        model = EncoderWeight(graph_train, graph_test, np.array(pattern1train), np.array(pattern2train),
                              np.array(pattern3train), np.array(pattern1test), np.array(pattern2test),
                              np.array(pattern3test), y_train, y_test)
    elif args.model == 'EncoderAttention':
        model = EncoderAttention(graph_train, graph_test, np.array(pattern1train), np.array(pattern2train),
                              np.array(pattern3train), np.array(pattern1test), np.array(pattern2test),
                              np.array(pattern3test), y_train, y_test)
    model.train()  # training
    model.test()  # testing


if __name__ == "__main__":
    main()