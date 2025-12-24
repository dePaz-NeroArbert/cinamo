import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="For My Yeobo ❤️",
    page_icon="☁️",
    layout="centered"
)

# 2. State Management (This remembers the clicks)
if 'feed_count' not in st.session_state:
    st.session_state.feed_count = 0
if 'game_won' not in st.session_state:
    st.session_state.game_won = False

# 3. Custom CSS for Cinnamoroll Theme
st.markdown("""
    <style>
    /* Import cute font */
    @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

    /* Background & Text */
    .stApp {
        background-color: #dcedf6;
        background-image: radial-gradient(#ffffff 15%, transparent 16%), radial-gradient(#ffffff 15%, transparent 16%);
        background-size: 60px 60px;
        background-position: 0 0, 30px 30px;
    }
    
    html, body, [class*="css"] {
        font-family: 'Varela Round', sans-serif;
        color: #0089c1;
    }

    /* Button Styling */
    div.stButton > button {
        background-color: #ffb7b2;
        color: white;
        border-radius: 20px;
        border: 2px solid white;
        padding: 10px 24px;
        font-size: 18px;
        transition: all 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: #ff9e99;
        transform: scale(1.05);
        border-color: #fff;
    }

    /* Progress Bar Color */
    .stProgress > div > div > div > div {
        background-color: #0089c1;
    }
    
    /* Letter Box */
    .letter-box {
        background-color: #fff0f5;
        border: 3px dashed #ffb7b2;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. App Logic
st.title("☁️ Merry Christmas! 🎄")

# Define the target number of treats
TARGET_TREATS = 5

# Display the main interaction area if game is not won yet
if not st.session_state.game_won:
    st.write("### Cinnamoroll looks hungry...")
    
    # Calculate progress
    progress = st.session_state.feed_count / TARGET_TREATS
    st.progress(progress)
    
    # Logic to swap images
    if st.session_state.feed_count > 0 and st.session_state.feed_count < TARGET_TREATS:
        # Show happy image briefly if they just clicked (simulated logic)
        st.image("images/happy.gif", width=300)
    else:
        st.image("images/idle.gif", width=300)

    # The Button
    if st.button("Give Cinnamon Roll 🥯"):
        st.session_state.feed_count += 1
        
        # Check for Win
        if st.session_state.feed_count >= TARGET_TREATS:
            st.session_state.game_won = True
            st.rerun() # Refresh the page to show the letter
            
    st.caption(f"Treats given: {st.session_state.feed_count} / {TARGET_TREATS}")

# 5. The Reveal (Win State)
else:
    st.balloons() # Cute balloon effect
    st.snow()     # Christmas snow effect
    
    st.image("images/happy.gif", width=300)
    
    st.markdown("""
    <div class="letter-box">
        <h2>To My Yeobo, ❤️</h2>
        <p>
            You fed Cinnamoroll enough treats! <br>
            Just like he loves cinnamon rolls, I love you so much.
        </p>
        <p>
            You make my world fluffy and bright. <br>
            <strong>Merry Christmas!</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Play Again?"):
        st.session_state.feed_count = 0
        st.session_state.game_won = False
        st.rerun()