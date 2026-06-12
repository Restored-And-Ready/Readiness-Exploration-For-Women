import streamlit as st
import requests
import json

# Set premium, deeply intentional page configuration
st.set_page_config(page_title="The Unlabeled Exploration", page_icon="🌳", layout="centered")

# Museum-Grade Custom Editorial Styling (Anchored in Inherent Goodness)
st.markdown("""
<style>
    .stApp { background-color: #FDFBF7; color: #2C2523; font-family: 'Arial', sans-serif; }
    h1, h2, h3 { color: #5C1D24 !important; font-family: 'Georgia', serif; font-weight: normal; }
    .stButton>button { 
        background-color: #5C1D24 !important; color: white !important; 
        border-radius: 4px; padding: 0.7rem 1.8rem; border: none; font-family: 'Georgia', serif; font-size: 1.1rem;
    }
    .stButton>button:hover { background-color: #7D2B33 !important; }
    .stTextArea textarea { background-color: #F7F4EF !important; border: 1px solid #E2DDD5 !important; color: #2C2523 !important; font-size: 1.05rem; }
    .stTextInput input { background-color: #F7F4EF !important; border: 1px solid #E2DDD5 !important; color: #2C2523 !important; }
    div[data-testid="stMarkdownContainer"] blockquote {
        border-left: 3px solid #5C1D24 !important; background-color: #F7F4EF; padding: 12px 24px; color: #4A3E3B; font-style: italic; font-size: 1.1rem;
    }
    label { font-size: 1.1rem !important; font-weight: bold !important; color: #4A3E3B !important; }
</style>
""", unsafe_allow_html=True)

# Initialize Core Paced Step Controller
if 'room_step' not in st.session_state:
    st.session_state.room_step = 1

# Initialize Complete Diagnostic Memory
if 'client_responses' not in st.session_state:
    st.session_state.client_responses = {}

# ==========================================
# 🌳 THE THRESHOLD: IDENTITY GATEWAY
# ==========================================
if st.session_state.room_step == 1:
    st.title("The Unlabeled Exploration 🌳")
    st.markdown("### *A Safe, Compassionate Space to Connect with the Woman Inside.*")
    
    st.markdown(
        "> \"Every coping mechanism, control loop, and moments of silent numbing are not signs that you are broken. "
        "They are the creative, protective parts of your system trying to shield you from a deep, aching void. "
        "At the root of it all, we are simply remembering that you are inherently good inside, and it is safe to put down the armor.\""
    )
    
    st.write(
        "Welcome. This is not a clinical interrogation or a rigid commercial test. This is a slow, sacred walk "
        "through the rooms of your internal castle. Give yourself permission to be completely unmasked here. "
        "We are exploring how you are natively wired versus how you were programmed to survive."
    )
    
    st.markdown("---")
    st.subheader("Secure Your Private Container")
    name = st.text_input("First & Last Name", value=st.session_state.client_responses.get('name', ''))
    email = st.text_input("Private Email Address", value=st.session_state.client_responses.get('email', ''))
    age = st.text_input("Age / Current Season of Life", value=st.session_state.client_responses.get('age', ''))
    
    st.markdown("---")
    st.subheader("Select Your Environmental Reality")
    st.write("To ensure the text mirrors your true daily experience, select the path that aligns with your current labor landscape:")
    
    path_selection = st.radio(
        "Choose your current path:",
        [
            "💼 Path A: The Corporate Leader / HR Executive / Clinical Manager (My workspace and home are physically separate; I run external teams or systems).",
            "🏡 Path B: The Stay-at-Home Mom / Matriarch (My workspace is my kitchen counter; my daily labor and home environment are fully connected).",
            "💻 Path C: The Solo WFH Entrepreneur / Visionary (I am building a brand or business from within my home, facing collapsed boundaries and deep professional isolation)."
        ],
        index=0
    )
    
    st.markdown("---")
    commit = st.checkbox("I commit to giving my system 30 to 60 minutes of uninterrupted time to honor this space and explore my truth.")
    
    if st.button("Step Across The Threshold"):
        if name and email:
            if commit:
                st.session_state.client_responses['name'] = name
                st.session_state.client_responses['email'] = email
                st.session_state.client_responses['age'] = age
                st.session_state.client_responses['chosen_path'] = path_selection
                st.session_state.room_step = 2
                st.rerun()
            else:
                st.warning("Please check the commitment box to claim this sacred time for yourself.")
        else:
            st.warning("Please provide your name and email to securely build your alignment mirror profile.")

