import numpy as np


class NFRParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(classes, nfr_values, ahp_values):
        """
        This function converts nfr input to nfr matrix
        :param classes: set, a set of classes in project
        :param nfr_values: dict, a odict that stores the classes and a dict of nfr weight and it's value as it's value
        :param ahp_values: dictionary, a dictionary that map each nfr to it's ahp
        :return: tuple holds dictionary that map each class to it's index in nfr matrix and numpy matrix that represents nfr
         matrix
        """
        classes_map = {}
        i = 0
        for className in classes:
            classes_map[className] = i
            i += 1

        nfr_matrix = [[0 for x in range(len(classes))] for y in range(len(classes))]  # fill matrix with 0
        for i, class1 in enumerate(classes):
            nfr_matrix[classes_map[class1]][classes_map[class1]] = 1
            for j, class2 in enumerate(classes, i + 1):
                nfr_dim_value = 0
                for nfr in ahp_values:
                    nfr_dim_value += (ahp_values[nfr] * (1 - abs((nfr_values[class1][nfr] - nfr_values[class2][nfr]))))

                nfr_matrix[classes_map[class1]][classes_map[class2]] = nfr_dim_value
                nfr_matrix[classes_map[class2]][classes_map[class1]] = nfr_dim_value

        return {'classes': classes_map, 'matrix_classes': np.matrix(nfr_matrix)}
