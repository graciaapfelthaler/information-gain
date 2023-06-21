from pydataset import data
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import math

# calculate entropy regarding the probabilities of occurence
def entropy(df):
    probabilities = []
    for feature in df.unique():
        feature_df = df[df == feature]
        probability = len(feature_df) / len(df)
        probabilities.append(probability)
    entropy = 0
    for prob in probabilities:
        entropy -= prob * math.log2(prob)
    return entropy

# calculate the attribute of your dataset with the highest infomation gain
def information_gain(dataframe, target_feature, list_of_attributes):

    # calculate original entropy
    entropy_0 = entropy(dataframe[target_feature])
    ingain = np.zeros_like((dataframe[list_of_attributes].columns)) + entropy_0

    # iterate through all attributes
    target_values = dataframe[target_feature].unique()
    i = 0
    for attribute in list_of_attributes:
        sum = 0 
        attribute_values = dataframe[attribute].unique()
        for a in attribute_values:
            attribute_short_list = dataframe[dataframe[attribute] == a]
            prob = len(attribute_short_list) / len(dataframe[attribute])
            entropy_i = entropy(attribute_short_list[target_feature])
            sum -= entropy_i * prob
        ingain[i] += sum
        i += 1

    df2 = pd.DataFrame(list(zip(list_of_attributes, ingain)), columns =["attribute", "information_gain"])     
    print(df2)

    highest_gain = df2.max()
    print('\n', 'Choose following attribute for the highest information gain concerning your target feature', target_feature, ':', '\n\n', highest_gain, '\n')

    return
