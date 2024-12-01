import streamlit as st
import time
import sys
from io import StringIO

st.set_page_config(
    page_title="Kid's Coding Academy - Decision Maker",
    page_icon="🎮",
    layout="wide"
)

# Learning Path Overview
st.markdown("""
# 🎮 Welcome to Decision Maker!

## Your Complete Coding Journey (21 Missions Total):
### Chapter 1: Beginner Missions (Missions 1-5)
✅ Mission 1: Making Your Computer Talk
✅ Mission 2: Storing Secret Messages
✅ Mission 3: Getting User Input
✅ Mission 4: Calculator Magic
✅ Mission 5: Number Games

### Chapter 2: Decision Maker (Missions 6-10) - You Are Here! 🎯
🔸 Mission 6: Yes or No Machine
🔸 Mission 7: Adventure Game
🔸 Mission 8: Rock, Paper, Scissors
🔸 Mission 9: Count with Me
🔸 Mission 10: Pattern Maker

### Coming Next:
🔜 Chapter 3: Creative Coder (Missions 11-15)
🔜 Chapter 4: List Explorer (Missions 16-21)

Current Progress: 5/21 Missions Completed
""")

def init_session_state():
    if 'current_mission' not in st.session_state:
        st.session_state.current_mission = 6
    if 'completed_missions' not in st.session_state:
        st.session_state.completed_missions = set()

def capture_output(code_to_execute):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    exec(code_to_execute)
    sys.stdout = old_stdout
    return mystdout.getvalue()

def show_mission_6():
    st.title("🤖 Mission 6: Yes or No Machine")
    
    st.markdown("""
    ### Time to Make Decisions!
    
    Let's teach your computer to make choices using `if` statements:
    """)
    
    st.code("""
answer = input("Do you like pizza? (yes/no): ")

if answer == "yes":
    print("Yummy! Pizza is awesome! 🍕")
if answer == "no":
    print("That's okay, more pizza for me! 😋")
    """)
    
    st.markdown("""
    🎯 Now create your own decision maker:
    1. Ask a fun question
    2. Use `if` to respond differently based on the answer
    3. Add emoji reactions!
    """)
    
    user_code = st.text_area("Write your decision code:", key="mission6_code", height=150)
    if st.button("Test My Decisions! 🤔", key="mission6_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Decision Output:")
            st.code(output_text)
            st.session_state.completed_missions.add(6)
        except Exception as e:
            st.write("Decision Helper:", str(e))

def show_mission_7():
    st.title("🎮 Mission 7: Adventure Game")
    
    st.markdown("""
    ### Create Your Own Adventure!
    
    Let's make a story where the player chooses what happens next:
    """)
    
    st.code("""
print("You find a magical door! 🚪")
choice = input("Do you want to: 1) Open it 2) Knock first? ")

if choice == "1":
    print("The door leads to a room full of treasure! 💎")
if choice == "2":
    print("A friendly dragon answers! 🐲")
    """)
    
    user_code = st.text_area("Create your adventure:", key="mission7_code", height=150)
    if st.button("Start Adventure! 🗺️", key="mission7_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Adventure Output:")
            st.code(output_text)
            st.session_state.completed_missions.add(7)
        except Exception as e:
            st.write("Adventure Guide:", str(e))

def show_mission_8():
    st.title("🎮 Mission 8: Rock, Paper, Scissors")
    
    st.markdown("""
    ### Let's Make a Classic Game!
    
    Time to use `if`, `elif`, and `else` to create Rock, Paper, Scissors:
    """)
    
    st.code("""
player = input("Choose: rock, paper, or scissors: ")
computer = "rock"  # For this example, computer always chooses rock

if player == "paper":
    print("You win! Paper covers rock! 🎉")
elif player == "scissors":
    print("You lose! Rock breaks scissors! 💔")
else:
    print("It's a tie! 🤝")
    """)
    
    user_code = st.text_area("Create your game:", key="mission8_code", height=150)
    if st.button("Play! ✌️", key="mission8_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Game Output:")
            st.code(output_text)
            st.session_state.completed_missions.add(8)
        except Exception as e:
            st.write("Game Guide:", str(e))

def show_mission_9():
    st.title("🔄 Mission 9: Count with Me")
    
    st.markdown("""
    ### Time to Learn Loops!
    
    Let's make the computer count and repeat things:
    """)
    
    st.code("""
for number in range(5):
    print(f"Counting: {number + 1} 🔢")

# Make a cool pattern
for i in range(3):
    print("🌟" * (i + 1))
    """)
    
    user_code = st.text_area("Create your counting program:", key="mission9_code", height=150)
    if st.button("Start Counting! 🔢", key="mission9_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Counting Output:")
            st.code(output_text)
            st.session_state.completed_missions.add(9)
        except Exception as e:
            st.write("Loop Helper:", str(e))

def show_mission_10():
    st.title("🎨 Mission 10: Pattern Maker")
    
    st.markdown("""
    ### Create Amazing Patterns!
    
    Use nested loops to make cool patterns:
    """)
    
    st.code("""
for row in range(3):
    for col in range(3):
        print("🌈", end="")
    print()  # New line after each row
    """)
    
    user_code = st.text_area("Create your pattern:", key="mission10_code", height=150)
    if st.button("Make Pattern! 🎨", key="mission10_button"):
        try:
            output_text = capture_output(user_code)
            st.write("Pattern Output:")
            st.code(output_text)
            st.session_state.completed_missions.add(10)
        except Exception as e:
            st.write("Pattern Helper:", str(e))

# Initialize session state
init_session_state()

# Sidebar navigation
st.sidebar.title("🎮 Decision Maker")
mission_choice = st.sidebar.radio(
    "Choose your mission:",
    ["Mission 6: Yes or No Machine",
     "Mission 7: Adventure Game",
     "Mission 8: Rock, Paper, Scissors",
     "Mission 9: Count with Me",
     "Mission 10: Pattern Maker"]
)

# Progress tracking
progress = len(st.session_state.completed_missions) * 20
st.sidebar.progress(progress)
st.sidebar.write(f"Progress: {progress}% complete")

# Mission selector
if "Mission 6" in mission_choice:
    show_mission_6()
elif "Mission 7" in mission_choice:
    show_mission_7()
elif "Mission 8" in mission_choice:
    show_mission_8()
elif "Mission 9" in mission_choice:
    show_mission_9()
elif "Mission 10" in mission_choice:
    show_mission_10()

# Achievement display
if progress == 100:
    st.sidebar.markdown("### 🏆 DECISION MAKER COMPLETED!")
    st.sidebar.balloons()
