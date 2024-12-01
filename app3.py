import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
from io import StringIO

st.set_page_config(
    page_title="Kid's Coding Academy - Creative Coder",
    page_icon="🎨",
    layout="wide"
)

# Learning Path Overview
st.markdown("""
# 🎨 Welcome to Creative Coder!

## Your Complete Coding Journey (21 Missions Total):
### Chapter 1: Beginner Missions (Missions 1-5)
✅ Mission 1: Making Your Computer Talk
✅ Mission 2: Storing Secret Messages
✅ Mission 3: Getting User Input
✅ Mission 4: Calculator Magic
✅ Mission 5: Number Games

### Chapter 2: Decision Maker (Missions 6-10)
✅ Mission 6: Yes or No Machine
✅ Mission 7: Adventure Game
✅ Mission 8: Rock, Paper, Scissors
✅ Mission 9: Count with Me
✅ Mission 10: Pattern Maker

### Chapter 3: Creative Coder (Missions 11-15) - You Are Here! 🎯
🔸 Mission 11: Drawing Lines
🔸 Mission 12: Shape Creator
🔸 Mission 13: Rainbow Patterns
🔸 Mission 14: Function Creator
🔸 Mission 15: Art Gallery

### Coming Next:
🔜 Chapter 4: List Explorer (Missions 16-21)

Current Progress: 10/21 Missions Completed
""")

def init_session_state():
    if 'current_mission' not in st.session_state:
        st.session_state.current_mission = 11
    if 'completed_missions' not in st.session_state:
        st.session_state.completed_missions = set()

def capture_output(code_to_execute):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    exec(code_to_execute)
    sys.stdout = old_stdout
    return mystdout.getvalue()

def show_mission_11():
    st.title("🎨 Mission 11: Drawing Lines")
    
    st.markdown("""
    ### Let's Draw with Code!
    
    We can draw lines by giving coordinates to our computer:
    """)
    
    st.code("""
import matplotlib.pyplot as plt

plt.plot([0, 1], [0, 1])  # Draw line from (0,0) to (1,1)
plt.axis([0, 2, 0, 2])    # Set visible area
st.pyplot(plt)
    """)
    
    user_code = st.text_area("Write your drawing code:", key="mission11_code", height=150)
    if st.button("Draw! 🎨", key="mission11_button"):
        try:
            plt.figure()
            output_text = capture_output(user_code)
            if output_text:
                st.write("Print Output:")
                st.code(output_text)
            st.pyplot(plt)
            st.session_state.completed_missions.add(11)
            plt.close()
        except Exception as e:
            st.write("Drawing Helper:", str(e))

def show_mission_12():
    st.title("⭐ Mission 12: Shape Creator")
    
    st.markdown("""
    ### Draw Amazing Shapes!
    
    Let's create shapes using points and lines:
    """)
    
    st.code("""
import matplotlib.pyplot as plt
import numpy as np

angles = np.linspace(0, 2*np.pi, 5)  # 5 points for a star
x = np.cos(angles)
y = np.sin(angles)
plt.plot(x, y, 'r-')  # 'r-' means red line
st.pyplot(plt)
    """)
    
    user_code = st.text_area("Create your shapes:", key="mission12_code", height=150)
    if st.button("Make Shapes! ⭐", key="mission12_button"):
        try:
            plt.figure()
            output_text = capture_output(user_code)
            if output_text:
                st.write("Print Output:")
                st.code(output_text)
            st.pyplot(plt)
            st.session_state.completed_missions.add(12)
            plt.close()
        except Exception as e:
            st.write("Shape Helper:", str(e))

def show_mission_13():
    st.title("🌈 Mission 13: Rainbow Patterns")
    
    st.markdown("""
    ### Add Colors to Your Art!
    
    Let's make colorful patterns:
    """)
    
    st.code("""
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i, color in enumerate(colors):
    plt.plot([0, 1], [i, i], color=color, linewidth=3)
st.pyplot(plt)
    """)
    
    user_code = st.text_area("Create rainbow art:", key="mission13_code", height=150)
    if st.button("Make Rainbow! 🌈", key="mission13_button"):
        try:
            plt.figure()
            output_text = capture_output(user_code)
            if output_text:
                st.write("Print Output:")
                st.code(output_text)
            st.pyplot(plt)
            st.session_state.completed_missions.add(13)
            plt.close()
        except Exception as e:
            st.write("Color Helper:", str(e))

def show_mission_14():
    st.title("🔧 Mission 14: Function Creator")
    
    st.markdown("""
    ### Create Your Own Drawing Commands!
    
    Let's make functions that draw shapes:
    """)
    
    st.code("""
def draw_square(size):
    x = [0, size, size, 0, 0]
    y = [0, 0, size, size, 0]
    plt.plot(x, y)

draw_square(1)  # Draw a square of size 1
st.pyplot(plt)
    """)
    
    user_code = st.text_area("Create your functions:", key="mission14_code", height=150)
    if st.button("Run Functions! 🔧", key="mission14_button"):
        try:
            plt.figure()
            output_text = capture_output(user_code)
            if output_text:
                st.write("Print Output:")
                st.code(output_text)
            st.pyplot(plt)
            st.session_state.completed_missions.add(14)
            plt.close()
        except Exception as e:
            st.write("Function Helper:", str(e))

def show_mission_15():
    st.title("🎨 Mission 15: Art Gallery")
    
    st.markdown("""
    ### Create Your Masterpiece!
    
    Use everything you've learned to make amazing art:
    """)
    
    st.code("""
def draw_flower(x, y, size):
    angles = np.linspace(0, 2*np.pi, 20)
    for angle in angles:
        plt.plot([x, x + size*np.cos(angle)],
                [y, y + size*np.sin(angle)],
                'r-')

draw_flower(0, 0, 1)
plt.axis('equal')
st.pyplot(plt)
    """)
    
    user_code = st.text_area("Create your masterpiece:", key="mission15_code", height=150)
    if st.button("Make Art! 🎨", key="mission15_button"):
        try:
            plt.figure()
            output_text = capture_output(user_code)
            if output_text:
                st.write("Print Output:")
                st.code(output_text)
            st.pyplot(plt)
            st.session_state.completed_missions.add(15)
            plt.close()
        except Exception as e:
            st.write("Art Helper:", str(e))

# Initialize session state
init_session_state()

# Sidebar navigation
st.sidebar.title("🎨 Creative Coder")
mission_choice = st.sidebar.radio(
    "Choose your mission:",
    ["Mission 11: Drawing Lines",
     "Mission 12: Shape Creator",
     "Mission 13: Rainbow Patterns",
     "Mission 14: Function Creator",
     "Mission 15: Art Gallery"]
)

# Progress tracking
progress = len(st.session_state.completed_missions) * 20
st.sidebar.progress(progress)
st.sidebar.write(f"Progress: {progress}% complete")

# Mission selector
if "Mission 11" in mission_choice:
    show_mission_11()
elif "Mission 12" in mission_choice:
    show_mission_12()
elif "Mission 13" in mission_choice:
    show_mission_13()
elif "Mission 14" in mission_choice:
    show_mission_14()
elif "Mission 15" in mission_choice:
    show_mission_15()

# Achievement display
if progress == 100:
    st.sidebar.markdown("### 🏆 CREATIVE CODER COMPLETED!")
    st.sidebar.markdown("### 🌟 You're a Creative Coding Master! 🌟")
    st.sidebar.balloons()
