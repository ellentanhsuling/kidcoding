import streamlit as st
import time
import sys
from io import StringIO

st.set_page_config(
    page_title="Kid's Coding Academy - Beginner Missions",
    page_icon="📚",
    layout="wide"
)

def create_code_keyboard():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button('"', key=f'quote_{st.session_state.current_mission}')
        st.button('(', key=f'paren1_{st.session_state.current_mission}')
    with col2:
        st.button(')', key=f'paren2_{st.session_state.current_mission}')
        st.button('=', key=f'equals_{st.session_state.current_mission}')
    with col3:
        st.button('print', key=f'print_{st.session_state.current_mission}')
        st.button('input()', key=f'input_{st.session_state.current_mission}')
    with col4:
        st.button('{', key=f'brace1_{st.session_state.current_mission}')
        st.button('}', key=f'brace2_{st.session_state.current_mission}')
    with col5:
        st.button('*', key=f'multiply_{st.session_state.current_mission}')
        st.button('/', key=f'divide_{st.session_state.current_mission}')

def handle_input(prompt):
    return st.text_input(prompt)

def capture_output(code_to_execute):
    global input
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    input = handle_input
    exec(code_to_execute)
    sys.stdout = old_stdout
    return mystdout.getvalue()

def show_mission_1():
    st.title("🌟 Mission 1: Making Your Computer Talk!")
    
    create_code_keyboard()
    
    st.markdown("""
    ### Hey Future Coder! 
    
    Let's make a box to store words and show them:
    ```python
    message = "Hello!"    # message is a box holding "Hello!"
    print(message)        # Shows what's in the message box
    ```
    
    Think of it like:
    📦 message = Your magical box
    "Hello!" = What you put inside the box
    print = Opening the box to show everyone!
    """)

    user_code = st.text_area("Type your code here:", key="mission1_code", height=100)
    
    if st.button("Run My Code! 🚀", key="mission1_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Your computer says:")
            st.code(output_text)
            st.balloons()
            st.session_state.completed_missions.add(1)
        except Exception as e:
            st.error("Oops! Let's try again! 💪")

def show_mission_2():
    st.title("🗝️ Mission 2: Storing Secret Messages")
    
    create_code_keyboard()
    
    st.markdown("""
    ### Welcome Secret Agent Coder! 
    
    Let's make three magical boxes to store your secret agent info:
    ```python
    code_name = "Agent Python"     # First box: your secret name
    agent_age = 9                  # Second box: your age (no quotes for numbers!)
    power = "invisible"            # Third box: your superpower
    
    print(f"Agent {code_name} is {agent_age} years old")
    print(f"Special power: {power}")
    ```
    
    The boxes are called 'variables':
    📦 code_name = Box for your agent name
    📦 agent_age = Box for your age
    📦 power = Box for your superpower
    """)
    
    user_code = st.text_area("Write your secret agent code:", key="mission2_code", height=150)
    if st.button("Run Secret Code 🕵️", key="mission2_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Secret Files:")
            st.code(output_text)
            st.balloons()
            st.session_state.completed_missions.add(2)
        except Exception as e:
            st.error("Mission needs adjustments! Try again! 💪")

def show_mission_3():
    st.title("🎤 Mission 3: Getting User Input")
    
    create_code_keyboard()
    
    st.markdown("""
    ### Let's Make Your Computer Ask Questions!
    
    Here's how to get answers from users:
    ```python
    # Ask a question and store the answer in a box
    pet_name = input("What's your pet's name? ")
    
    # Use the answer from the box
    print(f"Hello {pet_name}! You're such a good pet!")
    ```
    
    Think of it like:
    1. input() = Asking a question
    2. pet_name = Box to keep the answer
    3. print() = Showing the answer in a fun way
    """)
    
    user_code = st.text_area("Create your question program:", key="mission3_code", height=150)
    if st.button("Run My Program! 🎮", key="mission3_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Your Program Says:")
            st.code(output_text)
            st.session_state.completed_missions.add(3)
        except Exception as e:
            st.error("Let's fix this together! 💪")

def show_mission_4():
    st.title("🧮 Mission 4: Calculator Magic")
    
    create_code_keyboard()
    
    st.markdown("""
    ### Time for Math Magic!
    
    Let's make boxes for numbers and do math with them:
    ```python
    number1 = 10    # First number box
    number2 = 5     # Second number box
    
    # Math boxes
    plus_box = number1 + number2    # Addition
    times_box = number1 * number2   # Multiplication
    
    print(f"{number1} + {number2} = {plus_box}")
    print(f"{number1} × {number2} = {times_box}")
    ```
    
    Math symbols you can use:
    ➕ + for adding
    ➖ - for subtracting
    ✖️ * for multiplying
    ➗ / for dividing
    """)
    
    user_code = st.text_area("Create your calculator:", key="mission4_code", height=150)
    if st.button("Calculate! 🔢", key="mission4_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Your Calculator Says:")
            st.code(output_text)
            st.session_state.completed_missions.add(4)
        except Exception as e:
            st.error("Math needs a little fix! Try again! 💪")

def show_mission_5():
    st.title("🎮 Mission 5: Number Games")
    
    create_code_keyboard()
    
    st.markdown("""
    ### Let's Make a Fun Number Game!
    
    Here's how to make a guessing game:
    ```python
    secret_box = 7                              # Box with secret number
    guess = int(input("Guess (1-10): "))       # Box for player's guess
    points = 10                                 # Box for score
    
    if guess == secret_box:                     # Check if guess matches
        print(f"You win {points} points! 🎉")
    else:
        print("Try again! 🎲")
    ```
    
    Game pieces:
    🎲 secret_box = Your hidden number
    📥 guess = Player's guess
    🏆 points = Score to win
    """)
    
    user_code = st.text_area("Create your game:", key="mission5_code", height=150)
    if st.button("Play Game! 🎲", key="mission5_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Game Says:")
            st.code(output_text)
            st.session_state.completed_missions.add(5)
        except Exception as e:
            st.error("Game needs a tune-up! Try again! 💪")

# Initialize session state
if 'current_mission' not in st.session_state:
    st.session_state.current_mission = 1
if 'completed_missions' not in st.session_state:
    st.session_state.completed_missions = set()

# Sidebar navigation
st.sidebar.title("📚 Beginner Missions")
mission_choice = st.sidebar.radio(
    "Choose your mission:",
    ["Mission 1: Computer Talk",
     "Mission 2: Secret Messages",
     "Mission 3: User Input",
     "Mission 4: Calculator Magic",
     "Mission 5: Number Games"]
)

# Progress tracking
progress = len(st.session_state.completed_missions) * 20
st.sidebar.progress(progress)
st.sidebar.write(f"Progress: {progress}% complete")

# Mission selector
if "Mission 1" in mission_choice:
    show_mission_1()
elif "Mission 2" in mission_choice:
    show_mission_2()
elif "Mission 3" in mission_choice:
    show_mission_3()
elif "Mission 4" in mission_choice:
    show_mission_4()
elif "Mission 5" in mission_choice:
    show_mission_5()

# Achievement display
if progress == 100:
    st.sidebar.markdown("### 🏆 BEGINNER MISSIONS COMPLETED!")
    st.sidebar.balloons()