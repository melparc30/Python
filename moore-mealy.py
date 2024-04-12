# Moore Machine
class MooreMachine:
  def __init__(self, states, input_symbols, output_symbols, transition_function, output_function, initial_state):
    self.states = states
    self.input_symbols = input_symbols
    self.output_symbols = output_symbols
    self.transition_function = transition_function
    self.output_function = output_function
    self.initial_state = initial_state
    self.current_state = self.initial_state

  def next_output(self, input_symbol):
    self.current_state = self.transition_function(self.current_state, input_symbol)
    return self.output_function(self.current_state)

  def reset(self):
    self.current_state = self.initial_state

# Mealy Machine
class MealyMachine:
  def __init__(self, states, input_symbols, output_symbols, transition_function, output_function, initial_state):
    self.states = states
    self.input_symbols = input_symbols
    self.output_symbols = output_symbols
    self.transition_function = transition_function
    self.output_function = output_function
    self.initial_state = initial_state
    self.current_state = self.initial_state

  def next_output(self, input_symbol):
    self.current_state = self.transition_function(self.current_state, input_symbol)
    return self.output_function(self.current_state, input_symbol)

  def reset(self):
    self.current_state = self.initial_state



# Moore and Mealy state machine example in Python

# Define the number of states
num_states = int(input("Enter the number of states: "))

# Define the state transition table
# This table shows the transitions between states
# The first index represents the current state, and the second index represents the input
# The value in the table represents the next state
state_transition_table = [[0 for i in range(2)] for j in range(num_states)]

# Define the output table
# This table shows the output for each state and input combination
# The first index represents the current state, and the second index represents the input
# The value in the table represents the output
output_table = [[0 for i in range(2)] for j in range(num_states)]

# Fill in the state transition table and output table
# The values in the tables can be determined by the design of the state machine
for i in range(num_states):
    for j in range(2):
        state_transition_table[i][j] = int(input(f"Enter the next state for state {i} and input {j}: "))
        output_table[i][j] = int(input(f"Enter the output for state {i} and input {j}: "))

# Print the state transition diagram
print("State transition diagram:")
for i in range(num_states):
    print(f"State {i}:")
    for j in range(2):
        print(f"  Input {j}: next state = {state_transition_table[i][j]}, output = {output_table[i][j]}")


