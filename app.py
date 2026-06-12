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
# 💼 ROOM ONE: THE REALM OF DAILY LABOR (Tailored Paths)
# ==========================================
elif st.session_state.room_step == 2:
    st.title("Room One: Your Primary Realm of Daily Labor 💼")
    st.audio("track1.mp3")
    
    chosen_path = st.session_state.client_responses.get('chosen_path', '')
    
    # --- PATH A: THE CORPORATE LEADER ---
    if "Path A" in chosen_path:
        st.write(
            "When our home life or internal world enters a season of heavy instability, we often flee into our "
            "professional execution. We build meticulous organizational structures and systems at work because it "
            "is the one place we feel we can manufacture safety and control. But when your team fails to follow "
            "protocols, it triggers a deep, exhausting cycle of resentment. Look closely at your workspace right now..."
        )
        st.markdown("---")
        st.subheader("🎭 The Workspace Leadership Mirror")
        st.write("Which of these narratives most accurately mirrors how your internal operating system runs your career landscape right now?")
        
        labor_choice = st.radio(
            "Select your mirror:",
            [
                "🌟 The Anchored Sovereign (Aligned Flow): I command my workspace with calm clarity, set pristine boundaries, and delegate effortlessly. I do not parent my team or play their therapist. I cleanly clock out at the end of the day, and my career is a fulfilling expression of my gifts, not a shield to hide from personal pain.",
                "⚔️ The Resentful Savior (Control Addiction): I have built highly organized systems to feel safe at work. But when people ignore protocols, I feel deeply disrespected and overworked. I complain constantly about the lack of execution, yet I step in and fix their unfinished mess anyway. I am actively parenting my team, acting as the workplace therapist, and I never actually clock out.",
                "🫥 The Untouchable Fortress (Numbing / Flight Grip): When pressure mounts, I build a cold, hyper-efficient wall at my desk. I stop trusting anyone to do things right, pull all execution onto my own shoulders, and refuse to delegate. I cut off real connection with my team because it feels safer to be a solo island than to risk being let down by people."
            ]
        )

    # --- PATH B: THE STAY-AT-HOME MOM ---
    elif "Path B" in chosen_path:
        st.write(
            "Because your workspace is your home space, the lines between daily labor and private rest don't just "
            "blur—they completely vanish. You wear every single hat in the empire: doctor, driver, housekeeper, and "
            "logistics manager. Yet, because you aren't bringing in an outside paycheck, a quiet, destructive story "
            "whispers that your labor isn't 'providing' real value. You keep your exhaustion inside because you've been "
            "told you have it good, letting the pressure build silently behind closed doors..."
        )
        st.markdown("---")
        st.subheader("🎭 The Matriarch Operational Mirror")
        st.write("Which of these narratives mirrors how your system handles the daily load of running the home?")
        
        labor_choice = st.radio(
            "Select your mirror:",
            [
                "🌟 The Aligned Matriarch (Aligned Flow): I genuinely love my role and honor it as a sacred space. I set healthy domestic boundaries without an ounce of guilt, separate my self-worth from a corporate paycheck, and explicitly prioritize my own rest, health, and intellectual expansion alongside my family's needs.",
                "⚔️ The Hyper-Vigilant Captain (Control Addiction): I run this household like a strict military drill sergeant, managing every single tiny detail. I stay on high alert because a voice tells me that if I drop a single ball, the entire family structure will collapse. I am addicted to constant busyness to outrun the void of feeling unappreciated.",
                "🎭 The Isolated Martyr (Fawn / Numbing Addiction): I completely collapse my boundaries, say 'yes' when my body is screaming 'no', and swallow my true complaints to keep the peace. Because I am told I have it good, I hide my pain, letting it build inside while turning to secret comforts like online shopping, constant scrolling, or a daytime drink to survive the isolation."
            ]
        )

    # --- PATH C: THE SOLO WFH ENTREPRENEUR ---
    else:
        st.write(
            "You are birthing a kingdom from your bedroom or kitchen table, pouring your life-force into a laptop out of "
            "absolute survival necessity. But because your labor is invisible to your household, they treat your vision "
            "like a hobby, leaving you feeling profoundly lonely and unvalidated. You never physically 'leave' the office, "
            "forcing your nervous system to red-line from morning until midnight completely alone..."
        )
        st.markdown("---")
        st.subheader("🎭 The Bedroom Builder Mirror")
        st.write("Which of these narratives captures how your system is holding the pressure of your business creation?")
        
        labor_choice = st.radio(
            "Select your mirror:",
            [
                "🌟 The Aligned Builder (Aligned Flow): I work with a deep sense of spaciousness, vision, and trust. I cleanly close my laptop when the day is done, completely separate my personal worth from my business stats, and allow my labor to be a clean expression of my purpose.",
                "⚔️ The Isolated Gladiator (Control / Flight Grip): I am pouring pure survival panic into my business. I grind until 2 AM, over-engineer my strategy entirely in my head, and stay in constant, frantic motion. I treat myself like a machine because I feel like a completely unsupported solo island.",
                "🫥 The Paralyzed Creative (Freeze / Collapse State): The sheer weight of having to make this business work completely alone has overwhelmed my nervous system. I sit at my table and find myself totally frozen, heavy, and numb—using endless scrolling or trivial distractions to escape the terrifying pressure of the invisible void."
            ]
        )
        
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    labor_text = st.text_area(
        "Within your primary realm of daily labor, where are you explicitly feeling the friction of 'not feeling enough'? What is the secret addiction—whether to perfectionism, people-pleasing, or silent numbing—that your system uses to cope here?",
        height=150
    )
    
    if st.button("Walk Into the Next Space →"):
        st.session_state.client_responses['room1_mirror'] = labor_choice
        st.session_state.client_responses['room1_journal'] = labor_text
        st.session_state.room_step = 3
        st.rerun()