# ==========================================
# 💼 ROOM ONE: THE REALM OF DAILY LABOR
# ==========================================
elif st.session_state.room_step == 2:
    st.title("Room One: Your Primary Realm of Daily Labor 💼")
    st.audio("track1.mp3")
    
    chosen_path = st.session_state.client_responses.get('chosen_path', '')
    labor_prompt_text = ""
    
    # --- PATH A: THE CORPORATE LEADER ---
    if "Path A" in chosen_path:
        st.write(
            "When our home life or internal world enters a season of heavy instability, we often flee into our "
            "professional execution. We build meticulous organizational structures and systems at work because it "
            "is the one place we feel we can manufacture safety and control. But when your team fails to follow "
            "protocols, it triggers a deep, exhausting cycle of resentment."
        )
        st.markdown("---")
        st.subheader("How do you currently navigate the human ecosystem of your workspace?")
        
        labor_choice = st.radio(
            "Select the reality that matches your day-to-day experience:",
            [
                "I operate with clear boundaries and delegate tasks with ease. I can step away from my desk at the end of the day without carrying the emotional weight or fixing the personal problems of my team.",
                "I have built precise systems to ensure things are done right, but when people skip protocols, I feel deeply compromised. I find myself stepping in to fix their unfinished work while carrying a heavy layer of unspoken resentment.",
                "When workplace pressure or chaos mounts, I find myself pulling a cold wall down around my desk. I stop trusting others to execute accurately, pull all the responsibility onto myself, and treat my workspace like a solo island."
            ]
        )
        
        if "clear boundaries" in labor_choice:
            labor_prompt_text = "What does it feel like to lead and operate from this space of clean alignment? What specific professional boundaries are you currently using to successfully protect your peace?"
        elif "precise systems" in labor_choice:
            labor_prompt_text = "Where do you feel the heavy friction of parenting your team? Why does your survival software whisper that you must step in and fix their unfinished mess to protect the client or patient?"
        else:
            labor_prompt_text = "What specific vulnerability or chaos are you protecting yourself from by pulling all execution onto your solo island? What are you afraid will happen if you lower your guard?"

    # --- PATH B: THE STAY-AT-HOME MOM ---
    elif "Path B" in chosen_path:
        st.write(
            "Because your workspace is your home space, the lines between daily labor and private rest don't just "
            "blur—they completely vanish. You wear every single hat in the empire: doctor, driver, housekeeper, and "
            "logistics manager. Yet, because you aren't bringing in an outside paycheck, a quiet, destructive story "
            "whispers that your labor isn't 'providing' real value."
        )
        st.markdown("---")
        st.subheader("How does your system currently hold the daily load of running the home?")
        
        labor_choice = st.radio(
            "Select the reality that matches your day-to-day experience:",
            [
                "I honor my role at home as a sacred space. I can set clear domestic boundaries without guilt, disconnect my worth from an external paycheck, and confidently prioritize my own recovery, health, and rest alongside my family's needs.",
                "I find myself running this household like a strict operational drill, managing every tiny detail. I stay on constant high alert because a voice inside tells me that if I drop a single logistical ball, the entire family structure will fall apart.",
                "I frequently collapse my boundaries, saying yes when my body is screaming no, and swallow my true complaints to keep the peace. I turn to secret comforts—like endless scrolling, online shopping, or a quiet drink—just to survive the isolation."
            ]
        )
        
        if "sacred space" in labor_choice:
            labor_prompt_text = "How do you successfully separate your internal worth from a corporate paycheck? What does prioritizing your own intellectual expansion look like in your daily routine?"
        elif "strict operational drill" in labor_choice:
            labor_prompt_text = "What terrifies your system about dropping a single domestic ball? Where did you first learn the rule that you are only safe if you are perfectly managing every moving piece around you?"
        else:
            labor_prompt_text = "What specific unexpressed pain or grief are you swallowing to keep the peace? What empty space inside are the daytime drinks, scrolling, or Amazon packages trying to fill?"

    # --- PATH C: THE SOLO WFH ENTREPRENEUR ---
    else:
        st.write(
            "You are birthing a kingdom from your bedroom or kitchen table, pouring your life-force into a laptop out of "
            "absolute survival necessity. But because your labor is invisible to your household, they treat your vision "
            "like a hobby, leaving you feeling profoundly lonely and unvalidated."
        )
        st.markdown("---")
        st.subheader("How is your system currently holding the pressure of your business creation?")
        
        labor_choice = st.radio(
            "Select the reality that matches your day-to-day experience:",
            [
                "I create and operate my business with a sense of spaciousness and trust. I can cleanly close my laptop when the day is done, completely separate my personal worth from my stats, and let my work be an unforced expression of my purpose.",
                "I am pouring survival panic into my brand. I find myself grinding until 2 AM, over-engineering my strategy entirely in my head, and staying in frantic motion because I feel like an completely unsupported, isolated island.",
                "The sheer pressure of trying to build this business entirely alone has overwhelmed my system. I sit at my computer and find myself completely frozen, heavy, and numb—using trivial distractions or scrolling to escape the weight."
            ]
        )
        
        if "spaciousness and trust" in labor_choice:
            labor_prompt_text = "How does operating from deep trust alter your creative clarity? How do you cleanly disconnect your personal value from your daily revenue or social stats?"
        elif "survival panic" in labor_choice:
            labor_prompt_text = "What are you running from by grinding until 2 AM? What does your system believe will happen if you slow down and allow your business to rest for a weekend?"
        else:
            labor_prompt_text = "Where exactly does the pressure of building this alone freeze your creative energy? What does your system need to feel safe enough to thaw out and take one small step?"
        
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    labor_text = st.text_area(labor_prompt_text, height=150, key=f"labor_journal_{hash(labor_choice)}")
    
    if st.button("Walk Into the Next Space →"):
        st.session_state.client_responses['room1_mirror'] = labor_choice
        st.session_state.client_responses['room1_journal'] = labor_text
        st.session_state.room_step = 3
        st.rerun()

