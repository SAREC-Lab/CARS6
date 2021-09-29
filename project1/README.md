
**Trello Board Link*
https://trello.com/b/RqyrWWEP/assignment-4


**Task Plan Specification**

For our Task Plan specifications we plan to use a JSON file and define the plan using a data dictionary. 
We decided to use a data dictionary for our DSL for the project because of its versatility and usability. 
Applying new attributes to each state is easily accomplished for more complex paths. 
Additionally, formatting the JSON file in this manner makes it easier to parse in the directions correctly and make sure that each attribute is correctly defined.

**Requirements, Design Definitions, and Trace Matrices:**

R1 - The UGV moves the directed amount of feet within one foot.

	D1- The UGV loads in data from any correctly formatted task plan from the JSON file in the order 
given.
	D2- The UGV successfully returns to plan state after performing each task plan element.
	
	D3- The UGV shall complete a full 8 part task plan and then stop. 


Trace Matrix 1:

R1, D1

R1, D2

R1, D3


Trace Matrix 2: 

D1, plan_parser.py 

D2,  Statemachine.py, forward.py, backward.py, turnL.py, turnR.py, circleL.py, circleR.py, plan.py, threepoint.py

D3, stop.py

**Testing Strategy** 

In order to test our code and verify that it is meeting the design requirements and definitions. After complining the code and making sure each state was properly connected to one another we began running the task plans in the simulator. This allowed us to visualize what we hope our physical car will be able to accomplish. There was some difficultly in keeping the code consistent between group members, but these issues were resolved quickly.

After using the simulator outside of class, we needed to make sure these results would be achieved using the actual car. To continue to test the robustness of our code, we created an additional four task plans that used a variety of combinations of states. These would be our test cases in both the simulator and in person. 

When working with the physical car we were prepared to have a necessary learning curve. 






