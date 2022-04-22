# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    nutXuatPhat = problem.getStartState()
    if problem.isGoalState(nutXuatPhat):
        return []
    dfsStack = util.Stack()
    nutDaXet = [] #tao 1 list rong cac nut da di qua
    dfsStack.push((nutXuatPhat, [])) #dat diem xuat phat vao ngan xep
    while not dfsStack.isEmpty(): #tiep tuc tim kiem cho den khi tat ca cac nut duoc xet
        (nutHienTai, duongDi) = dfsStack.pop() #xoa phan tu o dau tien cua ngan xep
        if nutHienTai not in nutDaXet:
            nutDaXet.append(nutHienTai) #them vao vi tri cuoi cung cua List
            if problem.isGoalState(nutHienTai):
                return duongDi
            for successor in problem.getSuccessors(nutHienTai): #xet tat ca cac nut con
                dfsStack.push((successor[0], duongDi + [successor[1]]))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    nutXuatPhat = problem.getStartState() 
    if problem.isGoalState(nutXuatPhat): #kiem tra nut xuat phat co phai muc tieu ko
        return []
    bfsQueue = util.Queue()
    nutDaXet = []
    bfsQueue.push((nutXuatPhat, []))
    while not bfsQueue.isEmpty():
        (nutHienTai, duongDi) = bfsQueue.pop()
        if problem.isGoalState(nutHienTai):
            return duongDi #tra ve duong di neu dat duoc muc tieu
        if nutHienTai not in nutDaXet:
            nutDaXet.append(nutHienTai)
            #them nut con vao danh sach ria va noi cac hanh dong truoc do de duy tri duong di
            for successor in problem.getSuccessors(nutHienTai):
                bfsQueue.push((successor[0], duongDi + [successor[1]]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    nutXuatPhat = problem.getStartState()
    if problem.isGoalState(nutXuatPhat):
        return []
    nutDaXet = [] #tao 1 list cac nut da di qua
    ucsQueue = util.PriorityQueue()
    ucsQueue.push((nutXuatPhat, [], 0), 0)

    while not ucsQueue.isEmpty():
        nutHienTai, duongDi, chiPhiCu =  ucsQueue.pop()
        if nutHienTai not in nutDaXet: #chi xet nhung nut chua dc di qua
            nutDaXet.append(nutHienTai) #them nut hien tai vao danh sach nhung nut da di qua
            if problem.isGoalState(nutHienTai):
                return duongDi
            for nutTiepTheo, hanhDong, chiPhi in problem.getSuccessors(nutHienTai):
                #them cac nut con vao danh sach ria, noi cac hanh dong truoc do de duy tri duong di
                #tinh toan chi phi de den duoc nut dich tu nut ban dau {f(n) = g(n)}
                hangDongTiep = duongDi + [hanhDong]
                priority = chiPhiCu + chiPhi
                ucsQueue.push((nutTiepTheo, hangDongTiep, priority), priority)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    nutXuatPhat = problem.getStartState()
    if problem.isGoalState(nutXuatPhat):
        return []

    nutDaXet = []

    aStarQueue = util.PriorityQueue()
    aStarQueue.push((nutXuatPhat, [], 0), 0)

    while not aStarQueue.isEmpty(): #tiep tuc tim kiem cho den khi tat ca cac nut duoc quet
        nutHienTai, hanhDong, chiPhiCu = aStarQueue.pop()
        if nutHienTai not in nutDaXet: #xet nut hien tai neu no chua duoc di qua
            nutDaXet.append(nutHienTai)
            if problem.isGoalState(nutHienTai):
                return hanhDong #tra ve duong di neu tim duoc dich
            for nutTiepTheo, hDong, chiPhi in problem.getSuccessors(nutHienTai): #voi moi nut con
                # them cac nut con vao danh sach ria, noi cac hanh dong truoc do de duy tri duong di
                # tinh tong chi phi de den nut n tu dau va heuristiccost de den duoc muc tieu tu nut ban dau
                hangDongTiep = hanhDong + [hDong]
                chiPhiMoi = chiPhiCu + chiPhi
                heuristicCost = chiPhiMoi + heuristic(nutTiepTheo, problem)
                aStarQueue.push((nutTiepTheo, hangDongTiep, chiPhiMoi), heuristicCost)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
