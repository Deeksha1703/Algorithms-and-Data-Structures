def ideal_place(relevant):
    """
    Returns a location that is the minimum amount of combined distance to any relevant point.
    Input:
        - relevant: The location that we want the minimum distance to
    Returns:
        - Single location, that has a minimum combined distance from any relevant point.
    Time Complexity:
        Best: O(1)
        Worst: O(N)
    Space Complexity:
        Best: O(1)
        Worst: O(N)
    N -> number of relevant points
    """
    desired_place = [find_median(relevant, 0),find_median(relevant, 1)]
    return desired_place

def find_median(relevant, index):
    """
    Function to return the median value out of the relevant points, on a particular axis
    Input:
        - relevant: Locations on our grid that we want the minimum distance to
        - index: The index of the axis in the relevant points that we want to find
    Returns:
        - Median value from a particular index
    Time Complexity:
        Best: O(1)
        Worst: O(N)
    Space Complexity:
        Best: O(1)
        Worst: O(N)
    N -> number of relevant points
    """
    length_of_arry = len(relevant)
    median_index = length_of_arry//2
    arry_on_axis = [relevant[i][index] for i in range(length_of_arry)]

    desired_value = quick_select(arry_on_axis, 0, length_of_arry-1, median_index)
    return desired_value

def quick_select(array, low, high, k):
    """
    Implementation of quick sort algorithm to select the kth element from a list using partitioning
    Parameters:
        - array: Array of integers that we want to perform the quick select on
        - low: Lower bound index for the integer that we want to search for
        - high: Higher bound index for the integer that we want to search for
        - k: Index of the element we want to find
    Returns:
        - The kth element, from an array
    Time Complexity:
        Best: O(1)
        Worst: O(N)
    Space Complexity:
        Best: O(1)
        Worst: O(logN)
    N -> number of items in the array
    """
    if len(array)== 1:
        return array[k]
    pivot = median_of_medians(array)
    mid = partition(array, low, high, pivot)
    if k > mid:
        return quick_select(array, mid+1, high, k)
    elif mid > k:
        return quick_select(array, low, mid-1, k)
    else:
        return array[k]

