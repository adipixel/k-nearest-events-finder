# Nearest events finder
A program which accepts a user location as a pair of co- ordinates, and returns a list of the five closest events, along with the cheapest ticket price for each event.

### Summary
- The events are randomly generated with locations on the graph that ranges from -10 to 10 in both x-axis and y-axis.
- Each co-ordinate holds zero or one event and each event has zero or more tickets with a price more than zero dollars.
- The distances are calculated using Manhattan distance method.
- The size of the area is large having just few events,or size of area can be small with many events. So the challenge was to save the space and size while implementing the application. On the other hand, search time also had to as less as possible.
- The *kd-tree algorithm* is used in this application. A k-d tree (short for k-dimensional tree) is a space-partitioning data structure for organizing points in a k-dimensional space. Construction of kd-tree takes O(n log2 n) if heapsort is used to sort the tree nodes.
- Finding 1 nearest neighbour in a balanced k-d tree with randomly distributed points takes O(log n) time on average.
- If in case of adding new events, in the worst case, the tree can be re-balanced to get best search results.



### Execution Instructions
1. Clone this directory using `git clone https://github.com/adipixel/nearest-events-finder.git`
2. Go inside the cloned directory
3. Run `python project.py`
The program will generate the input data and display the locations of all events.
Then, it will ask to enter the location of the user in the format of `x, y` (range is -10 to 10)
4. Enter the user location co-ordinates adn hit enter
5. Boom! the five nearest events will appear.

Example Results:
```
Events closest to (1, 1)
Event: 048 - $ 16.39 , Distance 1
Event: 240 - $ 78.37 , Distance 2
Event: 095 - $ 2.88 , Distance 2
Event: 083 - $ 368.61 , Distance 2
Event: 078 - $ 31.54 , Distance 3

```


### Files
1. `project.py` - application program file
2. `data.json` - contains the randomly generated input data of following format

Format:
```json
[
	[{
		"tickets": [60.66, 81.56, 89.8, 121.44, 243.51, 271.95, 274.43, 312.35],
		"position": [0, 0],
		"num": 298
	},
	null,
	{
		"tickets": [121.15, 259.57],
		"position": [0, 2],
		"num": 324
	}]
]
```

### Assumptions
- The number tickets at each event ranges from 0 to 10 for simplicity. (But can be changed to any number in future)
- In the five nearest events found, if any event is having zero tickets, the program lets you know that there is no ticket available for that event
- If there are less than five events in the entire world of range -10 to 10, the program gives all the available results.
(Example: if there are just 3 events, the program returns just 3 of them instead of 5)


### Visualization of input data
For convenience and verification of results the input data can be plotted on a graph
#### Steps to plot input data
1. Goto `https://jsfiddle.net/adipixel/0p5322ou/3/`
2. In the javascript section, on line 8, paste the event location list generated on the console.

Example:
```
[7, 3] , [8, -8] , [-2, 0] , [-7, -3] , [1, -5] , [1, 6] , [3, 7] , [-2, -7] , [8, 5] , [-10, 1] , [9, 0] , [-6, -5] , [-5, -5] , [-9, 10] , [-9, -8] , [-8, -7] , [-3, -2] , [-2, 10] , [0, 4] , [1, 1] , [3, 2] , [2, 6] , [8, 2] , [6, -3] , [-9, -3] , [6, 0] , [9, -9] , [2, -9] , [-7, -5] , [-8, -10] , [0, -3] , [0, 1] , [-3, -7] , [7, -5] , [3, 1] , [-9, -9] , [5, -8] , [9, -3] , [-10, 9] , [6, 2] , [8, -4] , [-3, 4] , [-7, -10] , [0, -9] , [-5, 0] , [10, 5] , [-2, -3] , [8, 9] , [-5, 5] , [-2, -8] , [9, -8] , [-10, 10] ,
```
3. Hit the Run button on the top of the page



