from math import ceil

def trainer(wordlist, word, marker):
    """
    Function used to quickly identify the possible word matches from the a given word list
    Precondition: 
        - All words in the list are of same length
        - There are no duplicate words in the list
    Postcondition:
        - List of possible word matches is returned
    Input:
        wordlist: List of N words, where each word is a string of length M, with each character in the range of lowercase {a−z}
        word: Word which you have guessed.It is a string of length M , with each character in the range of lowercase {a − z}
        marker: Array of integers of length M. Each element is in the range {0, 1}, and is used to mark the characters in the guessed word
    Return:
        word_matches: A list of strings containing the valid words, based on the input provided
    Time complexity: 
        Best: O(M)
        Worst: O(NM + NX + XlogN) = O(NM)
    Space complexity: 
        Input: O(N)
        Aux: O(NM)
    """
    new_list = radix_sort_string(wordlist, word, marker)
    word_matches = get_words(word, new_list)
    return word_matches

def radix_sort_string(list, word, marker):
    """
    Function to sort words in the list in lexographical order
    Precondition:
        - All words in the list should be of equal length
        - All characters in the word should be lowercase alphabets
    Postcondition:
        - The returned list should contain the words in lexographical order
    Input:
        list: List of N words, where each word is a string of length M, with each character in the range of lowercase {a−z}
        word: Word which you have guessed.It is a string of length M , with each character in the range of lowercase {a − z}
        marker: Array of integers of length M. Each element is in the range {0, 1}, and is used to mark the characters in the guessed word
    Return:
        new_list: List of possible word matches
    Time complexity: 
        Best: O(N)
        Worst: O(XlogN)
    Space complexity: 
        Input: O(N)
        Aux: O(N)
    N -> Number of words in list
    """
    max_length = len(list[0])
    for i in range(max_length - 1, -1, -1):
        character = word[i]
        # checking if the alphabet is in the correct location
        location = marker[i] == 1
        # sorting the word alphabetically
        new_list = word_sort(list, character, i, location)
    return new_list

def word_sort(list,character,column,location):
    """
    Function used to sort each words in alphabetical order
    Precondition:
        - All words in the list should be of equal length
        - All characters in the word should be lowercase alphabets
    Postcondition:
        - Words should be sorted in alphabetical order
    Input:
        list: List of N words, where each word is a string of length M, with each character in the range of lowercase {a−z}
        character: The current alphabet whose location in the string we are checking
        column: The column number of the alphabet in a word
        location: Boolean variable that checks whether the alphabet is in the correct location or not
    Return:
        list: List of N words, where each word is a string of length M, with each character in the range of lowercase {a−z} which has been sorted in alphabetical order
    Time complexity: 
        Best: O(M)
        Worst: O(MN)
    Space complexity: 
        Input: O(MN)
        Aux: O(NM)
    """
    count = [None] * (26)
    # looping through count array
    for i in range(len(count)):
        count[i] = []

    correct_location = ord(character) - 97
    # loop through words in the list
    for word in list:
        item = ord(word[column]) - 97
        # if the alphabet is present in the appropriate location, then append words which have the alphabet in that specific location to the count array
        if (
            location == True
            and correct_location == item
            or location != True
            and correct_location != item
        ):
            count[item].append(word)
    index = 0
    for i in range(len(count)):
        item = i
        occurrences = len(count[i])
        for j in range(occurrences):
            list[index] = count[i][j]
            index = index + 1

    index = index - 1
    while index != len(list)-1:
        list.pop(len(list)-1)
    return list

def get_words(word,list):
    """
    Function that returns a list of possible words that could be the correct word by calling the counting_sort function
    Precondition:
        - All words in the list should be of equal length
        - All characters in the word should be lowercase alphabets
    Postcondition:
        - List of possible words should be returned
    Input:
        word: Word which you have guessed.It is a string of length M , with each character in the range of lowercase {a − z}
        list: List of N words, where each word is a string of length M, with each character in the range of lowercase {a−z}
    Return:
        possible_words: list of possible words that coul dbe the correct word
    Time complexity: 
        Best: O(N)
        Worst: O(NM)
    Space complexity: 
        Input: O(N)
        Aux: O(N)
    """
    possible_words = []
    for i in range(len(list)):
        sorted_words = counting_sort(list[i])
        possible_words.append(sorted_words)

    word_sort = counting_sort(word)
    for i in range(len(possible_words)):
        possible_words[i] = list[i] if possible_words[i] == word_sort else ""
        # looping through the possible_words list to remove occurrences of ""
    for item in possible_words:
        if item == "":
            possible_words.remove(item)
    return possible_words

