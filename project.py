from pydataset import data
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import math

URL="https://www2.cs.arizona.edu/classes/cs120/fall17/ASSIGNMENTS/assg02/Pokemon.csv"
pokemon = pd.read_csv(URL)
legendary = pokemon['Legendary']
attack = pokemon['Attack']
defense = pokemon['Defense']
hp = pokemon['HP']
values = legendary.unique()
first = pokemon[pokemon.Legendary != values[0]]
second = pokemon[pokemon.Legendary != values[1]]


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

def information_gain(dataframe, target_feature, list_of_attributes):

    entropy_0 = entropy(dataframe[target_feature])
    ingain = np.zeros_like((dataframe[list_of_attributes].columns)) + entropy_0
    print(ingain)

    target_values = dataframe[target_feature].unique()
    i = 0
    for attribute in list_of_attributes:
        sum = 0 
        attribute_values = dataframe[attribute].unique()
        #print(attribute_values)
        for a in attribute_values:
            attribute_short_list = dataframe[dataframe[attribute] == a]
            #print(attribute_short_list)
            prob = len(attribute_short_list) / len(dataframe[attribute])
            #print(prob)
            entropy_i = entropy(attribute_short_list[target_feature])
            sum -= entropy_i * prob
            #print(sum)
        ingain[i] += sum
        i += 1

    df2 = pd.DataFrame(list(zip(list_of_attributes, ingain)), columns =["attribute", "information_gain"])     
    print(df2)

    highest_gain = df2.max()
    print('\n', 'Choose following attribute for the highest information gain concerning your target feature', target_feature, ':', '\n\n', highest_gain, '\n')

    return 0

information_gain(pokemon, 'Legendary', ['Type 1', 'Type 2', 'Generation'])
