from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from tools.feature_format import featureFormat


def create_scatter_plot_color_pois(data_dictionary, features_list):
    """
    Creates a scatter plot coloring the pois as red and non-pois as blue
    :param data_dictionary: dictionary where each key is a string with a person's name and the value is another
    dictionary with the features associated to that person.
    :param features_list: should be len 3, the first element should be POI
    """
    data = featureFormat(data_dictionary, features_list)
    color_points = np.array([])
    values_x = np.array([])
    values_y = np.array([])
    for point in data:
        color_points = np.append(color_points, point[0])
        values_x = np.append(values_x, point[1])
        values_y = np.append(values_y, point[2])
    plt.scatter(values_x, values_y, c=color_points, cmap="bwr")
    plt.xlabel(str(features_list[1]))
    plt.ylabel(str(features_list[2]))
    plt.show()


def spot_negative_restricted_stock(data_dictionary):
    """
    Prints the name of the person who has a negative restricted stock value and the negative value
    :param data_dictionary: dictionary where each key is a string with a person's name and the value is another
    dictionary with the features associated to that person.
    """
    negative_restricted_stock = 0
    for name, features in data_dictionary.iteritems():
        if features["restricted_stock"] != "NaN":
            if features["restricted_stock"] < 0:
                negative_restricted_stock = features["restricted_stock"]
                name_negative_restricted_stock = name
    print "negative_restricted_stock", negative_restricted_stock, name_negative_restricted_stock
    return


def spot_first_outlier(data_dictionary, features_list):
    """
    Prints the first outlier of each feature
    :param data_dictionary: dictionary where each key is a string with a person's name and the value is another
    dictionary with the features associated to that person.
    :param features_list: a list of len 2 containing the strings of features names to evaluate
    """
    highest_feature_zero = 0
    name_highest_feature_zero = 0
    highest_feature_one = 0
    name_highest_feature_one = 0
    for name, features in data_dictionary.iteritems():
        if features[features_list[0]] != "NaN" and features[features_list[1]] != "NaN":
            if features[features_list[0]] > highest_feature_zero:
                highest_feature_zero = features[features_list[0]]
                name_highest_feature_zero = name
            if features[features_list[1]] > highest_feature_one:
                highest_feature_one = features[features_list[1]]
                name_highest_feature_one = name
    print "highest", str(features_list[0]), highest_feature_zero, name_highest_feature_zero
    print "highest", str(features_list[1]), highest_feature_one, name_highest_feature_one


def spot_outliers(data_dictionary, features_list, revision_value_feature_zero, revision_value_feature_one):
    """
    Prints outs the outliers found in two features at a time and each feature separately
    :param data_dictionary: dictionary where each key is a string with a person's name and the value is another
    dictionary with the features associated to that person.
    :param features_list: a list of len 2 containing the strings of features names to evaluate
    :param revision_value_feature_zero: the start point to check the outlier for the first feature
    :param revision_value_feature_one: the start point to check the outlier for the second feature
    """
    outliers_feature_zero = defaultdict(int)
    outliers_feature_one = defaultdict(int)
    outliers_both_features = defaultdict(int)
    for name, features in data_dictionary.iteritems():
        if features[features_list[0]] != "NaN" and features[features_list[1]] != "NaN":
            if features[features_list[0]] > revision_value_feature_zero \
                    and features[features_list[1]] > revision_value_feature_one:
                outliers_both_features[name] = [(features[features_list[0]], features[features_list[1]]), features["poi"]]
            elif features[features_list[0]] > revision_value_feature_zero:
                outliers_feature_zero[name] = [features[features_list[0]], features["poi"]]
            elif features[features_list[1]] > revision_value_feature_one:
                outliers_feature_one[name] = [features[features_list[1]], features["poi"]]
    print "outliers_both_features", outliers_both_features
    print "\noutliers", features_list[0], outliers_feature_zero
    print "\noutliers", features_list[1], outliers_feature_one

