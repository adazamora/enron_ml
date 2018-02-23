
def compute_fraction(numerator, denominator):
    if numerator == "NaN" or numerator == 0 or denominator == "NaN" or denominator == 0:
        return 0.
    else:
        return float(numerator)/denominator


def add_poi_fraction_to_dict(data_dict, new_feature_name, numerator_feature, denominator_feature):
    """
    Adds a new feature(corresponding to the division between two existing features) to the data dictionary
    :param data_dict: ictionary where each key is a string with a person's name and the value is another
    dictionary with the features associated to that person.
    :param new_feature_name: string containing the new feature name
    """
    for name, features in data_dict.iteritems():
        numerator = features[numerator_feature]
        denominator = features[denominator_feature]
        fraction = compute_fraction(numerator, denominator)
        features[new_feature_name] = fraction


def add_sum_values_to_dict(data_dict, new_feature_name, feature1, feature2):
    """
    Adds a new feature(corresponding to the sum between two existing features) to the data dictionary
    :param data_dict: ictionary where each key is a string with a person's name and the value is another
    dictionary with the features associated to that person.
    :param new_feature_name: string containing the new feature name
    """
    for name, features in data_dict.iteritems():
        ft1 = features[feature1]
        ft2 = features[feature2]
        if ft1 == "NaN" or ft2 == "NaN":
            features[new_feature_name] = 0
        else:
            sum_two_ft = ft1 + ft2
            features[new_feature_name] = sum_two_ft