def counting_sort(word):
    """
    Function which implemets the counting sort algorithm to sort a word in alphabetical order
    Postcondition:
        - Word is sorted in alphabetical order
    Input:
        word: Word which you have guessed.It is a string of length M , with each character in the range of lowercase {a − z}
    Return:
        sorted_word: Word which has been sorted in alphabetical order
    Time complexity: 
        Best: O(M)
        Worst: O(M)
    Space complexity: 
        Input: O(M)
        Aux: O(1)
     M -> Length of word
    """
    count = [0 for _ in range(27)]
    for x in word:
        count[ord(x)-97] += 1
    sorted_word = ""
    for i in range(len(count)):
        while count[i] > 0:
            sorted_word += chr(97+i)
            count[i] -= 1
    return sorted_word

def local_maximum(M):
    """
    Function to find index of local maximum of a grid of n-by-n grid of distinct numbers
    Precondition:
        - Matrix has equal number of rows and columns
    Postcondition:
        - Index of local maximum is returned
    Input:
        M: n-by-n grid of distinct integers (i.e., an n-by-n matrix)
    Return: 
        index: index of the local maximum
    Time complexity: 
        Best: O(N)
        Worst: O(N)
    Space complexity: 
        Input: O(N)
        Aux: O(N/2)
    """
    # finding number of rows and columns in the matrix
    rows = len(M[:])
    columns = len(M[:][0])
    answer = []
    # if the matrix is not empty, we calculate the local maximum
    if rows and columns != 0:
        local_max = local_max_recursion(M, rows, columns, columns // 2)
        index = index_2d(M,local_max)
        answer.append(index)
    # else we return an empty array
    else:
        answer.append([])
    return answer

def findMax(M, rows, middle,max):
    """
    Function to find the maximum value in the middle column
    Precondition:
        - Matrix has equal number of rows and columns
    Postcondition:
        - Maximum value in the middle column is returned
    Input:
        M: n-by-n grid of distinct integers (i.e., an n-by-n matrix)
        rows: Number of rows in matrix
        columns: Number of columns in matrix
        middle: Middle column of matrix
        max: Maximum value in column
    Return: 
        index: index of the maximum value
        max: maximum value in column
    Time complexity: 
        Best: O(N)
        Worst: O(N)
    Space complexity: 
        Input: O(N^2)
        Aux: O(N/2)
    """
    maximum_index = 0
    for i in range(rows):
        if (max < M[i][middle]):
            # Finding the value of global maximum and its index so that we can check its neighbours
            max = M[i][middle]
            maximum_index = i
    return max,maximum_index
 
def local_max_recursion(M, rows, columns,middle):
    """
    Function to find the peak element using recursion
    Precondition:
        - Matrix has equal number of rows and columns
    Postcondition:
        - Any one local maximum of the matrix is returned
    Input:
        M: n-by-n grid of distinct integers (i.e., an n-by-n matrix)
        rows: Number of rows in matrix
        columns: Number of columns in matrix
        middle: Middle column of matrix
    Return: 
        Value of local maximum
    Time complexity: 
        Best: O(N)
        Worst: O(N)
    Space complexity: 
        Input: O(N^2)
        Aux: O(N/2)
    """
    max = 0
    # Finding maximum value in the middle column
    max, maximum_index = findMax(M, rows, middle, max)
    if middle in [0, columns - 1]:
        return max

    # Checking If the element in the middle column is a local maximum
    if (max >= M[maximum_index][middle - 1] and
        max >= M[maximum_index][middle + 1]):
        return max

    # Checking if the maximum is lesser than elements on its left
    if (max < M[maximum_index][middle - 1]):
        return local_max_recursion(M, rows, columns, middle - ceil(middle / 2.0))

    if(columns > middle+ceil(middle/2.0)):    
        return local_max_recursion(M, rows, columns,middle + ceil(middle / 2.0))
    else:
        return local_max_recursion(M,rows,columns, middle + 1)
 
def index_2d(M,value):
    """
    Function to find index of an element in a matrix
    Postcondition:
        - Index of the value is returned
    Input:
        M: n-by-n grid of distinct integers (i.e., an n-by-n matrix)
        rows: Number of rows in matrix
        columns: Number of columns in matrix
        value: Value to be searched for in matrix
    Return: 
        index: index of the local maximum
    Time complexity: 
        Best: O(N)
        Worst: O(N)
    Space complexity: 
        Input: O(N^2)
        Aux: O(N)
    """
    for i, j in enumerate(M):
        if value in j:
            return [i, j.index(value)]

if __name__ == "__main__":
    wordlist = ["limes", "spare", "store", "loser", "aster", "pares","taser", "pears", "stare", "spear", "parse", "reaps", "rates","tears", "losts"]
    word = "pares"
    marker = [0,0,0,0,1]
    trainer(wordlist, word, marker)

    wordlist = ["limes", "spare", "store", "loser", "aster", "pares","taser", "pears", "stare", "spear", "parse", "reaps", "rates","tears", "losts"]
    word = "spare"
    marker = [1,1,0,0,1]
    trainer(wordlist, word, marker)

    wordlist = ["limes", "spare", "store", "loser", "aster", "pares","taser", "pears", "stare", "spear", "parse", "reaps", "rates","tears", "losts"]
    word = "sprae"
    marker = [1,1,0,0,1]
    trainer(wordlist, word, marker)

    wordlist = ["limes", "spare", "store", "loser", "aster", "pares","taser", "pears", "stare", "spear", "parse", "reaps", "rates","tears", "losts"]
    word = "spare"
    marker = [1,1,1,1,1]
    trainer(wordlist, word, marker)

    wordlist = ["costar", "carets", "recast", "traces", "reacts", "caster","caters", "crates", "actors", "castor"]
    word = "catrse"
    marker = [1,1,0,0,0,0]
    trainer(wordlist, word, marker)
     
    # M1_Actual_Value = [[]]
    M1 = [[]]
    local_maximum(M1)
    
    # M2_Actual_Value = [[1, 1]]
    M2 = [[9,1],
        [2,11]]
    local_maximum(M2)

    # M3_Actual_Value = [[1, 1]]
    M3 = [[99,100],
        [23,213]]
    local_maximum(M3)

    # M4_Actual_Value = [[2, 2]]
    M4= [[1,2,3],
        [3,4,5],
        [6,7,8]]
    local_maximum(M4)

    # M5_Actual_Value = [[2, 1]]
    M5 = [[91,32,13],
        [53,24,45],
        [64,67,28]]
    local_maximum(M5)

    # M6_Actual_Value = [[0, 3]]
    M6 = [[ 1, 2, 27, 28],
        [3, 4, 25, 26],
        [5, 6, 23, 24],
        [7, 8, 21, 22]]
    local_maximum(M6)

    # M7_Actual_Value = [[2,3]]
    M7 = [[1,2,3,4,5],
        [3,4,5,5,6],
        [4,6,7,8,8],
        [3,5,6,6,6],
        [2,3,4,5,6]]
    local_maximum(M7)

    # M8_Actual_Value = [[2,3]]
    M8 = [[12,24,35,42,53],
        [31,43,55,55,62],
        [44,65,77,87,85],
        [36,54,67,62,61],
        [26,32,45,51,68]]
    local_maximum(M8)
    
    # M9_Actual_Value = [[2,2]]
    M9 = [[1,2,3,4,5,6],
        [3,4,5,5,6,5],
        [4,6,12,8,8,3],
        [3,5,6,6,6,5],
        [2,3,4,5,6,3],
        [2,3,4,12,5,5]]
    local_maximum(M9)

    # M10_Actual_Value = [[5,5]]
    M10 = [[1,2,3,4,5,6],
        [3,4,5,5,6,5],
        [4,6,12,8,8,43],
        [3,5,6,6,6,55],
        [2,3,4,5,6,32],
        [2,3,4,12,54,56]]
    local_maximum(M10)

    # M11_Actual_Value = [[1,6]]
    M11 = [[1,2,3,4,5,6,1],
        [3,4,5,5,6,5,9],
        [4,6,9,8,8,4,3],
        [3,5,6,6,6,5,1],
        [2,3,4,5,6,3,1],
        [2,3,4,9,5,5,1],
        [2,3,4,9,5,5,1]]
    local_maximum(M11)

    # M12_Actual_Value = [[0,0]]
    M12 = [[99,99,99,99,99,99],
        [99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99]]
    local_maximum(M12)

    # M13_Actual_Value = [[5,0]]
    M13 = [[1,  3,  6,  10, 15, 21, 28],
        [2,  5,  9,  14, 20, 27, 34],
        [4,  8,  13, 19, 26, 33, 39],
        [7,  12, 18, 25, 32, 38, 90],
        [11, 17, 24, 31, 37, 57, 91],
        [99, 98, 97, 60, 59, 58, 56],
        [22, 29, 35, 40, 44, 55, 49]]
    local_maximum(M13)

    # M14_Actual_Value = [[0,0]]
    M14 = [[0]]
    local_maximum(M14)
    
    # M15_Actual_Value = [[2,9]]
    M15 = [[ 38,  52, -84,  49,  64,  73,  44, -86, -73,  12], 
        [-50,  8,   65,  72,  11, -25,  8,   74,  44, -1 ], 
        [ 42,  94,  0,  -55,  32, -42, -73,  24,  11,  81], 
        [ 82, -88, -20,  99,  23,  79,  89,  0,  -91, -19], 
        [-59,  49, -77,  54, -48,  81, -41, -10, -62,  62], 
        [  0, -41, -54,  99, -62,  39, -38, -55,  79, -71], 
        [ 73, -62, -57, -12,  93,  15, -36,  93,  70, -95], 
        [ 59, -15,  69, -18,  40, -53, -99, -54, -89,  86], 
        [ -1,  81,  6,   93, -60, -29, -85, -6,   64,  16], 
        [-45, -24,  87,  29, -24, -89, -75, -33,  95,  13]]
    local_maximum(M15)
    
    # M16_Actual_Value = [[0,4]]
    M16 = [[77, 24, 89, 75, 96], 
        [47, 77, 26, 26, 58], 
        [82, 51, 26, 60, 51], 
        [98, 61, 90, 70, 75], 
        [12, 43, 96, 51, 59]]
    local_maximum(M16)

    # M17_Actual_Value = [[0,2]]
    M17 = [[81, 26, 97, 89, 40, 19, 70, 93, 76, 93], 
        [18, 69, 77, 30, 76, 70, 46, 25, 26, 26], 
        [17, 63, 2,  58, 96, 45, 95, 69, 63, 62], 
        [17, 68, 24, 80, 88, 45, 2,  80, 79, 0 ], 
        [18, 9,  77, 64, 6,  81, 71, 25, 0,  33], 
        [13, 22, 63, 94, 62, 73, 34, 44, 80, 78], 
        [99, 6,  46, 57, 20, 18, 91, 28, 96, 70], 
        [71, 70, 65, 26, 34, 58, 31, 40, 47, 54], 
        [78, 73, 77, 62, 41, 97, 55, 71, 68, 27], 
        [28, 71, 14, 50, 60, 43, 74, 20, 42, 69]]
    local_maximum(M17)

    # M18_Actual_Value = [[3,15]]
    M18 = [[53, 35, 62, 77, 30, 68, 47, 16, 99, 32, 38, 88, 90, 50, 94, 11, 98, 79, 71, 20], 
        [52, 99, 9,  65, 7,  4,  74, 45, 66, 66, 74, 1,  51, 21, 32, 61, 89, 36, 27, 24], 
        [12, 77, 33, 72, 26, 43, 5,  57, 88, 8,  30, 70, 55, 50, 14, 83, 19, 94, 38, 20], 
        [41, 45, 10, 49, 6,  88, 9,  47, 87, 19, 54, 73, 77, 45, 64, 93, 53, 9,  69, 27], 
        [74, 10, 5,  69, 95, 27, 54, 41, 96, 65, 46, 72, 1,  99, 48, 93, 53, 27, 23, 79], 
        [38, 71, 24, 46, 23, 29, 58, 31, 65, 9,  85, 72, 61, 18, 66, 82, 51, 98, 65, 47], 
        [96, 71, 58, 2,  48, 49, 81, 13, 57, 68, 15, 14, 69, 58, 87, 86, 82, 25, 1,  73], 
        [58, 33, 43, 28, 49, 5,  93, 24, 28, 35, 65, 56, 93, 96, 91, 61, 16, 15, 24, 56], 
        [8,  56, 39, 81, 37, 14, 10, 87, 85, 91, 63, 37, 60, 3,  92, 44, 88, 25, 60, 84], 
        [81, 7,  97, 84, 14, 72, 99, 43, 61, 22, 44, 84, 38, 84, 13, 13, 96, 85, 40, 17], 
        [83, 52, 97, 99, 22, 9,  67, 17, 23, 97, 41, 89, 61, 47, 58, 73, 39, 29, 50, 1 ], 
        [47, 1,  30, 54, 10, 69, 71, 73, 75, 79, 67, 16, 91, 14, 39, 66, 54, 79, 29, 85], 
        [51, 65, 30, 34, 51, 90, 15, 6,  63, 22, 85, 86, 50, 92, 70, 49, 50, 84, 32, 51], 
        [85, 74, 19, 97, 92, 32, 72, 34, 11, 93, 80, 25, 76, 92, 60, 86, 69, 87, 12, 21], 
        [73, 94, 84, 25, 66, 89, 59, 9,  9,  41, 3,  44, 17, 20, 6,  2,  27, 62, 76, 15], 
        [2,  52, 60, 98, 77, 23, 76, 92, 90, 9,  13, 8,  3,  60, 40, 50, 37, 4,  47, 73], 
        [23, 46, 53, 96, 75, 71, 59, 75, 80, 91, 66, 3,  16, 57, 96, 9,  85, 61, 99, 57], 
        [76, 17, 78, 62, 32, 63, 66, 38, 47, 12, 93, 64, 31, 9,  21, 83, 99, 45, 41, 11], 
        [65, 0,  49, 17, 35, 60, 1,  47, 12, 30, 31, 75, 38, 65, 28, 65, 26, 28, 5,  44], 
        [81, 41, 79, 38, 1,  63, 28, 53, 26, 57, 88, 18, 3,  42, 80, 40, 32, 15, 27, 15]]
    local_maximum(M18)

    # M19_Actual_Value = [[0,0]]
    M19 = [[1, 1], [1, 1]]
    local_maximum(M19)

    # M20_Expected_Value = [[0, 6]]
    M20 = [[1,2,  27, 28, 29, 30, 49],
        [3,4,  25, 26, 31, 32, 48],
        [5,6,  23, 24, 33, 34, 47],
        [7,8,  21, 22, 35, 36, 46],
        [9,10, 19, 20, 37, 38, 45],
        [11, 12, 17, 18, 39, 40, 44],
        [13, 14, 15, 16, 41, 42, 43]]
    local_maximum(M20)
   
    # M21_Expected_Value = [[4, 0], [2, 4], [3, 6], [6, 6]] -> Should return any 1 value
    M21 = [[1,  3,  6,  10, 15, 21, 28],
        [2,  5,  9,  14, 20, 27, 34],
        [4,  8,  13, 19, 50, 33, 39],
        [7,  12, 18, 25, 32, 38, 51],
        [52, 17, 24, 31, 37, 42, 46],
        [16, 23, 30, 36, 41, 45, 48],
        [22, 29, 35, 40, 44, 47, 49]]
    local_maximum(M21)
   
    # M22_Expected_Value = [[4, 12]]
    M22 = [[1,   3,   6,   10,  15,  21,  28,  164, 201, 203, 206, 210, 215, 221, 228],
        [2,   5,   9,   14,  20,  27,  34,  163, 202, 205, 209, 214, 220, 227, 234],
        [4,   8,   13,  19,  26,  33,  39,  162, 204, 208, 213, 219, 226, 233, 239],
        [7,   12,  18,  25,  32,  38,  43,  161, 207, 212, 218, 225, 232, 238, 290],
        [11,  17,  24,  31,  37,  42,  46,  160, 211, 217, 224, 231, 909, 908, 907],
        [16,  23,  30,  36,  41,  45,  48,  159, 216, 223, 230, 260, 906, 904, 902],
        [22,  29,  35,  40,  44,  47,  49,  158, 222, 229, 235, 340, 305, 903, 901],
        [51,  52,  53,  54,  55,  56,  57,  157, 506, 505, 504, 503, 502, 501, 650],
        [101, 102, 127, 128, 129, 130, 149, 156, 601, 302, 327, 328, 629, 630, 649],
        [103, 104, 125, 126, 131, 132, 148, 155, 603, 604, 625, 626, 631, 632, 648],
        [105, 106, 123, 124, 133, 134, 147, 154, 605, 606, 623, 624, 633, 634, 647],
        [107, 108, 121, 122, 135, 136, 146, 153, 607, 608, 621, 622, 635, 636, 646],
        [109, 110, 119, 120, 137, 138, 145, 152, 609, 610, 619, 620, 637, 638, 645],
        [111, 112, 117, 118, 139, 140, 144, 151, 611, 612, 617, 618, 639, 640, 644],
        [113, 114, 115, 116, 141, 142, 143, 150, 613, 614, 615, 616, 641, 642, 643]]
    local_maximum(M22)

    M23 = [[727,775,113,951,337,472,354,153,929,857,176,767,912,444,792,889,964,722,321,563,952,246,713,802,218,921,757,795,917,855,913,619,409,40,353,239,182,586,270,862,317,727,218,411,657,705,57,677,438,748],
        [99,431,695,397,788,855,711,574,999,865,71,252,912,700,375,294,654,472,711,193,598,560,356,559,603,874,86,92,908,384,928,167,408,283,119,564,87,264,990,142,581,371,899,108,673,15,695,67,72,379],
        [847,335,8,901,815,612,976,80,496,423,498,721,265,328,809,483,310,110,460,375,408,862,84,409,447,267,759,856,906,656,712,72,683,25,638,692,870,505,187,719,72,980,369,299,207,669,282,984,617,690],
        [182,911,432,56,68,669,503,200,712,912,562,412,54,143,836,140,83,321,944,651,759,675,404,114,454,396,621,614,892,836,841,27,85,675,591,959,598,545,303,72,435,271,825,706,374,719,247,565,93,789],
        [72,884,125,733,15,667,313,941,634,820,206,152,602,29,980,886,301,934,383,599,765,63,878,413,316,79,713,942,937,399,336,369,935,331,746,628,998,69,846,273,604,412,214,364,434,818,143,404,537,98],
        [480,186,414,769,674,872,838,884,872,128,636,61,115,547,748,678,621,320,776,800,294,668,371,612,568,289,145,142,235,962,706,19,707,417,447,311,780,598,747,120,109,798,967,631,646,525,216,769,55,329],
        [521,799,593,165,68,644,604,924,248,55,394,583,56,746,185,471,757,111,47,26,429,590,426,417,633,771,192,680,648,179,242,351,722,983,169,478,549,767,750,889,488,322,293,982,129,238,255,153,734,682],
        [712,791,332,151,437,995,591,251,192,754,315,675,806,141,983,352,12,889,304,873,850,951,860,664,388,506,67,993,614,449,323,704,986,887,24,955,663,25,970,332,547,641,76,853,707,79,767,721,806,832],
        [979,121,997,457,636,550,934,522,929,582,852,500,428,364,968,734,276,449,360,647,545,278,459,398,11,795,913,669,769,47,709,582,836,101,461,620,188,833,807,314,845,204,485,370,519,292,73,376,887,175],
        [577,68,320,586,460,134,118,369,692,787,205,371,498,531,292,257,394,503,87,449,918,831,863,115,932,789,561,90,1,965,264,817,929,878,152,224,939,581,756,945,836,283,188,32,170,818,171,929,292,737],
        [999,234,773,648,229,87,596,806,584,624,62,604,312,333,172,237,285,243,780,290,79,378,250,542,648,21,33,557,935,104,686,108,931,874,97,25,267,804,724,283,306,746,198,368,566,232,269,905,925,739],
        [587,730,124,831,989,267,612,740,494,370,734,961,536,813,117,117,4,61,590,72,816,865,983,233,790,540,27,486,602,19,35,940,501,968,660,547,86,425,320,378,700,749,962,279,251,494,449,37,127,274],
        [864,704,450,880,637,871,622,308,644,211,491,43,58,696,277,382,487,638,315,351,562,909,259,746,20,731,147,892,622,407,849,600,461,897,721,469,33,681,372,430,35,560,239,484,824,833,550,519,910,188],
        [731,932,186,620,796,883,51,980,394,333,499,533,794,202,450,904,320,500,488,827,783,53,909,110,44,639,882,12,175,50,432,60,573,44,817,806,440,17,905,348,665,442,645,779,84,237,298,105,489,171],
        [56,335,537,879,813,993,347,127,677,824,109,638,112,944,710,482,290,848,894,215,604,646,857,213,615,95,163,455,558,182,886,491,145,415,330,760,849,537,50,696,522,555,960,333,955,7,209,615,274,999],
        [349,935,571,630,705,372,900,716,981,392,418,795,453,563,470,258,632,545,379,654,280,374,922,377,20,396,618,417,786,622,736,880,576,597,26,762,877,121,524,121,950,554,630,212,475,348,776,729,390,637],
        [692,626,973,425,521,403,723,464,28,938,673,173,996,536,895,682,742,282,317,870,402,775,896,755,838,26,120,397,196,841,243,392,590,901,445,31,412,576,277,309,186,707,464,695,459,554,587,778,577,546],
        [519,304,560,991,638,198,516,618,707,53,863,506,49,560,181,700,947,51,363,977,87,496,121,887,418,322,146,430,867,794,797,480,758,714,437,695,470,971,244,83,47,200,683,560,375,880,591,876,695,959],
        [94,188,415,982,986,328,322,547,97,917,768,796,728,572,631,358,852,870,218,869,431,851,957,256,19,255,343,462,533,292,278,616,655,724,527,101,250,766,978,576,30,514,713,336,118,745,847,929,325,253],
        [40,75,719,226,500,291,817,47,610,792,574,875,441,421,202,244,940,486,324,643,492,200,773,410,880,795,592,852,704,749,388,270,890,777,849,792,515,920,617,91,736,277,356,159,294,998,610,105,175,938],
        [269,295,893,493,259,275,429,229,736,341,803,731,102,607,796,642,237,203,523,877,646,973,236,673,387,596,348,597,947,457,42,847,714,732,866,861,6,459,973,793,224,929,983,246,510,834,171,423,80,527],
        [984,615,5,272,441,95,586,282,921,967,972,700,222,6,660,184,890,413,306,78,299,716,262,939,162,229,18,492,370,263,955,259,115,967,456,398,83,934,962,70,376,281,794,175,31,30,482,537,143,300],
        [391,80,982,847,226,201,962,241,3,127,276,887,706,936,821,504,426,668,814,632,533,583,461,663,77,865,786,933,431,545,46,383,390,524,985,773,947,404,499,683,157,532,728,234,304,739,462,800,344,458],
        [609,301,736,653,665,365,748,520,430,95,388,617,324,692,223,993,420,253,628,831,86,107,59,614,415,254,401,694,35,808,953,377,456,339,326,177,977,931,373,892,175,650,650,862,918,586,702,658,895,111],
        [959,954,562,277,397,51,109,134,244,425,746,64,129,738,639,822,852,922,24,388,898,736,520,426,914,284,406,686,39,973,289,233,923,957,131,219,635,75,685,918,965,999,699,233,237,149,758,77,453,149],
        [157,110,32,326,667,350,455,318,68,373,792,150,471,441,365,616,630,497,985,321,158,378,353,281,552,675,333,970,663,142,442,285,595,97,328,129,812,945,874,271,93,792,935,483,485,42,34,123,706,342],
        [989,450,864,115,738,5,912,608,271,914,215,106,698,452,421,322,626,456,451,571,616,231,309,411,677,400,53,221,462,335,619,998,31,492,892,597,807,586,652,354,953,111,4,290,878,438,504,290,783,315],
        [793,115,67,468,509,421,949,117,508,907,745,637,244,350,70,908,154,270,36,935,313,682,641,522,112,691,273,588,614,373,829,456,235,28,968,498,229,503,424,174,193,852,645,178,43,421,84,161,962,944],
        [902,308,840,162,622,829,301,588,308,513,45,888,375,965,626,613,220,331,909,790,611,432,965,577,898,172,252,695,901,745,86,641,333,660,807,670,333,854,555,300,189,209,972,208,957,787,111,566,29,974],
        [614,476,686,699,662,189,453,368,944,252,62,445,440,280,249,593,105,366,346,765,495,660,913,463,171,124,152,31,910,676,367,735,97,624,672,566,571,716,153,141,406,970,945,700,340,760,165,330,457,296],
        [323,781,777,55,158,460,41,194,895,717,872,301,362,354,85,749,324,926,361,325,559,427,22,78,776,498,464,576,458,66,507,728,452,728,262,927,336,78,422,347,425,132,781,9,605,876,626,693,686,321],
        [86,19,686,575,444,118,974,149,177,169,371,949,693,453,512,804,357,33,722,125,514,655,238,369,862,394,661,329,562,358,864,332,721,23,316,351,361,58,494,309,573,271,601,142,100,705,7,11,524,796],
        [849,183,73,871,140,606,575,634,184,894,172,374,380,830,879,258,692,556,140,43,567,743,108,607,348,682,149,89,778,521,901,187,280,604,929,960,337,521,164,277,295,894,307,425,694,728,831,355,75,651],
        [957,787,646,840,771,856,741,532,362,243,51,882,842,412,222,382,876,395,627,942,794,191,455,297,29,776,618,11,152,529,578,438,444,386,759,582,931,54,291,468,931,639,648,248,952,945,909,26,288,5],
        [5,529,141,715,923,581,331,286,321,186,322,929,115,634,307,864,779,643,8,242,699,166,119,941,386,217,703,325,832,671,989,202,40,13,646,150,11,540,335,898,824,430,371,193,372,819,491,46,255,93],
        [395,652,603,917,722,134,928,264,490,469,998,426,607,260,197,87,416,257,658,170,618,400,103,548,418,234,999,389,200,868,345,488,877,465,150,810,232,395,211,534,624,792,661,815,106,530,800,279,428,667],
        [299,138,473,296,84,570,265,585,419,318,736,886,809,38,251,78,566,306,2,614,297,589,497,208,468,755,611,181,746,23,478,363,889,276,462,660,101,349,582,110,847,649,927,436,798,769,625,422,230,402],
        [821,251,190,582,63,30,238,763,994,394,459,339,547,305,954,298,768,805,469,648,235,625,556,568,904,758,736,159,349,628,516,106,54,817,830,193,142,936,474,728,374,492,580,133,280,701,459,22,235,387],
        [570,143,263,45,742,710,186,993,294,644,333,810,651,938,18,153,827,576,194,959,709,785,788,144,601,48,83,547,393,479,187,592,382,994,679,838,179,376,839,785,555,713,720,379,622,497,394,396,994,979],
        [310,293,898,497,407,64,106,759,79,601,396,876,996,513,480,89,234,292,467,439,60,828,95,228,996,957,372,977,463,316,113,181,696,83,672,125,5,866,391,411,297,182,807,686,343,526,504,337,328,846],
        [204,554,385,819,149,179,284,72,710,488,375,994,907,403,740,714,43,352,816,572,78,740,626,589,491,832,852,836,643,770,567,236,976,986,321,854,658,922,845,208,795,467,720,425,8,624,517,532,17,613],
        [961,795,682,934,814,641,265,889,60,922,517,723,8,145,541,301,976,640,60,684,210,557,887,438,420,504,915,645,314,493,574,803,770,225,686,774,762,37,561,460,546,86,262,185,456,385,453,174,588,530],
        [129,735,658,396,955,244,172,962,519,236,784,50,661,333,388,597,275,55,883,738,79,966,163,996,603,792,427,777,6,859,586,452,172,102,722,677,381,495,126,339,391,552,277,540,351,135,208,40,816,962],
        [556,235,489,418,946,721,30,883,351,709,165,265,920,779,303,502,610,707,702,729,169,988,924,532,765,248,282,941,797,561,291,621,330,198,369,141,393,383,462,672,504,620,226,697,332,873,580,72,903,550],
        [984,556,879,527,641,262,127,315,602,215,975,250,229,711,73,760,880,844,908,22,483,799,424,663,195,322,69,361,258,421,468,908,166,455,206,207,806,325,852,361,401,944,63,534,289,561,661,788,24,633],
        [160,386,658,237,389,2,193,951,874,312,717,64,439,111,51,706,591,587,376,965,696,432,179,327,335,538,254,86,814,520,313,227,94,477,962,164,956,241,840,177,988,463,233,952,4,287,396,935,990,386],
        [30,306,405,43,78,748,237,312,450,794,957,674,336,588,294,854,208,335,263,908,24,137,984,670,411,549,503,220,241,41,237,274,915,256,939,288,650,640,885,813,666,714,795,241,799,498,654,87,12,893],
        [672,271,989,681,158,368,208,549,102,717,459,761,12,131,805,620,555,531,829,665,170,913,354,606,223,90,150,286,779,590,221,595,296,296,461,359,443,913,587,7,476,430,737,292,945,817,185,150,886,646],
        [467,605,47,663,670,181,949,932,687,106,534,375,468,257,469,64,693,941,853,681,533,200,554,608,129,584,452,155,882,325,999,604,310,110,224,517,860,393,431,729,181,729,213,998,119,325,108,416,898,139],
        [534,237,572,785,822,590,6,974,395,690,360,249,589,477,277,507,21,742,544,395,577,662,423,211,153,725,206,449,634,468,494,237,433,521,9,66,226,814,970,653,980,364,10,795,127,159,388,353,557,37]]
    local_maximum(M23)