def median_of_medians(array):
    """
    Median selection algorithm used to find a good pivot
    Input:
        - array: Array of integers we want to find the approximate median for
    Returns:
        - A median value that can be used as apivot
    Time Complexity:
        Best: O(1)
        Worst: O(N)
    Space Complexity:
        Best: O(1)
        Worst: O(logN)
    N -> number of items in the array
    """
    n = len(array)
    if n <= 5:
        return insertion_sort(array)
    medians = [insertion_sort(array[5*i:5*i+5]) for i in range(n//5)]
    return quick_select(medians, 0, len(medians), len(medians)//2)    

def insertion_sort(array):
    """
    Sorting algorithm that places the input element at its suitable place in each pass
    Input:
        - array: The list that needs to be sorted
    Returns:
        - The median in the sorted list
    Time Complexity:
        Best: O(N)
        Worst: O(N^2)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    N -> number of items in the array
    """
    arry_length = len(array)
    for i in range (1, arry_length):
        pointer = array[i]
        j = i-1
        while j >= 0 and pointer < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = pointer
    return array[arry_length//2]

def partition(array, low, high, pivot):
    """
    Splits up the algorithm, and partitions them into two sides, based on a pivot.
    Parameters:
        - array: The list that needs to be partitioned
        - low: The lower bound index for what we want to partition
        - high: The higher bound index for what we want to partition
        - pivot:The item we want to partition the list around.
    Returns:
        - The mid point in the array after partitioning has been done
    Time Complexity:
        Best: O(1)
        Worst: O(N)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    N -> number of items in the array
    """
    for i in range(low, high):
        if array[i] == pivot:
            swap(array, high, i)
            break
 
    v = array[high]
    i = low
    for j in range(low, high):
        if (array[j] <= v):
            swap(array, i, j)
            i += 1
    swap(array, i, high)
    return i

def swap(array, i, j):
    """
    Function to swap two elements in an array
    Input:
        - array: The array in whose elements need to be swapped
        - i: Index of the first item to be swapped
        - j: Index of the second item we want swapped
    Returns:
        - Nothing
    Time Complexity:
        Best: O(1)
        Worst: O(1)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    """
    array[i],array[j] = array[j],array[i]

class MinHeap():    #MinHeap class needed for question2
    def __init__(self, max_size: int) -> None:
        """
        Method to initialise the heap
        Input:
            - self: Instance of the MinHeap class
            - max_size: maximum size of heap
        Returns:
            - None
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        self.length = 0
        self.the_array = [0]*(max_size+1)

    def __len__(self) -> int:
        """
        Returns the number of elements in the heap
        Input:
            - self: Instance of the MinHeap class
        Returns:
            - Number of elements in the heap 
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        return self.length

    def is_full(self) -> bool:
        """
        Checks if the heap is full
        Input:
            - self: Instance of the MinHeap class
        Returns:
            - True if the heap is full, else false
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :precondition: 
            - 1 <= k <= self.length
        Input:
            - self: Instance of the MinHeap class
            - k: index of element
        Returns:
            - None
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        item = self.the_array[k]
        while k > 1 and item[1] < self.the_array[k // 2][1]:
            self.the_array[k] = self.the_array[k // 2]
            k //= 2
        self.the_array[k] = item

    def add(self, element) -> bool:
        """
        Swaps elements while risingInput:
        Input:
            - self: Instance of the MinHeap class
            - element: element to be swapped
        Returns:
            - None
        Time complexity: 
            Best: O(1)
            Worst: O(N)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def smallest_child(self, k: int) -> int:
        """
        Returns the index of k's child with greatest value.
        :precondition: 
            - 1 <= k <= self.length // 2
        Input:
            - self: Instance of the MinHeap class
            - k: Index
        Returns:
            - Index of K's child with greatest value
        Time complexity: 
            Best: O(1)
            Worst: O(N)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        if 2 * k == self.length or \
                self.the_array[2 * k][1] < self.the_array[2 * k + 1][1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ 
        Make the element at index k sink to the correct position.
        :precondition: 
            - 1 <= k <= self.length // 2
        Input:
            - self: Instance of the MinHeap class
            - k: index
        Returns:
            - Index of k's child with greatest value
        Time complexity: 
            Best: O(logN)
            Worst: O(logN)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k)
            if self.the_array[min_child][1] >= item[1]:
                break
            self.the_array[k] = self.the_array[min_child]
            k = min_child

        self.the_array[k] = item
        
    def get_min(self):
        """ 
        Removes the minimum element from the heap and returns its value 
        Input:
            - self: Instance of the MinHeap class
        Returns:
            - minimum_value: minimum value in the heap 
        Time complexity: 
            Best: O(N)
            Worst: O(N)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        if self.length == 0:
            raise IndexError

        min_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return min_elt
    

    def update(self,v):
        """
        Updates new distance to a pre-existing vertex
        Input:
            - self: Instance of the MinHeap class
            - v: vertex whose distance needs to be updated
        Returns:
            - None
        Time complexity: 
            Best: O(N)
            Worst: O(N)
        Space complexity: 
            Input: O(1)
            Aux: O(N)
        """
        start = self.the_array[1]
        iter = 1
        while iter < self.length:
            if start[0] == v[0]:
                start = v
            elif v[0] > start[0]:
                iter = (iter*2)+1
            else:
                iter *= 2
    
    def get_distance(self,v):
        """
        Returns the distance of a particular vertex
        Input:
            - self: Instance of the MinHeap class
            - v: vertex whose distance needs to be updated
        Returns:
            - distance of vertex
        Time complexity: 
            Best: O(N)
            Worst: O(N)
        Space complexity: 
            Input: O(1)
            Aux: O(N)
        """
        start = self.the_array[1]
        iter = 1
        for i in range(1,self.length):
            if self.the_array[i][0] == v:
                return self.the_array[i][1]

class Node: # Node class needed for question 2
    """
    Implementation of a generic node class
    """
    def __init__(self,value):
        """
        Function to initialise the node object
        Input:
            - self: Instance of the Node class
        Returns:
            - None
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        self.vertex = value
        self.edges = []
        self.visited = False
        self.discovered = False
    
    def printEdges(self):
        """
        Function to print each edge along with its weight
        Input:
            - self: Instance of the Node class
        Returns:
            - None
        Time complexity: 
            Best: O(E)
            Worst: O(E)
        E -> Number of edges
        Space complexity: 
            Input: O(1)
            Aux: O(E)
        """
        for i in self.edges:
            print(f"Edge to {str(i.v)} with a weight of {str(i.w)}")
            
class Edge: # Edge class needed for question 2
    """
    Class for edge data
    """
    def __init__(self,u,v,w):
        """
        Function to initialise the edge object
        """
        self.u = u
        self.v = v
        self.w = w

class RoadGraph:
    def __init__(self,roads):
        """
        Function to initialise the RoadGraph object
        Input:
            - self: Instance of the Node class
            - roads: A list of roads roads represted as a list of tuples (u, v, w), u is the starting location ID for a road, 
              v is the ending location ID for a road, w is the distance along that road,
        Returns:
            - None
        Time complexity: 
            Best: O(1)
            Worst: O(N)
        Space complexity: 
            Input: O(1)
            Aux: O(N)
        """
        max_vertex= roads[0][0]
        for i in range(len(roads)):
            if roads[i][0] > max_vertex:
                max_vertex = roads[i][0]
        self.V = max_vertex
        self.graph = [None] * (self.V+1)
        self.edges = [[-1 for _ in range(max_vertex)] for _ in range(max_vertex)]
        self.visited = []
        print(self.graph)
        self.createGraph(roads)

    def createGraph(self,roads):
        """
        Function to create graph using the starting location, ending location and distance givwn in the roads list
        Input:
            - self: Instance of the Node class
            - roads: A list of roads roads represted as a list of tuples (u, v, w), u is the starting location ID for a road, 
              v is the ending location ID for a road, w is the distance along that road,
        Returns:
            - None
        Time complexity: 
            Best: O(1)
            Worst: O(V*N)
        N -> Length of roads list
        Space complexity: 
            Input: O(1)
            Aux: O(E)
        """
        for j in range(self.V+1):
            self.graph[j] = (Node(j))
        print(self.graph)
        for k in roads:
            self.graph[k[0]].edges.append(Edge(k[0],k[1],k[2]))

    def printGraph(self):
        """
        Function to print each vertex in the graph
        Input:
            - self: Instance of the Node class
        Returns:
            - None
        Time complexity: 
            Best: O(N)
            Worst: O(N)
        N -> Length of graph
        Space complexity: 
            Input: O(1)
            Aux: O(N)
        """
        for i in self.graph:
            print(i.vertex)
            i.printEdges()
    
    def dijkstra(self, start):
        """
        Function to implement Djikstra's algorithm
        Precondition: 
            - Weight of the edges has to be non negative
            - Graph should be finite
        Postcondition:
            - Shortest distance should be returned
        Input:
            - start: Integer that represents the starting location of your journey. Your route must begin from this location.
        Return:
            - distance: Shortest distance from starting point to all other points
            - vertices: Vertex that has the least distance value
        Time complexity: 
            Best: O(V^2) 
            Worst: O(ElogV)
        where E is the set roads and V is the set of unique locations in roads
        Space complexity: 
            Input: O(1)
            Aux: O(|V|+|E|)
        """
        vert = start
        discover_queue = MinHeap(self.V)
        discover_queue.add((vert,0,0))
        distances = [(float("inf"),0)]*(self.V)
        vertices = [None] * (self.V)
        for i in range(len(vertices)):
            vertices[i] = []
        distances[vert] = (0,0)

        while discover_queue.length != 0:
            min = discover_queue.get_min()
            self.graph[min[0]].visited = True
            count = 0
            for edge in self.graph[min[0]].edges:
                if self.graph[edge.v].visited != True:
                    if self.graph[edge.v].discovered == False:
                        discover_queue.add((edge.v,min[1]+edge.w))
                        distances[count] = (min[1]+edge.w,edge.v)
                        vertices[count].append(min[1])
                        self.graph[edge.v].discovered = True
                    elif distances[edge.v][0] > min[1]+edge.w:
                        discover_queue.update((edge.v,min[1]+edge.w))
                        distances[count] = (min[1]+edge.w,edge.v)
                        vertices[count].append(min[1])
                        self.graph[edge.v].discovered = True

                count = count + 1
        #reset status of vertices      
        for vert in self.graph:
            vert.discovered = False
            vert.visited = False

        print(distances)
        return distances, vertices

    def routing(self,start,end,chores_location):
        """
        Function to return the shortest route from the start location to the end location, going through at least 1 of the locations listed in chores_location.
        Precondition: 
            - The function should go through at least one chore location 
        Postcondition:
            - The shortest route is returned
        Input:
            - start: Integer that represents the starting location of your journey. Your route must begin from this location.
            - end: Non-negative integer that represents the ending location of your journey. Your route must end in this location.
            - chores_location: Non-empty list of non-negative integers that stores all of the locations where your chores could be performed.
        Return:
            sum[i]: shortest route from start location to the end location
        Time complexity: 
            Best: 
            Worst: O(|E|log|V|)
        Space complexity: 
            Input: O(1)
            Aux: 0(|V|+|E|)
        """
        start_location,paths_s = self.dijkstra(start)
        end_location,paths_e = self.dijkstra(end)
	
        new_start = []
        new_end = []
        new_vertices_start = []
        new_vertices_end = []
        for i in range(len(start_location)):
            if start_location[i][0] in chores_location:
                new_start.append(start_location[i])
                new_vertices_start.append(paths_s[i])
		
            if end_location[i][0] in chores_location:
                new_end.append(end_location[i])
                new_vertices_end.append(paths_e[i])	

        sum = []
        for i in range(len(new_start)):
            if new_start[i] == end:
                continue
            else:
                sum[i] = (new_start[i][0],new_start[i][1]+new_end[i][1])
        temp = 0
        for i in range(len(sum)):
            if sum[i][1] < sum[i+1][1]:
                temp = i
        return sum[i]