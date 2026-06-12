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
        
        if "I operate with clear boundaries" in labor_choice:
            labor_prompt_text = "What does it feel like to lead and operate from this space of clean alignment? What specific professional boundaries are you currently using to successfully protect your peace?"
        elif "I have built precise systems" in labor_choice:
            labor_prompt_text = "Where do you feel the heavy friction of parenting your team? Why does your software whisper that you must step in and fix their unfinished mess to protect the client or patient?"
        else:
            labor_prompt_text = "What specific vulnerability or chaos are you balancing by pulling all execution onto your solo island? What are you choosing to look at when you lower your guard?"

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
        
        if "I honor my role at home" in labor_choice:
            labor_prompt_text = "How do you successfully separate your internal worth from a corporate paycheck? What does prioritizing your own intellectual expansion look like in your daily routine?"
        elif "strict operational drill" in labor_choice:
            labor_prompt_text = "What does your system prioritize when managing every moving piece around you? What becomes possible when these details run smoothly?"
        else:
            labor_prompt_text = "What specific adjustments or space are you longing for to ease the isolation? What would true, unmasked support feel like in your household right now?"

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
                "I am pouring survival panic into my brand. I find myself grinding until 2 AM, over-engineer my strategy entirely in my head, and staying in frantic motion because I feel like an completely unsupported, isolated island.",
                "The sheer pressure of trying to build this business entirely alone has overwhelmed my system. I sit at my computer and find myself completely frozen, heavy, and numb—using trivial distractions or scrolling to escape the weight."
            ]
        )
        
        if "spaciousness and trust" in labor_choice:
            labor_prompt_text = "How does operating from deep trust alter your creative clarity? How do you cleanly disconnect your personal value from your daily revenue or social stats?"
        elif "survival panic" in labor_choice:
            labor_prompt_text = "What adjustments to your timeline or structure would allow your business expansion to feel more spacious and unforced?"
        else:
            labor_prompt_text = "Where exactly does your creative energy flow best when the pressure drops? What does your system need to feel completely supported as you take your next small step?"
        
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
            parenting_prompt_text = "What structural adaptations would allow you to share the daily load more effectively? Where can you open up space to receive supportive alignment?"
        else:
            parenting_prompt_text = "What does a balanced, calm home environment look like to you? How can your current household framework adjust to support that vision?"
            
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
            parenting_prompt_text = "What specific operational changes would bridge the gap between you and your partner? How can your household software rebalance so you feel completely supported?"

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
            intimacy_prompt_text = "What does an updated, emotionally clear relationship with your romantic past look like? What would your heart need to feel entirely safe to open up again?"
        else:
            intimacy_prompt_text = "What would it look like to softly invite the 'Lover' archetype back into your life? What spaces of your day are ready to expand into personal romance and companionship?"

    else:
        st.write(
            "Strip away the kids, the schedules, and the household chores. When the bedroom door closes and it is "
            "just you and your partner, what is the honest truth of your connection?"
        )
        st.markdown("---")
        intimacy_choice = st.radio(
            "Which of these statements best captures your current marital intimacy?",
            [
                "Our intimacy is a space of deep safety, pleasure, and emotional surrender. I express my true desires and boundaries without fear, and our relationship is where I drop my armor and experience true rest.",
                "Our relationship feels emotionally distant or heavy. I find myself constantly people-pleasing—suppressing my real voice, ignoring my own boundaries, and doing whatever it takes just to keep the peace and avoid conflict.",
                "The passion and physical vitality have gone completely cold. We are platonic roommates coexisting in the dark. I spend my evenings escaping into my head, using scrolling, shopping, or quiet distractions to numb the void between us."
            ]
        )
        
        if "deep safety" in intimacy_choice:
            intimacy_prompt_text = "Your intimate bedroom connection is functioning as a radiant sanctuary of alignment. What does this deep safety and pleasure unlock for your partnership and your independent vision?"
        elif "emotionally distant" in intimacy_choice:
            intimacy_prompt_text = "What does a deeply fulfilling, vocal, and secure intimacy look like for you? What communication shifts would bring your partnership back into alignment?"
        else:
            intimacy_prompt_text = "What does a vibrant, high-matching relational baseline feel like to your body? How can your connection update to mirror the passion that belongs in your marriage?"

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
            "I live almost entirely inside my analytical head. I disconnect from physical sensations completely, over-intellectualizing my health issues or treating my symptoms like an abstract science project instead of actually feeling my flesh."
        ]
    )
    
    if "I am deeply attuned to my body" in body_choice:
        body_prompt_text = "Your system is operating in clear somatic alignment. What dedicated health boundaries or recovery practices are successfully keeping your physical temple so radiant right now?"
    elif "like a machine" in body_choice:
        body_prompt_text = "What standard of vibrant, effortless health and relaxation is your tissue ready to reclaim? What does true somatic recovery look like for your physical system?"
    elif "locks up" in body_choice:
        body_prompt_text = "What does a completely open, fluid, and light physical body feel like to you? What does your tissue need to safely drop the protective armor and return to balance?"
    else:
        body_prompt_text = "What physical baseline of raw feeling and vitality is your body ready to activate? How can your awareness shift from the neck down to fully inhabit your flesh?"
        
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
        identity_prompt_text = "What does an unshakeable, internal sense of enoughness look like when you are in absolute stillness? Who is the sovereign woman that exists beneath the production?"
    elif "hyper-critical" in identity_choice:
        identity_prompt_text = "What words of radical compassion, validation, and ultimate safety is your inner child ready to receive from you right now? What is your true internal truth?"
    else:
        identity_prompt_text = "Who are you when you step into the room completely for yourself? What do your true, unmasked desires, creative longings, and personal essence look like?"
        
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
# 🕊️ THE ALIGNMENT MIRROR: ENHANCED NLP UPGRADE BLUEPRINT
# ==========================================
elif st.session_state.room_step == 8:
    st.title("Your Alignment Mirror 🕊️")
    st.write("Take a deep breath. Exhale the armor. Your multi-dimensional somatic blueprint has been compiled.")
    st.audio("track5.mp3")
    
    st.markdown("---")
    st.header("✨ Your Unmasked Somatic Blueprint")
    st.write("Below is the record of the exact data markers and reflection journal answers you mapped across your internal castle today:")
    
    # Render Raw Answers for transparent validation
    with st.expander("Review Your Captured Journal Inputs"):
        st.markdown(f"**Primary Realm of Labor:**\n*{st.session_state.client_responses.get('room1_journal')}*")
        st.markdown(f"**Parenting Dynamic Load:**\n*{st.session_state.client_responses.get('room2_parenting_journal')}*")
        st.markdown(f"**Intimate & Sensual Self:**\n*{st.session_state.client_responses.get('room2_intimacy_journal')}*")
        st.markdown(f"**Physical Body & Tissues:**\n*{st.session_state.client_responses.get('room3_journal')}*")
        st.markdown(f"**Core Self-Worth Dialogue:**\n*{st.session_state.client_responses.get('room4_journal')}*")

    st.markdown("---")
    
    # AUDIT THE DASHBOARD FOR SYSTEM UPGRADE CALIBRATION
    fumes_areas = []
    
    if "clear boundaries" not in st.session_state.client_responses.get('room1_mirror', '') and "I honor my role at home" not in st.session_state.client_responses.get('room1_mirror', '') and "spaciousness and trust" not in st.session_state.client_responses.get('room1_mirror', ''):
        fumes_areas.append("💼 **Operational Optimization:** Your professional landscape is currently utilizing high processing power, drawing focus away from your baseline stillness.")
        
    if "calm authority" not in st.session_state.client_responses.get('room2_parenting_mirror', '') and "functional unit" not in st.session_state.client_responses.get('room2_parenting_mirror', ''):
        fumes_areas.append("🧒 **Family Dynamics:** Your domestic routine is requesting a shift in structural load sharing to allow your parenting style to flow with complete ease.")
        
    if "healthy part" not in st.session_state.client_responses.get('room2_intimacy_mirror', '') and "deep safety" not in st.session_state.client_responses.get('room2_intimacy_mirror', ''):
        fumes_areas.append("🥀 **Intimate & Sensual Self:** Your relational energy is resting in a protected posture, ready to expand back into its full warmth, luxury, and passion.")
        
    if "I am deeply attuned to my body" not in st.session_state.client_responses.get('room3_mirror', ''):
        fumes_areas.append("🩺 **Somatic Landscape:** Your physical body is absorbing the daily momentum, holding tension in the tissue rather than allowing for clean, restorative rest.")
        
    if "anchored in my inherent worth" not in st.session_state.client_responses.get('room4_mirror', ''):
        fumes_areas.append("👑 **Internal Dialogue Software:** Your inner narrative is relying on an output-driven performance script to validate your space, ready for a self-compassion update.")

    num_leaks = len(fumes_areas)
    
    st.subheader("📊 Candy's Dashboard Analysis")
    
    # TIER 1: TOTAL SYSTEMIC ALIGNMENT (0 leaks)
    if num_leaks == 0:
        st.markdown(
            "### **Your System is Operating at Peak Capacity.**\n\n"
            "Your internal dashboard is showing exceptional spaciousness, pristine boundaries, and a gorgeous, "
            "grounded connection to your sovereign worth. Your engine is firing on clean, integrated power across the board.\n\n"
            "This is precisely why we utilize **The Private Somatic Restoration Container** as an advanced masterclass architecture—to expand your capacity, evolve your vision, and allow your body to experience an even higher level of luxury, balance, and impact without compromise."
        )
        
    # TIER 2: SURGICAL PINPOINT MAINTENANCE (1 to 2 leaks) - POSITIVE NLP UPGRADE
    elif 1 <= num_leaks <= 2:
        st.markdown(
            "### **Targeted Optimization: Elevating a Specific Area to Match Your Standard.**\n\n"
            "Looking closely at your markers, your foundation is exceptionally brilliant. You have done beautiful, "
            "intentional work to protect your peace and navigate your lifestyle with mastery across the vast majority of your rooms. "
            "Your system is highly functional, which means you deserve a life where **every single piece** matches the high standard of what is already working well. "
            "Right now, there is just an isolated lag where your energy is running low or emptying out:"
        )
        for area in fumes_areas:
            st.markdown(area)
            
        st.markdown(
            "### 🔧 Calibrating the Lag\n\n"
            "Because the rest of your vehicle is running beautifully, we do not need a chaotic overhaul—we just need a refined software update. "
            "When one isolated area is running dry, it forces the high-performing parts of your life to carry extra momentum. "
            "You aren't broken; your system is simply ready to bring this single area up into complete calibration so your entire life runs seamlessly.\n\n"
            "In your **1-to-1 Somatic Release Session**, we will pull straight up on the lift, skip what is already thriving, and focus entirely "
            "on sealing this specific gap. We are here to run the exact system update needed so your body can rest in complete, uninterrupted wholeness. "
            "This is exactly why we design this container."
        )
        
    # TIER 3: SYSTEMIC OVERCOMPENSATION (3 or more leaks)
    else:
        st.markdown(
            "### **Systemic Reset: Ready for a Comprehensive Calibration.**\n\n"
            "Looking closely at your markers, your internal system is holding an immense amount of input. "
            "You have been relying on your raw strength, intellect, and execution to carry multiple areas of your life "
            "simultaneously. Your vehicle has been incredibly resilient, but several core operational lines are currently ready for a full system update:"
        )
        for area in fumes_areas:
            st.markdown(area)
            
        st.markdown(
            "### 🔧 Upgrading Your Entire System\n\n"
            "When multiple warning lights illuminate on your dashboard at once, trying to resolve them with mental willpower, strategy, or simply "
            "'pushing through' is like using an outdated operating system to run highly advanced software. You have evolved past your old coping loops, "
            "and your body is simply letting you know it is time for a complete upgrade to support the current season of your life.\n\n"
            "Our work inside **The Private Somatic Restoration Container** is designed for this exact level of elevation. We will open a premium, protected "
            "architecture to fully recalibrate your nervous system, physically update the patterns held in your tissue, and systematically balance "
            "every single dimension of your world so your energy runs completely clear and unforced."
        )

    st.markdown("---")
    st.subheader("🏛 ... Dedicated 30-Day Private Restoration Architecture")
    st.write(
        "To seamlessly align your internal software and ensure every single aspect of your lifestyle matches "
        "the brilliant capacity of your true essence, we step into a dedicated, three-phase framework:"
    )
    
    st.markdown("#### Phase 1: The Private Somatic Release Session")
    st.write("A live, dedicated 1-to-1 deep dive container where we pop open the hood, map your exact somatic calibration points, and guide your body to physically update and release any old processing pressure or lingering tissue residue.")
    
    st.markdown("#### Phase 2: The 21-Day Protected Integration")
    st.write("Three weeks of protected integration loops equipped with daily somatic resource tracks and custom practices designed specifically to anchor your new, upgraded operational boundaries.")
    
    st.markdown("#### Phase 3: The Weeks 3 & 4 Alignment Check")
    st.write("A dedicated review container to lock in your systemic calibration and ensure your lifestyle runs smoothly for the long haul.")
    
    st.markdown("---")
    st.markdown("### 🕊 Container Logistics & Booking")
    st.write(
        "The foundational investment for this complete three-phase dynamic somatic architecture is **$750**.\n\n"
        "To officially claim this system upgrade, lock your exploration profile onto Candy's private desk, and receive your "
        "secure calendar invitation to select your live session time, click the submit button below."
    )
    
    st.markdown("---")
    
    # INTERACTIVE SUBMIT BUTTON ARCHITECTURE
    if 'submitted' not in st.session_state:
        if st.button("Submit My Somatic Profile to Candy 🕊"):
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
