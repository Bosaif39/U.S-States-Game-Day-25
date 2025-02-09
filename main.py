import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Load and display the U.S. map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV file containing U.S. state names and coordinates
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # Convert the "state" column into a list
guessed_states = []

# Game loop: Runs until the player correctly guesses all 50 states
while len(guessed_states) < 50:

    # Ask the user to enter a state name
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    
    # Exit condition: If the user types "Exit", save the missing states to a CSV file
    if answer_state == "Exit":
        missing_states = [missing_state for missing_state in all_states if(missing_state not in guessed_states ) ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
        
    # Check if the guessed state is valid and hasn't been guessed before
    if answer_state in all_states:
        guessed_states.append(answer_state)

        # Create a new turtle to write the state name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Get the x, y coordinates of the guessed state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
