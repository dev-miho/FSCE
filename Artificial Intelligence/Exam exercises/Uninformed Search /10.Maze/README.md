In a maze with N rows and M columns, a person starts at coordinates (x_start, y_start) and needs to reach (x_target, y_target), avoiding K obstacles whose coordinates are given in the input.

The person can move in 4 directions "Gore", "Dolu", "Levo", "Desno" or stay in place ("Stoj"). There is a timer from 1 to 4 (read from input timer), which increases by 1 after each action (after 4 it resets to 1).

There is a laser at position (x_laser, y_laser) (read from input).

When the timer is in state 1, the position of the laser is updated to match the position of the person.

When the timer is in state 4, it fires a beam in a + shape from its current position, so the person must not be in the same row or column as the laser.

You should use uninformed search to find the shortest sequence of actions for the person to reach the target.

All test cases will start from a valid state: if the timer is 1, then the person and the laser will be at the same position, and if the timer is 4 then the person and the laser will not be in the same row or column.

dirs={"Gore":(0,+1),"Dolu":(0,-1),"Levo":(-1,0),"Desno":(+1,0)}

The input will be

N M
x_start y_start
x_target y_target
timer
x_laser y_laser
K
x1 y1
x2 y2
...
xK yK

### Test Case 1
- Input: `5 5
0 0
4 4
1
0 0
4
1 1
2 2
1 2
2 1`
- Output: `No Solution!`

### Test Case 2
- Input: `3 3
1 1
0 1
4
2 2
0`
- Output: `['Levo']`

### Test Case 3
- Input: `3 7
0 1
6 2
1
0 1
12
0 2
0 0
1 2
2 2
2 0
3 0
3 2
4 0
4 2
5 0
5 2
6 0`
- Output: `['Desno', 'Dolu', 'Stoj', 'Stoj', 'Gore', 'Desno', 'Desno', 'Desno', 'Desno', 'Desno', 'Gore']`