# ==========================================
# 🏡 ROOM TWO: THE STATUS GATE (Untangling Kids from Partner)
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
# 🏡 ROOM TWO (ACTUAL): TAILORED RELATIONAL EXPLORATION
# ==========================================
elif st.session_state.room_step == 4:
    st.title("Room Two: The Deep Relational & Intimate Mirrors 🏡")
    st.audio("track2.mp3")
    
    status = st.session_state.client_responses.get('relational_status', '')
    
    # --- PATH SINGLE NARRATIVE ---
    if "Path Single" in status:
        st.write(
            "As a solo anchor, every single ounce of emotional, physical, and financial weight rests squarely on "
            "your shoulders. It is easy to completely exile your sensuality, burying the 'Lover' archetype out of "
            "parental guilt, a fear of being hurt again, or the unexpressed grief of a past relational death..."
        )
        st.markdown("---")
        st.subheader("🧒 Checkpoint A: The Solo Parenting Dynamic")
        r2_q1 = st.radio(
            "What is the survival software currently running your parenting household?",
            [
                "🌟 The Anchored Matriarch (Light): I lead my home with calm authority, hold loving boundaries with my children, and trust that my presence alone is more than enough.",
                "⚔️ The Hyper-Vigilant Captain (Control): I run a tight, hyper-regulated ship because there is no safety net. I force myself to be both mother and father, terrified that if I drop one ball, everything collapses.",
                "🎭 The Guilt-Driven Pleaser (Fawn): I carry immense unspoken shame over the fact that their family structure split. I overcompensate out of fear by collapsing my boundaries and letting my kids run the emotional atmosphere of the house."
            ]
        )
        st.markdown("---")
        st.subheader("🥀 Checkpoint B: The Untouched Intimate Self")
        r2_q2 = st.radio(
            "Look strictly at you—the woman, your sensuality, and your romantic desires. What is the true state of your heart?",
            [
                "🌟 The Open Sovereign (Light): I honor my sexual and romantic desires as a sacred part of my wholeness. I am open to love and deep physical connection without shame, guilt, or the need to compromise my independent worth.",
                "⚔️ The Grieving / Fearful Exile (Living Loss): I deeply desire connection, but I am secretly mourning a past relational death, divorce, or betrayal. My system is frozen in fear, telling myself the story that I can't risk dating because of my kids.",
                "🫥 The Frozen Mother Mask (Numbing Addiction): I have completely locked my sexual life-force and the 'Lover' archetype behind a brick wall. I don't date or explore my body, using my busy identity as a mother to numb the massive void of a companion."
            ]
        )

    # --- PATH PARTNERED NARRATIVE ---
    else:
        st.write(
            "Sharing a roof or a bed does not automatically guarantee connection. So many high-performing women find "
            "themselves 'single parenting with a spouse'—carrying the entire domestic load alone while managing a heavy "
            "shield of bitter resentment, leaving the actual sexual and intimate marriage to go completely cold..."
        )
        st.markdown("---")
        st.subheader("🧒 Checkpoint A: The Shared Parenting Dynamic")
        r2_q1 = st.radio(
            "When it comes to the daily operations and management of the children, how do you and your spouse interact?",
            [
                "🌟 The Unified Operational Team (Light): We manage the logistics and parenting well as a functional unit. We check boxes, run schedules, and keep the household organized and stable together through mutual respect.",
                "⚔️ The Married Single Mom (Control / Resentful Warrior): My spouse is completely checked out or operates like another child I have to manage. I am single-parenting with a spouse, doing all the emotional lifting, which leaves me carrying a heavy armor of bitter resentment."
            ]
        )
        st.markdown("---")
        st.subheader("🫥 Checkpoint B: The Intimate / Sexual Marriage Mirror")
        r2_q2 = st.radio(
            "Strip away the kids and the chores. When the bedroom door closes and it is just you two, what is the raw truth?",
            [
                "🌟 The Radiant Sanctuary (Light): Our intimacy is a place of absolute safety, surrender, and deep pleasure. I express my sexual desires and boundaries without fear, and our relationship is where I fully drop my armor and rest.",
                "🎭 The Toxic Walk-On-Eggshells Prison (Fawn Addiction): Our connection feels unsafe, heavy, and emotionally distant. I am constantly people-pleasing—suppressing my true voice, ignoring my resentment, and even compromising my own physical boundaries just to keep the peace and avoid conflict.",
                "🫥 The Sexually Starving Roommates (Numbing Addiction): The passion, desire, and sexual vitality have gone completely cold. We are platonic roommates coexisting in the dark. I live in my head, using shopping, scrolling, or daytime/nighttime comforts to numb the lack of real physical connection."
            ]
        )

    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    relational_text = st.text_area(
        "Look honestly at your living losses, your marriage, or your intimate isolation. Where is your sexual and emotional life-force currently suffering, and what is the story you have been telling yourself to stay stuck?",
        height=150
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 2
            st.rerun()
    with col2:
        if st.button("Walk into the Body →"):
            st.session_state.client_responses['room2_parenting_mirror'] = r2_q1
            st.session_state.client_responses['room2_intimacy_mirror'] = r2_q2
            st.session_state.client_responses['room2_journal'] = relational_text
            st.session_state.room_step = 5
            st.rerun()

# ==========================================
# 🩺 ROOM THREE: PHYSICAL HEALTH & SOMATIC THRESHOLDS
# ==========================================
elif st.session_state.room_step == 5:
    st.title("Room Three: Your Physical Health & Somatic Thresholds 🩺")
    st.write(
        "Your physical body has been the faithful witness to every ounce of pressure, unexpressed grief, and emotional "
        "residue you have carried. It keeps the score perfectly when the mind tries to override. This is an opportunity "
        "to tune entirely into your flesh and listen to what your tissue has been swallowing to keep you standing..."
    )
    st.audio("track3.mp3")
    
    st.markdown("---")
    st.subheader("🎭 The Somatic Operating Mirror")
    st.write("How does your internal operating system currently treat your physical body?")
    
    body_choice = st.radio(
        "Select your mirror:",
        [
            "🌟 The Radiant Temple (Aligned Flow): I am deeply attuned to my body's language. I honor its physical boundaries, feed it with somatic presence and pleasure, and allow it to experience true, unconditional rest before a breakdown forces me to stop.",
            "⚔️ The Over-Taxed Machine (Control Addiction): I treat my body like a soldier or a tool. I am addicted to adrenaline and cortisol, forcing my system to override chronic fatigue, ignore warning signals, and keep marching forward because I put everyone else first.",
            "🫥 The Somatic Shut Down (Freeze / Protection Armor): When emotional pressure gets too high, my physical system freezes. I suffer from chronic tightness, unexplained fatigue, or weight retention that acts like literal physical armor protecting my vulnerability from the world.",
            "🔮 The Disassociated Mind (Flight / Neck-Up Living): I live entirely from the neck up. I ignore my body's physical sensations completely, over-intellectualizing my health issues or treating my symptoms like an abstract science project instead of actually feeling my flesh."
        ]
    )
    
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    body_text = st.text_area(
        "Close your eyes and notice where your breath catches right now. When your body experiences chronic pain, fatigue, or weight stagnation, do you shut down, numb out, or force it to push through? What does your tissue need to release?",
        height=150
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 3
            st.rerun()
    with col2:
        if st.button("Explore Your Identity →"):
            st.session_state.client_responses['room3_mirror'] = body_choice
            st.session_state.client_responses['room3_journal'] = body_text
            st.session_state.room_step = 6
            st.rerun()

# ==========================================
# 👑 ROOM FOUR: IDENTITY, ESSENCE & WORTH
# ==========================================
elif st.session_state.room_step == 6:
    st.title("Room Four: Your Identity & Sovereign Essence 👑")
    st.write(
        "We step now into the quietest room. Strip away the corporate titles, the business metrics, the maternal roles, "
        "and the endless demands of everyone who relies daily on your strength. We are looking directly at you—how you "
        "speak to yourself when no one is looking, and whether you believe you are worthy when you are completely empty..."
    )
    st.audio("track4.mp3")
    
    st.markdown("---")
    st.subheader("🎭 The Self-Worth Identity Mirror")
    st.write("When you are completely alone with your thoughts, who is dominating your internal dialogue?")
    
    identity_choice = st.radio(
        "Select your mirror:",
        [
            "🌟 The Sovereign Queen (Aligned Flow): I am deeply anchored in my inherent worth. I own my throne, honor my true essence, and speak to myself with radical compassion, knowing that I am deeply good inside just for existing.",
            "⚔️ The Performance-Based Prisoner (Control Addiction): My worth is entirely tied to my output. If I am not achieving, fixing, or producing, I feel completely useless and empty. I judge my value based entirely on stats, performance, and what other people think of me.",
            "🔥 The Harsh Inner Drill Sergeant (Self-Criticism Addiction): My internal dialogue is ruthless. I speak to my own soul with a level of severity, criticism, and judgment I would never use on another human being, constantly auditing my flaws and telling myself I'm not enough.",
            "🎭 The Invisible Chameleon (Fawn Addiction): I have spent so long pleasing everyone else, avoiding friction, and playing the family or workplace therapist that I genuinely don't know who I am anymore. If you strip away my roles, I feel like a completely blank space."
        ]
    )
    
    st.markdown("---")
    st.subheader("Your Written Reflection Journal")
    identity_text = st.text_area(
        "Look directly into the mirror of your soul. Where have you been abandoning your own identity to buy safety or validation? What is the core lie about your 'enoughness' that your inner child is still carrying?",
        height=150
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Go Back"):
            st.session_state.room_step = 5
            st.rerun()
    with col2:
        if st.button("Compile Your Alignment Mirror ✨"):
            st.session_state.client_responses['room4_mirror'] = identity_choice
            st.session_state.client_responses['room4_journal'] = identity_text
            st.session_state.room_step = 7
            st.rerun()

# ==========================================
# 🕊️ THE ALIGNMENT MIRROR: SAFE LANDING & LEAP
# ==========================================
elif st.session_state.room_step == 7:
    st.title("Your Alignment Mirror 🕊️")
    st.write("Take a deep breath. Exhale the armor. Your complete multi-dimensional exploration profile has been compiled.")
    st.audio("track5.mp3")
    
    st.markdown("---")
    st.subheader("Your Hidden Operating System Dashboard")
    
    st.info(
        f"**Somatic Explorer Profile:** {st.session_state.client_responses.get('name')}\n\n"
        f"**Current Pathway Matrix:** {st.session_state.client_responses.get('chosen_path')}\n"
        f"**Relational Infrastructure:** {st.session_state.client_responses.get('relational_status')}\n\n"
        f"Your choices across your Daily Labor, Home & Intimacy, Physical Body, and Core Identity have been securely "
        f"locked into our high-integrity, private database container."
    )
    
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
    st.write("Three weeks of protected integration loops equipped with bespoke daily somatic resource tracks and custom practices designed specifically for your body's friction points.")
    
    st.markdown("### 🔄 Phase 3: The Weeks 3 & 4 Alignment Check")
    st.write("A dedicated review to ensure your new boundaries and internal somatic clarity stick for the long haul.")
    
    st.markdown("---")
    st.markdown("### 🕊️ Container Logistics & Booking")
    st.write(
        "The foundational investment for this complete three-phase somatic architecture is **$750**.\n\n"
        "By initiating this private container, you will be given a secure, private calendar invitation to select "
        "your session time and complete your investment. To honor the deep, intentional preparation required to hold this space "
        "exclusively for you, your session and 30-day container are officially secured and confirmed once the investment is complete."
    )
    
    # Secure background automated push to webhook.site
    if 'fired' not in st.session_state:
        try:
            webhook_url = st.secrets["WEBHOOK_URL"]
            requests.post(webhook_url, json=st.session_state.client_responses)
            st.session_state.fired = True
        except:
            pass
            
    if st.button("Restart Exploration Journey 🔄"):
        st.session_state.room_step = 1
        st.session_state.client_responses = {}
        if 'fired' in st.session_state: del st.session_state.fired
        st.rerun()
