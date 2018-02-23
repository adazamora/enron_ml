from collections import defaultdict


def count_num_of_pois(data_dict):
    num_pois = 0
    for name, features in data_dict.iteritems():
        if features["poi"] == 1:
            num_pois += 1
    return num_pois


def count_missing_values_per_feature(data_dict):
    missing_dict = defaultdict(int)
    for name, features in data_dict.iteritems():
        for ft_name, ft_value in features.iteritems():
            if ft_value == "NaN":
                missing_dict[ft_name] += 1
    return missing_dict
