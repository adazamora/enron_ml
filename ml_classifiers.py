from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


# The code from line 9 to line 15 is taken from Udacity's code in tester.py
PERF_FORMAT_STRING = "\
\tAccuracy: {:>0.{display_precision}f}\t\tPrecision: {:>0.{display_precision}f}\tRecall: {:>0.{display_precision}f}"
PERF_FINAL_FORMAT_STRING = "\
Accuracy: {:>0.{display_precision}f}\tPrecision: {:>0.{display_precision}f}\t\
Recall: {:>0.{display_precision}f}\t\tF1: {:>0.{display_precision}f}"
RESULTS_FORMAT_STRING = "Total predictions: {:4d}\tTrue positives: {:4d}\tFalse positives: {:4d}\
\tFalse negatives: {:4d}\tTrue negatives: {:4d}"


def test_classifier_sss(clf, features, labels, is_final=False):
    """
    Test a classifier's performance using StratifiedShuffleSplit calculating and printing its accuracy, precision and
    recall
    :param clf: machine learning classifier
    :param is_final: if True, also calculates and print f1 score and prints the number of predictions made
    """
    sss = StratifiedShuffleSplit(n_splits=1000, test_size=0.3, random_state=123)
    true_negatives = 0
    false_negatives = 0
    true_positives = 0
    false_positives = 0
    for train_index, test_index in sss.split(features, labels):
        # From this line on, I copied the code from the test_classifier function in tester.py
        features_train = []
        features_test = []
        labels_train = []
        labels_test = []
        for ii in train_index:
            features_train.append(features[ii])
            labels_train.append(labels[ii])
        for jj in test_index:
            features_test.append(features[jj])
            labels_test.append(labels[jj])
        # Fit the classifier using training set, and test on test set
        clf.fit(features_train, labels_train)
        predictions = clf.predict(features_test)
        for prediction, truth in zip(predictions, labels_test):
            if prediction == 0 and truth == 0:
                true_negatives += 1
            elif prediction == 0 and truth == 1:
                false_negatives += 1
            elif prediction == 1 and truth == 0:
                false_positives += 1
            elif prediction == 1 and truth == 1:
                true_positives += 1
            else:
                print "Warning: Found a predicted label not == 0 or 1."
                print "All predictions should take value 0 or 1."
                print "Evaluating performance for processed predictions:"
                break
    try:
        total_predictions = true_negatives + false_negatives + false_positives + true_positives
        accuracy = 1.0 * (true_positives + true_negatives) / total_predictions
        precision = 1.0 * true_positives / (true_positives + false_positives)
        recall = 1.0 * true_positives / (true_positives + false_negatives)
        f1 = 2.0 * true_positives / (2 * true_positives + false_positives + false_negatives)
        if is_final:
            print PERF_FINAL_FORMAT_STRING.format(accuracy, precision, recall, f1, display_precision=5)
            print RESULTS_FORMAT_STRING.format(total_predictions, true_positives, false_positives, false_negatives,
                                               true_negatives)
        else:
            print PERF_FORMAT_STRING.format(accuracy, precision, recall, display_precision=3)
            print ""
    except:
        print "Got a divide by zero when trying out:", clf
        print "Precision or recall may be undefined due to a lack of true positive predictions."


def scale_features(features):
    """
    Scales features using MinMaxScaler and RobustScaler
    :return: features with the min_max_scaler, features with the robust scaler
    """
    # Scaling the features with min_max scaler
    min_max_scaler = MinMaxScaler()
    features_min_max = min_max_scaler.fit_transform(features)

    # Scaling the features with robust scaling
    robust_scaled = RobustScaler()
    features_robust = robust_scaled.fit_transform(features)
    return features_min_max, features_robust


def scaled_features_classifier_evaluation(classifier, features, labels):
    """
    Evaluates a classifier using non scaled features, min_max scaled and robust scaled features
    with test_classifier_sss function.
    :param classifier: Name of the machine learning classifier
    """
    features_min_max, features_robust = scale_features(features)

    # Doing some work on the titles display
    name_classifier = str(classifier)
    first_parenthesis = name_classifier.find("(")
    name_to_display = name_classifier[:first_parenthesis]
    if name_to_display == "Pipeline":
        clf_position = name_classifier.find("'clf',")
        next_parentheses = name_classifier.find("(", clf_position)
        new_name_to_display = name_classifier[clf_position + 7: next_parentheses]
        print new_name_to_display + ":"
    else:
        print name_to_display + ":"

    # Printing and classifying the features
    print "\nFeatures non-scaled"
    test_classifier_sss(classifier, features, labels)
    print "Features min max scaled"
    test_classifier_sss(classifier, features_min_max, labels)
    print "Features robust scaled"
    test_classifier_sss(classifier, features_robust, labels)


def evaluate_algorithms(features, labels):
    """
    Given some features and labels, uses them as input to DecisionTree, GaussianNB and Kneighbors classifiers,
    does feature selection on GaussianNB and Kneighbors and prints outs the accuracy, precision and recall
    """
    print "DecisionTreeClassifier:"
    test_classifier_sss(DecisionTreeClassifier(), features, labels)
    scaled_features_classifier_evaluation(GaussianNB(), features, labels)
    scaled_features_classifier_evaluation(KNeighborsClassifier(), features, labels)