# ==========================================
# 🏡 ROOM TWO: THE STATUS GATE
# ==========================================
elif st.session_state.room_step == 3:
    st.title("Room Two: Your Home, Relational Dynamics & Intimacy 🏡")
    st.write(
        "Now, we turn our gaze behind closed doors—into your closest relationships, your family dynamics, and the "
        "core of your intimacy and sexual vitality. Women deeply tangle their identity as a *mother* with their identity "
        "as a *sensual, relational woman*, often burying their private desires under their children's schedules. "
        "To untangle this matrix, let us look at your exact relational landscape:"
    )
    
    st.markdown("---")
    relational_status = st.radio(
        "Select your current relational status:",
        [
            "Path Single: I am single, divorced, or navigating life without a live-in partner.",
            "Path Partnered: I am married, cohabitating, or in a long-term committed relationship."
        ]
    )
    
    if st.button("Enter the Relational Room"):
        st.session_state.client_responses['relational_status'] = relational_status
        st.session_state.room_step = 4
        st.rerun()

# ==========================================
# 🏡 ROOM TWO: CHECKPOINT A (Parenting Only)
# ==========================================
elif st.session_state.room_step == 4:
    st.title("Room Two: Checkpoint A - The Parenting Dynamic 🧒")
    st.audio("track2.mp3")
    status = st.session_state.client_responses.get('relational_status', '')
    parenting_prompt_text = ""
    
    if "Path Single" in status:
        st.write(
            "As a solo anchor, every single ounce of emotional, physical, and financial weight rests squarely on "
            "your shoulders. Let us explore the baseline reality of your household operations:"
        )
        st.markdown("---")
        parenting_choice = st.radio(
            "Which of these descriptions most accurately matches how your home currently functions?",
            [
                "I lead my household with a sense of calm authority and grace. I hold loving, clear boundaries with my children and trust that my presence and love are more than enough.",
                "I run a highly regulated, tight ship because there is no safety net beneath me. I force myself to be everything at once, terrified that if I drop a single ball, our entire baseline structure will collapse.",
                "I carry immense unspoken guilt over the fact that our family structure split or shifted. I frequently find myself collapsing my own structural boundaries and walking on eggshells around my children to avoid friction."
            ]
        )
        
        if "calm authority" in parenting_choice:
            parenting_prompt_text = "Your solo parenting landscape is reflecting a beautiful state of clean alignment. What boundaries or mental shifts have allowed you to cultivate this internal peace?"
        elif "highly regulated" in parenting_choice:
            parenting_prompt_text = "What does it physically cost your spirit to carry the full weight of provider and protector entirely alone? Where can you allow your system to receive support?"
        else:
            parenting_prompt_text = "What specific past failure or family rupture are you trying to overcompensate for by letting your children walk over your structural boundaries?"
            
    else:
        st.write(
            "Sharing a roof does not automatically guarantee shared labor. Let us look at how the daily logistics, "
            "emotional loads, and management of the children are actually balanced between you and your partner:"
        )
        st.markdown("---")
        parenting_choice = st.radio(
            "Which of these descriptions captures your current co-parenting reality?",
            [
                "We manage the logistics and daily routines well as a functional unit. We communicate with mutual respect, share the structural loads evenly, and keep the household organized and stable together.",
                "I am essentially single-parenting with a spouse. My partner is completely checked out or acts like another child I have to manage. I carry the entire emotional and physical workload alone while shielding a deep layer of bitter resentment."
            ]
        )
        
        if "functional unit" in parenting_choice:
            parenting_prompt_text = "Your household teamwork is operating in pure light. How do you and your partner actively maintain this mutual respect and shared operational flow without dropping into resentment?"
        else:
            parenting_prompt_text = "What is the true somatic weight of single-parenting with a spouse? How deep does the silent, bitter resentment run toward your partner, and how is it draining your energy?"

    st.markdown("---")
    st.subheader("Your Parenting Reflection Journal")
    parenting_text = st.text_area(parenting_prompt_text, height=150, key=f"parenting_journal_{hash(parenting_choice)}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 3
            st.rerun()
    with col2:
        if st.button("Continue to Intimacy Mirror →"):
            st.session_state.client_responses['room2_parenting_mirror'] = parenting_choice
            st.session_state.client_responses['room2_parenting_journal'] = parenting_text
            st.session_state.room_step = 5
            st.rerun()

# ==========================================
# 🏡 ROOM TWO: CHECKPOINT B (Intimacy Only)
# ==========================================
elif st.session_state.room_step == 5:
    st.title("Room Two: Checkpoint B - Your Intimate & Sensual Self 🥀")
    status = st.session_state.client_responses.get('relational_status', '')
    intimacy_prompt_text = ""
    
    if "Path Single" in status:
        st.write(
            "Strip away your responsibilities to your children. Let us look strictly at you—the woman, your sensuality, "
            "and your private romantic desires. What is the raw reality inside your heart?"
        )
        st.markdown("---")
        intimacy_choice = st.radio(
            "Which of these statements best mirrors your personal intimate heart right now?",
            [
                "I honor my sexual and romantic desires as a healthy part of my wholeness. I feel open to love, vulnerability, and deep physical connection without shame, guilt, or compromising my independent worth.",
                "I desire companionship and touch, but I am secretly mourning a past relational rupture, divorce, or betrayal. My system feels frozen in fear, and I use my kids' schedules as a protective shield to keep from risking further pain.",
                "I have completely locked my sexual life-force, desires, and sensuality behind a brick wall. I don't explore connection, and I use my busy identity as a mother to numb out and ignore the massive void of a companion."
            ]
        )
        
        if "healthy part" in intimacy_choice:
            intimacy_prompt_text = "Your private intimate heart is open and aligned. What does this deep emotional security allow you to confidently welcome or explore next in your life?"
        elif "secretly mourning" in intimacy_choice:
            intimacy_prompt_text = "What is the name of the relational ghost or past divorce your heart is still actively mourning? What terrifies your system about lowering your guard and risking exposure again?"
        else:
            intimacy_prompt_text = "You've hidden your sensual life-force behind the mask of a busy mother. What would happen if you allowed yourself to admit that you deeply crave romantic and physical companionship?"

    else:
        st.write(
            "Strip away the kids, the schedules, and the household chores. When the bedroom door closes and it is "
            "just you and your partner, what is the honest truth of your connection?"
        )
        st.markdown("---")
        intimacy_choice = st.radio(
            "Which of these statements best captures your current marital intimacy?",
            [
                "Our intimacy is a space of deep safety, pleasure, and emotional surrender. I express my true desires and boundaries without fear, and our connection is where I drop my armor and experience true rest.",
                "Our relationship feels emotionally distant or heavy. I find myself constantly people-pleasing—suppressing my real voice, ignoring my own boundaries, and doing whatever it takes just to keep the peace and avoid friction.",
                "The passion and physical vitality have gone completely cold. We are platonic roommates coexisting in the dark. I spend my evenings escaping into my head, using scrolling, shopping, or quiet distractions to numb the void between us."
            ]
        )
        
        if "deep safety" in intimacy_choice:
            intimacy_prompt_text = "Your intimate bedroom connection is functioning as a radiant sanctuary of alignment. What does this deep safety and pleasure unlock for your partnership and your independent vision?"
        elif "emotionally distant" in intimacy_choice:
            intimacy_prompt_text = "Where exactly are you compromising your own physical or emotional boundaries inside your sexual intimacy just to avoid his judgment, anger, or relational friction?"
        else:
            intimacy_prompt_text = "You are platonic roommates coexisting in the dark. What outside comforts (online shopping, scrolling, daytime drinking) are you using to fill the void of real physical connection?"

    st.markdown("---")
    st.subheader("Your Intimacy Reflection Journal")
    intimacy_text = st.text_area(intimacy_prompt_text, height=150, key=f"intimacy_journal_{hash(intimacy_choice)}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 4
            st.rerun()
    with col2:
        if st.button("Walk into the Body →"):
            st.session_state.client_responses['room2_intimacy_mirror'] = intimacy_choice
            st.session_state.client_responses['room2_intimacy_journal'] = intimacy_text
            st.session_state.room_step = 6
            st.rerun()

# ==========================================
# 🩺 ROOM THREE: PHYSICAL HEALTH & SOMATIC THRESHOLDS
# ==========================================
elif st.session_state.room_step == 6:
    st.title("Room Three: Your Physical Health & Somatic Thresholds 🩺")
    st.write(
        "Your physical body has been the faithful witness to every ounce of pressure, unexpressed grief, and emotional "
        "residue you have carried. It keeps the score perfectly when the mind tries to override. Let us tune in and listen:"
    )
    st.audio("track3.mp3")
    
    st.markdown("---")
    st.subheader("How does your internal operating system currently handle your physical body?")
    
    body_choice = st.radio(
        "Select the statement that best describes your relation to your physical health:",
        [
            "I am deeply attuned to my body's language. I honor its physical boundaries, protect its need for true rest, and respond to its whispers before a physical breakdown forces me to stop.",
            "I treat my body like a machine or a soldier. I run on adrenaline and cortisol, cancel my own appointments to prioritize everyone else, and force my system to march through pain and exhaustion.",
            "When the emotional or mental pressure gets too heavy, my physical system locks up. I struggle with chronic tightness, unexplainable fatigue, or stubborn weight retention that feels like a layer of protective armor.",
            "I live almost entirely inside my analytical head. I disconnect from physical sensations completely, over-intellectualizing my symptoms or treating my health like an abstract science project instead of actually feeling my flesh."
        ]
    )
    
    if "attuned to my body" in body_choice:
        body_prompt_text = "Your system is operating in clear somatic alignment. What dedicated health boundaries or recovery practices are successfully keeping your physical temple so radiant right now?"
    elif "like a machine" in body_choice:
        body_prompt_text = "Where exactly is your body screaming for you to stop? What are you actively trying to outrun by forcing your system to march through pain on pure cortisol and adrenaline?"
    elif "locks up" in body_choice:
        body_prompt_text = "Where in your flesh do you physically feel this defensive armor (stubborn weight retention, shoulder tightness, chronic pain)? What deep emotional vulnerability is it trying to protect?"
    else:
        body_prompt_text = "What specific, heavy emotions are you deeply afraid to actually feel in your chest and gut by choosing to live entirely inside your analytical head?"
        
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    body_text = st.text_area(body_prompt_text, height=150, key=f"body_journal_{hash(body_choice)}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 5
            st.rerun()
    with col2:
        if st.button("Explore Your Identity →"):
            st.session_state.client_responses['room3_mirror'] = body_choice
            st.session_state.client_responses['room3_journal'] = body_text
            st.session_state.room_step = 7
            st.rerun()

# ==========================================
# 👑 ROOM FOUR: IDENTITY, ESSENCE & WORTH
# ==========================================
elif st.session_state.room_step == 7:
    st.title("Room Four: Your Identity & Sovereign Essence 👑")
    st.write(
        "We step now into the quietest room. Strip away the corporate titles, the business metrics, the maternal roles, "
        "and the endless demands of everyone who relies daily on your strength. We are looking directly at you."
    )
    st.audio("track4.mp3")
    
    st.markdown("---")
    st.subheader("When you are completely alone with your thoughts, what does your internal dialogue sound like?")
    
    identity_choice = st.radio(
        "Select the reality that matches your inner world when no one is looking:",
        [
            "I feel deeply anchored in my inherent worth. I protect my energetic boundaries without guilt, speak to myself with radical compassion, and know that I am deeply good inside simply for existing.",
            "My self-worth is entirely chained to my output and performance. If I am not achieving, fixing, building, or producing, I feel completely empty, useless, and terrified of being exposed as an underachiever.",
            "My internal dialogue is incredibly severe and hyper-critical. I speak to my own soul with a level of judgment, auditing, and severity that I would never use on another human being.",
            "I have spent so many years pleasing everyone else and playing the household therapist that I genuinely don't know who I am anymore. If you strip away my roles as a mother, worker, or partner, I feel like a blank space."
        ]
    )
    
    if "anchored in my inherent worth" in identity_choice:
        identity_prompt_text = "You are standing firmly on your throne, resting in your inherent worth. What does it physically feel like to fully accept your own enoughness without needing to perform for anyone?"
    elif "chained to my output" in identity_choice:
        identity_prompt_text = "If you completely stopped producing, fixing, or working for one full week, who would you be? Why does absolute stillness feel like such an existential threat to your system?"
    elif "hyper-critical" in identity_choice:
        identity_prompt_text = "Whose hyper-severe voice is that inner critic actually using when it judges you? What does the little girl inside you desperately need to hear from you instead?"
    else:
        identity_prompt_text = "Who are you when you strip away your identity as a mother, worker, or partner? What does your true, unmasked identity look like when no one else is in the room?"
        
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    identity_text = st.text_area(identity_prompt_text, height=150, key=f"identity_journal_{hash(identity_choice)}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 6
            st.rerun()
    with col2:
        if st.button("Compile Your Alignment Mirror ✨"):
            st.session_state.client_responses['room4_mirror'] = identity_choice
            st.session_state.client_responses['room4_journal'] = identity_text
            st.session_state.room_step = 8
            st.rerun()

# ==========================================
# 🕊️ THE ALIGNMENT MIRROR: TRUE REPORT OUTPUT
# ==========================================
elif st.session_state.room_step == 8:
    st.title("Your Alignment Mirror 🕊️")
    st.write("Take a deep breath. Exhale the armor. Your complete multi-dimensional somatic blueprint has been compiled.")
    st.audio("track5.mp3")
    
    st.markdown("---")
    st.header("✨ Your Unmasked Somatic Blueprint")
    st.write("Below is the full, high-integrity reflection of your internal castle. This layout belongs exclusively to you.")
    
    st.markdown("### 💼 Room 1: Your Realm of Daily Labor")
    st.markdown(f"**Your Observed Pattern:**\n> {st.session_state.client_responses.get('room1_mirror', 'No Selection')}")
    st.markdown(f"**Your Private Journal Insight:**\n*{st.session_state.client_responses.get('room1_journal', 'No written entry saved.')}*")
    
    st.markdown("---")
    st.markdown("### 🧒 Room 2: Checkpoint A - The Parenting Dynamic")
    st.markdown(f"**Your Observed Pattern:**\n> {st.session_state.client_responses.get('room2_parenting_mirror', 'No Selection')}")
    st.markdown(f"**Your Private Journal Insight:**\n*{st.session_state.client_responses.get('room2_parenting_journal', 'No written entry saved.')}*")
    
    st.markdown("---")
    st.markdown("### 🥀 Room 2: Checkpoint B - Your Intimate & Sensual Self")
    st.markdown(f"**Your Observed Pattern:**\n> {st.session_state.client_responses.get('room2_intimacy_mirror', 'No Selection')}")
    st.markdown(f"**Your Private Journal Insight:**\n*{st.session_state.client_responses.get('room2_intimacy_journal', 'No written entry saved.')}*")
    
    st.markdown("---")
    st.markdown("### 🩺 Room 3: Your Physical Body & Somatic Thresholds")
    st.markdown(f"**Your Observed Pattern:**\n> {st.session_state.client_responses.get('room3_mirror', 'No Selection')}")
    st.markdown(f"**Your Private Journal Insight:**\n*{st.session_state.client_responses.get('room3_journal', 'No written entry saved.')}*")
    
    st.markdown("---")
    st.markdown("### 👑 Room 4: Your Core Identity & Sovereign Essence")
    st.markdown(f"**Your Observed Pattern:**\n> {st.session_state.client_responses.get('room4_mirror', 'No Selection')}")
    st.markdown(f"**Your Private Journal Insight:**\n*{st.session_state.client_responses.get('room4_journal', 'No written entry saved.')}*")
    
    st.markdown("---")
    st.markdown(
        "> 🛡️ **The Unlabeled Remonition:** *This profile is an intuitive, highly responsive mirror based entirely on the "
        "authentic narrative choices and somatic markers you chose to lay bare today. Your body carries immense wisdom. "
        "Every control addiction, parenting overcompensation, or physical numbing loop you highlighted is simply a "
        "protective part of you trying to shield an internal void. You can finally release the control, let go, and let God.*"
    )
    
    st.markdown("---")
    st.subheader("An Invitation to Private, High-Integrity Somatic Restoration")
    st.write(
        "If your system is profoundly tired of driving on adrenaline, and you are ready to transition from a "
        "conceptual understanding of your void into a lived, physical reality of unshakeable enoughness, I invite you "
        "into our dedicated, 30-day private restoration architecture:"
    )
    
    st.markdown("### 🏛️ Phase 1: The Private Somatic Release Session")
    st.write("A live, dedicated 1-to-1 deep dive container where we map your specific nervous system loops and guide your body to physically release the accumulated pressure, concrete tightness, and emotional residue.")
    
    st.markdown("### 🛡️ Phase 2: The 21-Day Protected Integration")
    st.write("Three weeks of protected integration loops equipped with daily somatic resource tracks and custom practices designed specifically for your body's friction points.")
    
    st.markdown("### 🔄 Phase 3: The Weeks 3 & 4 Alignment Check")
    st.write("A dedicated review to ensure your new boundaries and internal somatic clarity stick for the long haul.")
    
    st.markdown("---")
    st.markdown("### 🕊️ Container Logistics & Booking")
    st.write(
        "The foundational investment for this complete three-phase somatic architecture is **$750**.\n\n"
        "To officially claim this container and send your unmasked reflection profile directly onto Candy's desk, click the submit button below."
    )
    
    st.markdown("---")
    
    # NEW INTERACTIVE SUBMIT BUTTON ARCHITECTURE
    if 'submitted' not in st.session_state:
        if st.button("Submit My Somatic Profile to Candy 🕊️"):
            try:
                webhook_url = st.secrets["WEBHOOK_URL"]
                requests.post(webhook_url, json=st.session_state.client_responses)
                st.session_state.submitted = True
                st.rerun()
            except:
                st.error("Connection link timed out. Please check your dashboard settings and try submitting again.")
    else:
        st.success("✨ Your unmasked somatic profile has been securely transmitted straight to Candy's private desk! Check your email for your next steps and calendar invitation.")
        
        if st.button("Restart Exploration Journey 🔄"):
            st.session_state.room_step = 1
            st.session_state.client_responses = {}
            if 'submitted' in st.session_state: del st.session_state.submitted
            st.rerun()
