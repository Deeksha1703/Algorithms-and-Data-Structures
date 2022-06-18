def allocate(preferences, sysadmins_per_night, max_unwanted_shifts, min_shifts):
    """
    Function to define the schedules of the system administrators that will be on duty in the night shifts for the next 30 nights
    Precondition: 
        - Each sysadmin can only be allocated to a maximum of max_unwanted_shifts night shifts
        - Each sysadmin needs to be allocated to at elast min_shifts night shifts
    Postcondition: 
        - A valid night shift allocation is returned if one exists, else None
    Input:
        - preferences: Night shift preferences of each sysadmin
        - sysadmins_per_night: The exact number of sysadmins that should be on duty each night
        - max_unwanted_shifts: Each of the n sysadmins should be allocated to at most max_unwanted_shifts night shifts for which s/he was not inter- ested
        - min_shifts: Each of the n sysadmins should be allo- cated to at least min_shifts night shifts
    Return:
        - allocation: A list of lists allocation. allocation[i][j] should be equal to 1 if the sysadmin numbered j is allocated to work on the the night 
                      numbered i, and allocation[i][j] should be equal to 0 if the sysadmin numbered j is not allocated to work on the the night numbered i
    Time Complexity:
        Best: O(NlogN)
        Worst: O(N^2)
    Space Complexity:
        Best: O(N)
        Worst: O(N)
    """
    nights = 30
    allocation = None
    allocation_count = nights * sysadmins_per_night
    total_admins = len(preferences[0])
    result = 2+total_admins*2+nights+1

    if (allocation_count-(min_shifts*total_admins)) < 0:
        return allocation

    graph = [None]*(result)
    add_node(graph, 1, 0, 0)
    add_node(graph, 0, 1, allocation_count-(min_shifts*total_admins))
    
    for j in range(total_admins):
        add_node(graph, 0, j+2, min_shifts)
        add_node(graph, j+2, 1, 0)
        add_node(graph, j+2, 0, 0)
        add_node(graph, 1, j+2, nights)
        add_node(graph, total_admins + j + 2, j+2, 0)
        add_node(graph, j+2, total_admins+ j + 2, max_unwanted_shifts)
        
    for i in range(nights):
        for k in range(len(preferences[i])):
            if preferences[i][k] != 1:
                add_node(graph, 2+total_admins+k, 2+total_admins*2+i, 1)
                add_node(graph, 2+total_admins*2+i, 2+total_admins+k, 0)
            elif preferences[i][k] == 1:
                add_node(graph, k+2, 2+total_admins*2+i, 1)
                add_node(graph, 2+total_admins*2+i, k+2, 0)
                
        add_node(graph, 2+total_admins*2+i, result-1, sysadmins_per_night)
        add_node(graph, result-1, 2+total_admins*2+i, 0)

    allocation = FordFulkerson(graph, 0, nights, result-1, sysadmins_per_night, total_admins)
    return allocation

def BreadthFirstSearch(graph, source_node, end_node, parent):
    """
    Function to implement breadth first search algorithm which searches through a graph until it can find the target node.
    Input:
        - graph: The graph to be traversed
        - source_node: The starting node of the graph
        - end_node: The ending node of the graph
        - parent: List that holds each node's parent
    Return:
        - Returns true if the particular node is found, else False
    Time Complexity:
        Best: O(V+E)
        Worst: O(V+E)
    Space Complexity:
        Best: O(|V|)
        Worst: O(|V|)
    """
    visted = [False]*len(graph)
    queue = [source_node]
    visted[source_node] = True

    while queue:
        cur_index = queue.pop(0)
        
        for i in graph[cur_index]:
            adjacent_vertex_index = i[0]
            if visted[adjacent_vertex_index] == False and i[1] > 0:
                queue.append(adjacent_vertex_index)
                parent[adjacent_vertex_index] = cur_index
                visted[adjacent_vertex_index] = True
                if adjacent_vertex_index == end_node:
                    return True
    return False

def FordFulkerson(graph, source, nights, sink, sysadmins_per_night, admins):
    """
    Function to implement Ford Fulkerson agorithm which detects maximum flow from start vertex to sink vertex in a given graph
    Input:
        - graph: The graph to be traversed
        - source: The starting node of the graph
        - sink: The ending node if the graph
        - nights: number of nights that allocation needs to be done for
        - sysadmins_per_night: The exact number of sysadmins that should be on duty each night
        - admins: Total number of sysadmins that we have
    Return:
        - allocation: A list of lists allocation. allocation[i][j] should be equal to 1 if the sysadmin numbered j is allocated to work on the the night 
                      numbered i, and allocation[i][j] should be equal to 0 if the sysadmin numbered j is not allocated to work on the the night numbered i
    Time Complexity:
        Best: O(EF)
        Worst: O(EF)
    E -> Number fo edges in the graph
    F -> Maximum flow in the graph
    Space Complexity:
        Best: O(V)
        Worst: O(V)
    V -> Number of vertices
    """
    maximum_flow = 0
    allocation = [[0]*admins]
    allocation.extend([0]*admins for _ in range(nights-1))
    parent = [-1]*len(graph)
    while BreadthFirstSearch(graph, source, sink, parent):
        flow = float("Inf")
        s = sink
        while (s != source):
            ind = None
            for i in range(len(graph[parent[s]])):
                if graph[parent[s]][i][0] == s:
                    ind = i 
            flow = min(flow, graph[parent[s]][ind][1])
            s = parent[s]
            
        maximum_flow += flow

        vertex = sink
        while (vertex != source):
            u = parent[vertex]

            vertex_index = None
            for i in range(len(graph[u])):
                if graph[u][i][0] == vertex:
                    vertex_index = i 
            graph[u][vertex_index][1] -= flow
            
            u_index = None
            for i in range(len(graph[vertex])):
                if graph[vertex][i][0] == u:
                    u_index = i 
            graph[vertex][u_index][1] += flow
            
            vertex = parent[vertex]

    if (maximum_flow != sysadmins_per_night * nights):
        allocation = None 
    else:
        for i in range(admins):
            for j in graph[i+2+admins]:
                if (j[0] != i+2) and j[1] == 0:
                    final_index = j[0] - (admins*2 + 2)
                    allocation[final_index][i] = 1
            for k in graph[i+2]:
                if (k[0] != admins+i+2) and k[1] == 0:
                    final_index = k[0] - (admins*2 + 2)
                    allocation[final_index][i] = 1
    return allocation

