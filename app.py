import streamlit as st
import requests
import json

# Set premium page configuration
st.set_page_config(page_title="The Readiness Analysis", page_icon="🌳", layout="centered")

# Custom Museum-Grade Editorial Styling
st.markdown("""
<style>
    .stApp { background-color: #FDFBF7; color: #2C2523; font-family: 'Arial', sans-serif; }
    h1, h2, h3 { color: #5C1D24 !important; font-family: 'Georgia', serif; font-weight: normal; }
    .stButton>button { 
        background-color: #5C1D24 !important; color: white !important; 
        border-radius: 4px; padding: 0.6rem 1.5rem; border: none; font-family: 'Georgia', serif;
    }
    .stButton>button:hover { background-color: #7D2B33 !important; }
    .stTextArea textarea { background-color: #F7F4EF !important; border: 1px solid #E2DDD5 !important; color: #2C2523 !important; }
    .stTextInput input { background-color: #F7F4EF !important; border: 1px solid #E2DDD5 !important; color: #2C2523 !important; }
    div[data-testid="stMarkdownContainer"] blockquote {
        border-left: 3px solid #5C1D24 !important; background-color: #F7F4EF; padding: 10px 20px; color: #4A3E3B; font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Paced Step Controller
if 'room_step' not in st.session_state:
    st.session_state.room_step = 1

# Initialize Session Memory for client answers
if 'client_responses' not in st.session_state:
    st.session_state.client_responses = {}

# 🫙 ROOM 1: THE THRESHOLD (The Safe Arrival)
if st.session_state.room_step == 1:
    st.title("The Readiness Analysis 🌳")
    st.markdown("### *Museum-Grade Restoration for a Woman of Inherent Worth.*")
    
    st.markdown(
        "> \"The problem is not that you are falling apart. The problem is that the old system can no "
        "longer carry who you are becoming. Your body, home, career, and identity are simply "
        "calling for a profound update.\""
    )
    
    st.write(
        "Take a breath. Put down the heavy bags you’ve been carrying before you entered this space. "
        "This is not a test to pass, a clinical interrogation, or a commercial marketing quiz. This is a quiet, "
        "responsive space to map your internal operating system. You are entirely safe here."
    )
    
    st.markdown("---")
    st.subheader("Secure Your Private Container Below")
    
    name = st.text_input("First & Last Name", value=st.session_state.client_responses.get('name', ''))
    email = st.text_input("Private Email Address", value=st.session_state.client_responses.get('email', ''))
    age = st.text_input("Age / Current Season of Life", value=st.session_state.client_responses.get('age', ''))
    
    st.markdown("### 🚧 Grounding Your Presence")
    st.write("Completing this analysis step-by-step is your very first victory—proving to your nervous system that you are finally prioritizing you.")
    
    commit = st.checkbox("I commit to myself to hold space for this entire narrative journey right now. I am done waiting for tomorrow.")
    
    if st.button("Step Across The Threshold"):
        if name and email:
            if commit:
                st.session_state.client_responses['name'] = name
                st.session_state.client_responses['email'] = email
                st.session_state.client_responses['age'] = age
                st.session_state.room_step = 2
                st.rerun()
            else:
                st.warning("Please check the box to commit this sacred time to yourself before entering.")
        else:
            st.warning("Please provide your name and email so we can securely deliver your reflection summary profile.")

# 💼 ROOM 2: THE PROFESSIONAL ARCHITECTURE (Work & Mission)
elif st.session_state.room_step == 2:
    st.title("Room One: Your Work & Professional Space 💼")
    st.write(
        "Let us look first at the landscape where you spend your creative labor and energy—the business you are building "
        "or the professional lane you manage. For high-performing women, this is often the place where we master the art "
        "of masking our exhaustion. Look closely at this space right now..."
    )
    
    st.audio("track1.mp3")
    
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    
    work_ans = st.text_area(
        "What would serve you at work or within your business to feel truly at ease? When do you feel the most connected to your vision, and what would it take to return there?",
        value=st.session_state.client_responses.get('room1_work', ''), height=200
    )
    
    if st.button("Move to the Next Space →"):
        st.session_state.client_responses['room1_work'] = work_ans
        st.session_state.room_step = 3
        st.rerun()

# 🏡 ROOM 3: THE SANCTUARY & SHELTER (Home & Relations)
elif st.session_state.room_step == 3:
    st.title("Room Two: Your Home & Relational Dynamics 🏡")
    st.write(
        "Now, turn your gaze toward the spaces behind closed doors—your home, your closest relationships, and the dynamics "
        "of your daily shelter. A sanctuary is meant to restore you, yet so often, it becomes the place where we simply manage more hidden labor..."
    )
    
    st.audio("track2.mp3")
    
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    
    home_ans = st.text_area(
        "In your home, your relationships, and your daily environment right now, what will help you in your family dynamic to feel completely safe, supported, and at rest?",
        value=st.session_state.client_responses.get('room2_home', ''), height=200
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 2
            st.rerun()
    with col2:
        if st.button("Move to the Next Space →"):
            st.session_state.client_responses['room2_home'] = home_ans
            st.session_state.room_step = 4
            st.rerun()

# 👑 ROOM 4: THE ESSENCE (Identity & Self)
elif st.session_state.room_step == 4:
    st.title("Room Three: Your Identity & Essence 👑")
    st.write(
        "Let us step deeper into the quietest room. Strip away the titles, the business goals, the family demands, and the "
        "expectations of everyone who relies daily on your strength. We are looking directly at you—your sovereign essence..."
    )
    
    st.audio("track3.mp3")
    
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    
    identity_ans = st.text_area(
        "Where do you personally feel safe, seen, and supported in your own skin right now? What do you need to feel more deeply connected to who you inherently are?",
        value=st.session_state.client_responses.get('room3_identity', ''), height=200
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 3
            st.rerun()
    with col2:
        if st.button("Listen to the Body →"):
            st.session_state.client_responses['room3_identity'] = identity_ans
            st.session_state.room_step = 5
            st.rerun()

# 🩺 ROOM 5: THE SYSTEMIC WITNESS (The Body)
elif st.session_state.room_step == 5:
    st.title("Room Four: Your Physical Health & Somatic Thresholds 🩺")
    st.write(
        "Your physical body has been the faithful witness to every ounce of pressure, concrete tightness, and emotional "
        "residue you have carried. It keeps the score perfectly when the mind tries to override and push through..."
    )
    
    st.audio("track4.mp3")
    
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    
    body_ans = st.text_area(
        "Close your eyes, notice where your breath catches right now, and ask your system: What does your physical body need right now to find true peace and deep rest?",
        value=st.session_state.client_responses.get('room4_body', ''), height=200
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 4
            st.rerun()
    with col2:
        if st.button("Compile & Submit Profile ✨"):
            st.session_state.client_responses['room4_body'] = body_ans
            st.session_state.room_step = 6
            st.rerun()

# 🕊️ ROOM 6: THE OVERVIEW, EXPLORATION BREAKDOWN & RESULTS
elif st.session_state.room_step == 6:
    st.title("Your Alignment Mirror 🕊️")
    st.write("Thank you for your honesty. Your full narrative profile has been securely compiled.")
    
    st.audio("track5.mp3")
    
    st.markdown("---")
    st.subheader("Your Hidden Operating System: The Exploration Summary")
    
    st.info(
        f"**Somatic Explorer Profile: {st.session_state.client_responses.get('name')}**\n\n"
        "Your full written reflections across your Work, Home, Identity, and Body have been successfully recorded. "
        "Your responses are safe within our secure container."
    )
    
    st.markdown(
        "> 🛡️ **A Gentle Reminder:** *This reflection is not a clinical, psychological, or medical diagnosis. "
        "It is an intuitive, highly responsive mirror based entirely on the authentic narrative markers you chose to "
        "share here. Your body carries immense wisdom, and these results simply highlight where your internal operating "
        "system is currently asking for deeper care, space, and intentional release.*"
    )
    
    st.markdown("---")
    st.subheader("An Invitation to Deeper, Private Somatic Restoration")
    st.write(
        "If your system is tired of driving on fumes and you are ready to move from a conceptual understanding "
        "into a lived, physical reality of restoration, I invite you into a dedicated, high-integrity container:"
    )
    
    st.markdown("### 🏛️ Phase 1: The Private Somatic Release Session")
    st.write("A live, dedicated 1-to-1 deep dive container where we map your specific nervous system loops and guide your system to release the accumulated physical and emotional residue.")
    
    st.markdown("### 🛡️ Phase 2: The 21-Day Protected Integration")
    st.write("Three weeks of protected integration loops equipped with bespoke daily somatic resource tracks and custom practices designed specifically for your body's friction points.")
    
    st.markdown("### 🔄 Phase 3: The Weeks 3 & 4 Alignment Check")
    st.write("A dedicated review to ensure your new boundaries and internal somatic clarity stick for the long haul.")
    
    st.markdown("---")
    st.markdown("### 🕊️ Booking & Container Logistics")
    st.write(
        "The foundational investment for this complete three-phase somatic architecture is **$750**.\n\n"
        "By initiating this private container, you will be given a secure, private calendar invitation to select "
        "your session time and complete your investment. To honor the deep, intentional preparation required to hold this space "
        "exclusively for you, your session and 30-day container are officially secured and confirmed once the investment is complete."
    )
    
    # Background data push
    if 'fired' not in st.session_state:
        try:
            webhook_url = st.secrets["WEBHOOK_URL"]
            requests.post(webhook_url, json=st.session_state.client_responses)
            st.session_state.fired = True
        except:
            pass
            
    if st.button("Start New Analysis 🔄"):
        st.session_state.room_step = 1
        st.session_state.client_responses = {}
        if 'fired' in st.session_state: del st.session_state.fired
        st.rerun()
