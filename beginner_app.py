import streamlit as st
import time
import sys
from io import StringIO

st.set_page_config(
    page_title="Kid's Coding Academy - Beginner Missions",
    page_icon="📚",
    layout="wide"
)

# Learning Path Overview
st.markdown("""
# 📚 Welcome to Beginner Missions!

## Your Complete Coding Journey (21 Missions Total):
### Chapter 1: Beginner Missions (Missions 1-5) - You Are Here! 🎯
🔸 Mission 1: Making Your Computer Talk
🔸 Mission 2: Storing Secret Messages
🔸 Mission 3: Getting User Input
🔸 Mission 4: Calculator Magic
🔸 Mission 5: Number Games

### Coming Next:
🔜 Chapter 2: Decision Maker (Missions 6-10)
🔜 Chapter 3: Creative Coder (Missions 11-15)
🔜 Chapter 4: List Explorer (Missions 16-21)

Current Progress: 0/21 Missions Completed
""")

def init_session_state():
    if 'current_mission' not in st.session_state:
        st.session_state.current_mission = 1
    if 'completed_missions' not in st.session_state:
        st.session_state.completed_missions = set()

def capture_output(code_to_execute):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    exec(code_to_execute)
    sys.stdout = old_stdout
    return mystdout.getvalue()

def show_mission_1():
    st.title("🌟 Mission 1: Making Your Computer Talk!")
    
    st.markdown("""
    ### Hey Future Coder! 
    
    Did you know you can make your computer say anything? Let's try it!
    
    This is your first piece of magical code:
    """)
    
    st.code('print("Hello World!")', language='python')
    
    st.markdown("""
    🎯 What's happening here:
    1. `print` is like a megaphone for your computer
    2. The message goes between the `"quotes"`
    
    Try these:
    - Make it say your name
    - Make it tell a joke
    - Make it roar like a dinosaur
    """)
    
    user_code = st.text_area("Type your code here:", key="mission1_code", height=100)
    
    if st.button("Run My Code! 🚀", key="mission1_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Output:")
            st.code(output_text)
            
            st.balloons()
            st.success("You did it! You're now a computer whisperer! 🌟")
            st.session_state.completed_missions.add(1)
        except Exception as e:
            st.error("Oops! Let's try again! 💪")
            st.write(f"Hint: {str(e)}")

def show_mission_2():
    st.title("🗝️ Mission 2: Storing Secret Messages")
    
    st.markdown("""
    ### Welcome Secret Agent Coder! 
    
    Today we'll learn how to store secret information in something called 'variables'.
    Think of variables like magical boxes that can hold anything!
    """)
    
    st.code("""
secret_name = "Agent Python"
age = 9
favorite_food = "pizza"

print(f"Code name: {secret_name}")
print(f"Agent age: {age}")
print(f"Mission fuel: {favorite_food}")
    """)
    
    st.markdown("""
    🎯 Try creating your own secret agent profile:
    1. Create a variable for your code name
    2. Store your age in a variable
    3. Add your favorite food
    """)
    
    user_code = st.text_area("Write your secret agent code:", key="mission2_code", height=150)
    if st.button("Run Secret Code 🕵️", key="mission2_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Secret Output:")
            st.code(output_text)
            
            st.balloons()
            st.session_state.completed_missions.add(2)
        except Exception as e:
            st.write("Mission Control suggests:", str(e))

def show_mission_3():
    st.title("🎤 Mission 3: Getting User Input")
    
    st.markdown("""
    ### Time to Make Interactive Programs!
    
    Let's make your computer ask questions and remember the answers:
    """)
    
    st.code("""
name = input("What's your name? ")
color = input("What's your favorite color? ")
print(f"Hi {name}! {color} is a fantastic color!")
    """)
    
    st.markdown("""
    🎯 Your turn! Create a program that:
    1. Asks for someone's favorite animal
    2. Asks for their favorite superpower
    3. Creates a superhero story with their answers
    """)
    
    user_code = st.text_area("Create your interactive program:", key="mission3_code", height=150)
    if st.button("Test My Program 🎮", key="mission3_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Program Output:")
            st.code(output_text)
            
            st.session_state.completed_missions.add(3)
        except Exception as e:
            st.write("Debugging hint:", str(e))

def show_mission_4():
    st.title("🧮 Mission 4: Calculator Magic")
    
    st.markdown("""
    ### Time for Some Math Magic!
    
    Let's build a super calculator:
    """)
    
    st.code("""
number1 = 10
number2 = 5

sum_result = number1 + number2
multiply_result = number1 * number2

print(f"{number1} + {number2} = {sum_result}")
print(f"{number1} × {number2} = {multiply_result}")
    """)
    
    st.markdown("""
    🔢 Math Symbols:
    - `+` for adding
    - `-` for subtracting
    - `*` for multiplying
    - `/` for dividing
    """)
    
    user_code = st.text_area("Create your calculator:", key="mission4_code", height=150)
    if st.button("Calculate! 🔢", key="mission4_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Calculator Output:")
            st.code(output_text)
            
            st.session_state.completed_missions.add(4)
        except Exception as e:
            st.write("Math hint:", str(e))

def show_mission_5():
    st.title("🎮 Mission 5: Number Games")
    
    st.markdown("""
    ### Let's Make a Cool Number Game!
    
    We'll combine everything we learned to make a guess-the-number game:
    """)
    
    st.code("""
secret_number = 7
guess = int(input("Guess my number (1-10): "))
points = 10

if guess == secret_number:
    print(f"You win {points} points! 🎉")
else:
    print("Try again! 🎲")
    """)
    
    st.markdown("""
    🎯 Now create your own game:
    1. Pick a secret number
    2. Ask the player for a guess
    3. Tell them if they won
    """)
    
    user_code = st.text_area("Create your game:", key="mission5_code", height=150)
    if st.button("Play Game! 🎲", key="mission5_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Game Output:")
            st.code(output_text)
            
            st.session_state.completed_missions.add(5)
        except Exception as e:
            st.write("Game hint:", str(e))

# Initialize session state
init_session_state()

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
