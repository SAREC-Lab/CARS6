
**Trello Board Link*
https://trello.com/b/RqyrWWEP/assignment-4


**Task Plan Specification**

For our Task Plan specifications we are going to use a JSON file and define the plan using a data dictionary. 
We decided to use a data dictionary for our DSL for the project because of its versatility and usability. 
Applying new attributes to each state is easily accomplished for more complex paths. 
Additionally, formatting the JSON file in this manner makes it easier to parse in the directions correctly and make sure that each attribute is correctly defined.

**Requirements, Design Definitions, and Trace Matrices:**

R1 - The UGV moves the directed amount of feet within one foot.

	D1- The UGV loads in data from any correctly formatted task plan from the JSON file in the order given.
	
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

When working with the physical car we were prepared to have a necessary learning curve. We had a lot of issues getting the code to run on the car, or even getting our car to run. Because of these technical problems we decided to run all of our tests in the simulator. We made more task plans to test the code, and made test cases for each state to make sure they were running in the correct order. 

After adjusting the code many times in order to pass the tests, our car was running smoothly in the simulator. Unfortunately we were unable to run the code with our actual car and therefore were unable to see how the car really ran. We realized there there a plethora of task plan combinations that our code would need to work with and that only using 5-6 plans is a limitation to our code and design. Given the time constraint and numerous issues with the hardware, we recognize the room for improvement within our testing strategies.






