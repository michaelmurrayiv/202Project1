"""
 Michael Murray
 4/7/22

 This code recursively generates a list of every permutation of the input string, in lexicographic order
"""


def perm_gen_lex(str):
    perm_list = []  # create an empty list to store all the permutations

    # create an internal function that can transform copies of the string into each permutation
    def build_permutations(permutation, str_copy):
        if len(permutation) == len(str):  # add completed permutations to perm_list
            return perm_list.append(''.join(permutation))

        for i in range(len(str_copy)):  # for each character in the input string, run build_permutations
            # removes a character from string_copy and adds it to the permutation
            build_permutations(permutation + str_copy[i], str_copy[:i] + str_copy[i + 1:])

    build_permutations('', str)  # runs the internal function using the user-defined string

    if perm_list == ['']:  # makes sure that an empty string yields an empty list (removes apostrophes)
        perm_list = []

    return perm_list
