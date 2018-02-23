from sklearn.feature_selection import SelectPercentile, f_classif, SelectKBest, mutual_info_regression
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import matplotlib.pyplot as plt


def percentile_feature_selection(features, labels, n_percentile):
    selector = SelectPercentile(f_classif, percentile=n_percentile)
    selector.fit(features, labels)
    return selector.get_support(indices=True)


def kbest_feature_selection(features, labels, k_number):
    selector = SelectKBest(mutual_info_regression, k=k_number)
    selector.fit(features, labels)
    return selector.get_support(indices=True)


def get_important_features_names(features_list, indices_list):
    """
    Returns the name of important features
    :param features_list: a list of all of the features, the first element must be POI
    :param indices_list: a list containing the indices of the most important features
    :return: a list with the most important features names
    """
    features_list = features_list[1:]
    important_features_names = []
    for index in indices_list:
        important_features_names.append(features_list[index])
    return important_features_names


def calculate_features_importance_scores(features, labels):
    clf = ExtraTreesClassifier(random_state=np.random.seed(25))
    clf = clf.fit(features, labels)
    return clf.feature_importances_


def get_features_names_scores(features_list, scores_list):
    """
    Associates each score to its corresponding feature, and sorts them in descending order and prints them and returns
    two numpy arrays of importances and features sorted
    :param features_list: a list of all of the features, the first element must be POI
    :param indices_list: a list containing the indices of the most important features
    :return: a numpy array of the features, in descendent order
    """
    features_scores = []
    features_list = features_list[1:]
    if len(features_list) == len(scores_list):
        for position in range(len(features_list)):
            features_scores.append((features_list[position], scores_list[position]))
    # Now I want to sort the list in descending order:
    features_scores_array = np.array(features_scores)
    features_descending = features_scores_array[features_scores_array[:,1].argsort()[::-1]]
    print features_descending
    names = features_descending[:,0]
    values = features_descending[:,1]
    return names, values


def create_ft_scores_barchart(features_names, score_values):
    N = len(score_values)
    x = range(N)
    width = 1/1.7
    plt.bar(x, score_values, width, color="RoyalBlue")
    plt.xticks(x, features_names, rotation=90)
    plt.ylabel("Importance feature score")
    plt.show()