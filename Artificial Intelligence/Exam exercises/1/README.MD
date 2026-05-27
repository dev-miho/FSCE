A 5x5 board is given, on which two boxes and a person are placed.
The person needs to push the boxes so as to bring them to the bottom-right corner of the board marked in red. 
The person can move in four directions: up, down, left, and right by one position.
While moving, if there is a box in front of them, they can push the box in the direction in which they are moving.
A box cannot be pulled, only pushed. Only one box may occupy a single position.

For all test cases, the size of the board is the same, while the positions of the person and the boxes vary and are read from standard input.
Your task is to implement the movement of the person (and thus the pushing of the boxes) in the successor function, such that the action for moving the person up is tried first, then down, left, and right. 
  The actions are named “Move man up/down/left/right” if the man is moved, or “Push box 1/2 up/down/left/right” if, while moving the person, one of the boxes is also pushed. 
    Additionally, you need to check whether the goal has been reached, that is, to implement the goal_test function, and to check whether the state is valid, that is, to implement the check_valid function. 
    The problem state is stored in a tuple where the elements are the x and y positions of the person and the boxes. For example, the initial state in Figure 1 would be ((0, 0), (2, 2), (3, 3)). 
    You should apply uninformed search to find a solution with the minimum number of steps.


![diagram](FSCE/Artificial Intelligence/Exam exercises/Images/pomestuvanje_kutii.png)
