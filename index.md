## Team Squushy

To right! Take it back now ya'll... 
Time to make a turtlebot dance!!

### Project Vision Statement

The goal of our project is to use voice recognition to make our turtlebot do the Cha Cha Slide. We will create a library of phrases from the song for our turtlebot to react and dance along to, following the steps choreographed by DJ Casper. To do this we will use a python library which allows for the voice recognition software. We wanted to improve a simple state machine to be able to take in audio, convert it to text using Speech to Text, and then determine which state to use based on the words said. This will give the illusion that the turtlebot is dancing along with the song as it plays. 

## Glossary

**Speech to Text (STT)**

## Design Process
To ensure the team worked efficiently and timely, we decided to use the SCRUM design process for this project. Using a Trello Board (LINK TO BOARD) we were able to organize the project into short 'sprints' for each team member. Due to the fact that this class only met once a week, it was east to assign each member their individual work for the week and what the goals for each sprint were. The benefits to using SCRUM managment for this project included, helping the team complete project deliverables quickly and efficiently, ensuring effective use of time, large projects are divided into easily manageable sprints, developments are coded and tested during the sprint review, and that SCRUM works well for fast-moving development projects. 

## Requirements
### Use Case 
**Name**: Turtle cha cha

**ID**: UC1

**Description**: Turtle bot completes user specified cha cha dance move

**Primary Actor(s)**: User

**Stakeholders & Interests: User - entertained by turtlebot **

- Pre-Conditions: Turtlebot system is active; Turtlebot has assigned routine for cha cha command; Turtlebot can hear and process commands

- Post-Conditions: Success: Turtlebot Successfully completes designated cha cha move on command; Failure: Turtlebot completes the wrong move

Trigger: Turtlebot receives a command to do the cha cha

**Main Success Scenario**:

1. The Turtle bot is active and ready to receive command.
2. User says voice command to cha cha
3. Turtlebot performs cha cha
4. Turtlebot completes cha cha and awaits next command

**Alternative Steps**:
1. Turtlebot receives another voice command and adds it to queue

**Exceptions**:
1. In step 2, instead of voice command, user manually types command

## How-to Make your Turtlebot Dance
1. Open [STT Interface] (https://squushy.herokuapp.com/)
2. Play Cha-Cha Slide by Dj Casper 
3. Click the Start/Stop button
4. In the terminal on your computer run 'roscore'
5. Open a new window and cd to 'catkin_ws/src' 
6. Run the line 'roslaunch turtlebot3_bringup turtlbot3_robot.launch'
7. The turtlbot will read 10 words every ~20ms 
8. Watch as the turtlebot dance
9. Please note that the connect between the terminal and turtlebot will close after 30 seconds of silence, and steps 4-6 will have to be repeated.

## Specific hazards or quality concerns that you addressed.




## Simple Architecture Design
![Architecture](CARS6/blob/gh-pages/highlevel.jpeg)
## System Level Design
![Data Flow](gh-pages/dataflow.jpeg)
## Testing and Implementation
To begin to implement our 
## Results and Demonstration

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)