def add_node(graph, index, node, weight):
    """
    Function to add a node to a graph
    Input:
        - u: Index of graph where node needs to be appended
        - v: Node to be appended
        - weight: weight of node
    Time Complexity:
        Best: O(1)
        Worst: O(1)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    """
    if graph[index] is None:
        graph[index] = [[node, weight]]
    else:
        graph[index].append([node, weight])

class TrieNode:
  """
    Class for TrieNode which will be used to construct the Trie
  """
  def __init__(self, letter):
    """
   Constructor to initialise the TrieNode class
    Input:
        - letter: Starting character of the string
    Time Complexity:
        Best: O(1)
        Worst: O(1)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    """
    self.letter = letter
    self.children = {}
    self.level = 0
    self.count = 0
    self.is_end_of_word = False

class EventsTrie:
  def __init__(self,timelines):
    """
    Constructor to initialise the EventsTrie class
    Input:
        timelines: Timelines in whcih we need to search for longest event
    Time Complexity:
        Best: O(NM^2)
        Worst: O(NM^2)
    Space Complexity:
        Best: O(NM)
        Worst: O(NM)
    """
    self.root = TrieNode("*")
    self.timelines = timelines

  def traversal(self,nd,noccurence):
    """
    Function to traverse every branch to the bottom and check if it is of max depth and check if noccurence is matching the input
    Precondition: noccurenence needs to be greater than 0
    Postcondition: The last letter in the node is returned
    Input:
        - nd: Current node
        - noccurence: positive integer in the range 1 to N
    Return:
        - lCurr: The currect letter that is being traversed
    Time Complexity:
        Best: O(N)
        Worst: 0(N)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    """
    curr_node = nd
    if curr_node.letter == "*":
      lPrev=''
    if curr_node.children:
          lPrev =''
          for child in curr_node.children: 
              lCurr = ''
              childnode = curr_node.children[child]
              if childnode.count >= noccurence:
                lCurr= childnode.letter+self.traversal(childnode,noccurence)

              if len(lCurr) > len(lPrev):
                  lPrev = lCurr
          if curr_node.letter == "*":
            return lPrev
    else: 
          lCurr=''
    return lCurr


  def add_word(self,word):
    """
    Function to concatenate word to the root in a recursive manner
    Precondition: word string needs to have at least 1 character
    Postcondition: word is concatenated to the root
    Input:
        - word: Word to be concatenated
    Time Complexity:
        Best: O(N)
        Worst: O(N)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    """
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        curr_node.children[letter] = TrieNode(letter)
      prev_node = curr_node
      curr_node = curr_node.children[letter]
      curr_node.level = prev_node.level + 1
      curr_node.count+=1
    curr_node.is_end_of_word = True
  
  def does_word_exist(self, word):
    """
    Function to check if a given word exists
    Input:
        - word: Word that we need to check for
    Return:
        - True if word exists, else false 
    Time Complexity:
        Best: O(N)
        Worst: O(N)
    Space Complexity:
        Best: O(1)
        Worst: O(1)
    """
    if word == "":
      return True
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        return False
      curr_node = curr_node.children[letter]
    return curr_node.is_end_of_word 

  def getLongestChain(self, noccurence):
    """
    Function to find the longest chain of events in noccurence timelines
    Precondition: 
        - noccurence should not be 0
    Postcondition: 
        - The longest chain of events in nocccurence timelines is returned
    Input:
        - noccurence: positive integer in the range 1 to N
    Return:
        - maxString: Longect chain of events that occurs in nooccurence timelines
    Time Complexity:
        Best: O(K)
        Worst: O(K)
    K -> length of the longest event chain that occur at least in noccurence number of timelines.
    Space Complexity:
        Best: O(N)
        Worst: O(N)
    """
    for timeline in self.timelines:
        length=len(timeline)
        for i in range(length):
            self.add_word(timeline[i:])
    if noccurence == 1:
      maxString = max(self.timelines, key=len)
    elif noccurence < 1:
      maxString is None
    else:
        maxString = self.traversal(self.root,noccurence)
    return maxString