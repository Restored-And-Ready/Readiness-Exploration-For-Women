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
        "Welcome. This isn't a stiff test or a clinical interview. Think of this as a quiet space to step back, "
        "take off the armor, and look honestly at how you're running your life. Give yourself permission to be completely "
        "unmasked here. We're looking at how you are natively wired versus how you learned to survive."
    )
    
    st.markdown("---")
    st.subheader("Let's Get Started")
    name = st.text_input("First & Last Name", value=st.session_state.client_responses.get('name', ''))
    email = st.text_input("Private Email Address", value=st.session_state.client_responses.get('email', ''))
    age = st.text_input("Age / Current Season of Life", value=st.session_state.client_responses.get('age', ''))
    
    st.markdown("---")
    st.subheader("Where is your energy focused daily?")
    st.write("To make sure the reflection questions match your actual daily life, choose the path below that best fits your current world:")
    
    path_selection = st.radio(
        "Choose your path:",
        [
            "💼 Path A: The Corporate Leader / Executive / Manager (My workspace and home are completely separate; I run outside teams or systems).",
            "🏡 Path B: The Stay-at-Home Mom / Matriarch (My workspace is my home; my daily work and family life are fully connected).",
            "💻 Path C: The Solo WFH Entrepreneur / Visionary (I am building a brand or business from home, facing collapsed boundaries and do it all myself)."
        ],
        index=0
    )
    
    st.markdown("---")
    commit = st.checkbox("I commit to giving myself 30 to 60 minutes of uninterrupted time to honor this space and find my truth.")
    
    if st.button("Step Inside"):
        if name and email:
            if commit:
                st.session_state.client_responses['name'] = name
                st.session_state.client_responses['email'] = email
                st.session_state.client_responses['age'] = age
                st.session_state.client_responses['chosen_path'] = path_selection
                st.session_state.room_step = 2
                st.rerun()
            else:
                st.warning("Please check the commitment box to claim this private time for yourself.")
        else:
            st.warning("Please provide your name and email so we can securely build your custom dashboard.")

# ==========================================
# 💼 ROOM ONE: THE REALM OF DAILY LABOR
# ==========================================
elif st.session_state.room_step == 2:
    st.title("Room One: Your Daily Work 💼")
    st.audio("track1.mp3")
    
    chosen_path = st.session_state.client_responses.get('chosen_path', '')
    labor_prompt_text = ""
    
    # --- PATH A: THE CORPORATE LEADER ---
    if "Path A" in chosen_path:
        st.write(
            "Running a team and managing a workspace takes a massive amount of coordination. When our home life "
            "or internal world feels up and down, we often dive into work to feel in control. We build tight structures "
            "because it’s the one place we can guarantee results. Let's look under the hood and see how holding "
            "that high-level responsibility affects how you feel when you finally turn off the lights at the end of the day."
        )
        st.markdown("---")
        st.subheader("How do you currently navigate your workspace?")
        
        labor_choice = st.radio(
            "Select the description that matches your day-to-day reality:",
            [
                "I operate with clear boundaries and delegate tasks with ease. I can step away from my desk at the end of the day without carrying the emotional weight or fixing the personal problems of my team.",
                "I have built precise systems to ensure things are done right, but when people skip protocols, I feel deeply compromised. I find myself stepping in to fix their unfinished work while carrying a heavy layer of unspoken resentment.",
                "When workplace pressure or chaos mounts, I find myself pulling a cold wall down around my desk. I stop trusting others to execute accurately, pull all the responsibility onto myself, and treat my workspace like a solo island."
            ]
        )
        
        if "clear boundaries" in labor_choice:
            labor_prompt_text = "What does it feel like to lead from this space of clean alignment? What specific boundaries are you currently using to successfully protect your peace?"
        elif "precise systems" in labor_choice:
            labor_prompt_text = "Where do you feel the heavy friction of parenting your team? What is the unspoken cost of stepping in and fixing everyone else's unfinished work?"
        else:
            labor_prompt_text = "What are you protecting yourself from by pulling all execution onto your solo island? What are you afraid will happen if you lower your guard and trust people?"

    # --- PATH B: THE STAY-AT-HOME MOM ---
    elif "Path B" in chosen_path:
        st.write(
            "Running a household and keeping a family thriving means you're always on. Because your home is your workspace, "
            "the lines between work, parenting, and rest disappear fast. You wear every single hat in the empire—logistics manager, "
            "driver, scheduler, and chef. Let's see how managing it all impacts your daily peace."
        )
        st.markdown("---")
        st.subheader("How does your system currently hold the daily load of running the home?")
        
        labor_choice = st.radio(
            "Select the description that matches your day-to-day reality:",
            [
                "I honor my role at home as a beautiful space. I can set clear domestic boundaries without guilt, disconnect my worth from an external paycheck, and confidently prioritize my own recovery, health, and rest alongside my family's needs.",
                "I find myself running this household like a strict operational drill, managing every tiny detail. I stay on constant high alert because a voice inside tells me that if I drop a single logistical ball, the entire family structure will fall apart.",
                "I frequently collapse my boundaries, saying yes when my body is screaming no, and swallow my true complaints to keep the peace. I turn to secret comforts—like endless scrolling, online shopping, or a quiet drink—just to survive the isolation."
            ]
        )
        
        if "I honor my role at home" in labor_choice:
            labor_prompt_text = "How do you successfully separate your internal worth from a paycheck? What does prioritizing your own health and rest look like in your weekly routine?"
        elif "strict operational drill" in labor_choice:
            labor_prompt_text = "What are you worried will happen if you drop a single domestic ball? Where did you first learn that you are only safe if you are perfectly managing everything around you?"
        else:
            labor_prompt_text = "What specific unexpressed pain or grief are you swallowing to keep the peace? What empty space are the quiet drinks, scrolling, or Amazon packages trying to fill?"

    # --- PATH C: THE SOLO WFH ENTREPRENEUR ---
    else:
        st.write(
            "Building a business from home means your laptop or computer is your constant companion. You're pouring your "
            "life-force and passion into your vision, often completely alone. Let's deep dive into your current venture "
            "and see how holding this massive dream entirely on your own affects your mind and body."
        )
        st.markdown("---")
        st.subheader("How are you currently handling the pressure of building your business?")
        
        labor_choice = st.radio(
            "Select the description that matches your day-to-day reality:",
            [
                "I create and operate my business with a sense of spaciousness and trust. I can cleanly close my laptop when the day is done, completely separate my personal worth from my stats, and let my work be an unforced expression of my purpose.",
                "I am pouring survival panic into my brand. I find myself grinding until 2 AM, over-engineer my strategy entirely in my head, and staying in frantic motion because I feel like an completely unsupported, isolated island.",
                "The sheer pressure of trying to build this business entirely alone has overwhelmed my system. I sit at my computer and find myself completely frozen, heavy, and numb—using trivial distractions or scrolling to escape the weight."
            ]
        )
        
        if "spaciousness and trust" in labor_choice:
            labor_prompt_text = "How does operating from deep trust alter your creative clarity? How do you cleanly disconnect your personal value from your daily revenue or social stats?"
        elif "survival panic" in labor_choice:
            labor_prompt_text = "What adjustments to your timeline or structure would allow your business expansion to feel more spacious and unforced? What are you running from at 2 AM?"
        else:
            labor_prompt_text = "Where exactly does your creative energy flow best when the pressure drops? What do you need right now to feel completely supported as you take your next small step?"
        
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
    st.title("Room Two: Your Home & Relationships 🏡")
    st.write(
        "Now, let's look behind closed doors—into your closest relationships, your family dynamics, and the "
        "core of your intimacy and sexual vitality. It's so easy for a woman to completely tangle her identity as a mother "
        "with her identity as a romantic woman, often burying her private desires under the family schedule. "
        "Let's untangle this. Select your current status below:"
    )
    
    st.markdown("---")
    relational_status = st.radio(
        "Select your current relationship landscape:",
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
            "As a solo anchor, the daily emotional, physical, and financial details rest on your shoulders. "
            "Let's look honestly at how your home currently feels:"
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
            parenting_prompt_text = "Your parenting landscape is reflecting a beautiful state of clean alignment. What boundaries or shifts have allowed you to cultivate this peace?"
        elif "highly regulated" in parenting_choice:
            parenting_prompt_text = "What does it physically cost your spirit to carry the full weight of provider and protector entirely alone? Where can you allow yourself to receive support?"
        else:
            parenting_prompt_text = "What specific past failure or family change are you trying to overcompensate for by letting your boundaries collapse?"
            
    else:
        st.write(
            "Sharing a roof doesn't always mean shared work. Let's look at how the daily routines, "
            "emotional weight, and parenting duties are actually balanced between you and your partner:"
        )
        st.markdown("---")
        parenting_choice = st.radio(
            "Which of these descriptions captures your current co-parenting reality?",
            [
                "We manage the logistics and daily routines well as a functional unit. We communicate with mutual respect, share the loads evenly, and keep the household organized and stable together.",
                "I am essentially single-parenting with a spouse. My partner is completely checked out or acts like another child I have to manage. I carry the entire emotional and physical workload alone while shielding a deep layer of bitter resentment."
            ]
        )
        
        if "functional unit" in parenting_choice:
            parenting_prompt_text = "Your household teamwork is operating in a beautiful space. How do you and your partner actively maintain this mutual respect and shared flow without dropping into resentment?"
        else:
            parenting_prompt_text = "What is the true weight of single-parenting with a spouse? How deep does that silent, bitter resentment run toward your partner, and how is it draining your energy daily?"

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
            "Let's strip away your responsibilities to your children. This is just about you—the woman, your sensuality, "
            "and your romantic desires. What is the raw reality inside your heart?"
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
            intimacy_prompt_text = "Your intimate heart is open and aligned. What does this deep emotional security allow you to confidently welcome or explore next in your life?"
        elif "secretly mourning" in intimacy_choice:
            intimacy_prompt_text = "What is the name of the past heartbreak or divorce your heart is still actively processing? What terrifies you about lowering your guard and letting someone in again?"
        else:
            intimacy_prompt_text = "You've hidden your sensual self behind the mask of a busy mother. What would happen if you allowed yourself to admit that you deeply crave romance and touch?"

    else:
        st.write(
            "Let's look past the kids, the schedules, and the household chores. When the bedroom door closes and it is "
            "just you and your partner, what is the honest truth of your connection?"
        )
        st.markdown("---")
        intimacy_choice = st.radio(
            "Which of these statements best captures your current marital intimacy?",
            [
                "Our intimacy is a space of deep safety, pleasure, and emotional surrender. I express my true desires and boundaries without fear, and our relationship is where I drop my armor and experience true rest.",
                "Our relationship feels emotionally distant or heavy. I find myself constantly people-pleasing—suppressing my real voice, ignoring my own boundaries, and doing whatever it takes just to keep the peace and avoid conflict.",
                "The passion and physical vitality have gone completely cold. We are platonic roommates coexisting in the dark. I spend my evenings escaping into my head, using shopping, scrolling, or quiet distractions to numb the void between us."
            ]
        )
        
        if "deep safety" in intimacy_choice:
            intimacy_prompt_text = "Your bedroom connection is a real sanctuary. What does this deep safety and pleasure unlock for your life and your personal vision?"
        elif "emotionally distant" in intimacy_choice:
            intimacy_prompt_text = "Where exactly are you compromising your own physical or emotional boundaries inside your intimacy just to avoid conflict, judgment, or tension?"
        else:
            intimacy_prompt_text = "You are platonic roommates coexisting in the dark. What outside comforts (online shopping, constant scrolling, quiet drinks) are you using to fill the void of real physical connection?"

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
# 🩺 ROOM THREE: PHYSICAL HEALTH
# ==========================================
elif st.session_state.room_step == 6:
    st.title("Room Three: Your Physical Body 🩺")
    st.write(
        "Your body is the faithful witness to every ounce of pressure, unexpressed grief, and stress you carry. "
        "It keeps the score perfectly when our minds try to power through. Let's tune in and listen to what your body is saying:"
    )
    st.audio("track3.mp3")
    
    st.markdown("---")
    st.subheader("How do you currently treat your physical body?")
    
    body_choice = st.radio(
        "Select the statement that best describes your relation to your physical health:",
        [
            "I am deeply attuned to my body's language. I honor its physical boundaries, protect its need for true rest, and respond to its whispers before a physical breakdown forces me to stop.",
            "I treat my body like a machine or a soldier. I run on adrenaline and cortisol, cancel my own appointments to prioritize everyone else, and force my system to march through pain and exhaustion.",
            "When the emotional or mental pressure gets too heavy, my physical system locks up. I struggle with chronic tightness, unexplainable fatigue, or stubborn weight retention that feels like a layer of protective armor.",
            "I live almost entirely inside my analytical head. I disconnect from physical sensations completely, over-intellectualizing my health issues or treating my symptoms like an abstract science project instead of actually feeling my flesh."
        ]
    )
    
    if "attuned to my body" in body_choice:
        body_prompt_text = "Your body is operating in clear alignment. What specific practices or rest boundaries are successfully keeping your physical temple so radiant right now?"
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
# 👑 ROOM FOUR: IDENTITY & WORTH
# ==========================================
elif st.session_state.room_step == 7:
    st.title("Room Four: Your Core Self 👑")
    st.write(
        "We step now into the quietest room. Strip away the titles, the business metrics, the maternal roles, "
        "and the endless demands of everyone who relies on your strength. We are looking directly at you."
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
        identity_prompt_text = "You are resting in your inherent worth. What does it physically feel like to fully accept your own enoughness without needing to perform or produce for anyone?"
    elif "chained to my output" in identity_choice:
        identity_prompt_text = "What does an unshakeable, internal sense of enoughness look like when you are in absolute stillness? Who is the sovereign woman that exists beneath the production?"
    elif "hyper-critical" in identity_choice:
        identity_prompt_text = "What words of radical compassion, validation, and ultimate safety is your inner child ready to receive from you right now? What is your true internal truth?"
    else:
        identity_choice = "Who are you when you step into the room completely for yourself? What do your true, unmasked desires and creative longings look like when no one else is watching?"
        
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
# 🕊️ THE ALIGNMENT MIRROR: CANDY'S TRUE TAPESTRY OPENING
# ==========================================
elif st.session_state.room_step == 8:
    st.title("Your Alignment Mirror 🕊️")
    st.write("Take a deep breath. Let it out. Your private somatic blueprint is completely ready.")
    st.audio("track5.mp3")
    
    st.markdown("---")
    st.header("✨ Your Private Reflection Report")
    
    # --- CANDY'S FULLY HUMANIZED SOVEREIGN LIFESTYLE TRANSMISSION ---
    st.markdown("### 🎭 The Many Faces of Your Native Wiring")
    st.write(
        "Look closely at the text answers you mapped out across these rooms today. What you are looking at is "
        "not a clinical diagnosis, a rigid commercial category, or a list of flaws. It is simply a live snapshot of "
        "how you have elegantly learned to navigate your world."
    )
    st.write(
        "As a multi-faceted, high-performing woman, you were beautifully engineered to activate entirely different internal "
        "postures—or *faces*—depending on the room you stand in. You hold the **Sovereign** and the **Warrior** to protect and "
        "execute at your desk, the **Matriarch** to hold the operational details of your household together, and the intuitive "
        "**Magician** to create. Deep down inside, you also hold the sacred **Lover**—the side of you meant for pure, unforced surrender, "
        "passion, and deep rest behind closed doors."
    )
    st.write(
        "True systemic exhaustion doesn't mean you are broken. It happens because our modern environment constantly forces our boundaries to dissolve. "
        "When the lines blur completely, you accidentally get stuck in a single gear. You find yourself carrying the protective armor of the Warrior "
        "from your desk straight into your family dynamics or your marriage, until you lose the margin to know where one state ends and the next begins. "
        "When those temporary survival states lock together, you stop wearing them as temporary tools and begin to mistake them for your *actual identity*. "
        "You stop saying 'I am currently in my Warrior gear' and begin to believe 'I *am* just an exhausted workhorse.'"
    )
    st.write(
        "**Here is the foundational truth you must anchor into today:** You are natively built for a state of *Shalom*—complete, unyielding "
        "internal wholeness. Every behavior, pattern, and moment of quiet numbing you uncovered today is just a rule your software created to preserve "
        "your peace in a world that constantly demands performance over presence. But you are not the roles you play. **You are the driver, and you hold "
        "the keys to this entire vehicle.**"
    )
    
    st.markdown("---")
    st.write("Below is your complete, raw, unmasked data profile from your walk today:")
    
    # Render Raw Answers for transparent verification
    with st.expander("Review Your Private Reflections"):
        st.markdown(f"**Your Daily Work:**\n*{st.session_state.client_responses.get('room1_journal')}*")
        st.markdown(f"**Parenting Dynamic Load:**\n*{st.session_state.client_responses.get('room2_parenting_journal')}*")
        st.markdown(f"**Intimate & Sensual Self:**\n*{st.session_state.client_responses.get('room2_intimacy_journal')}*")
        st.markdown(f"**Physical Body & Tissues:**\n*{st.session_state.client_responses.get('room3_journal')}*")
        st.markdown(f"**Core Self Dialogue:**\n*{st.session_state.client_responses.get('room4_journal')}*")

    # HIGH-END INTERACTIVE HTML BLUEPRINT DOWNLOAD WRAPPER (SOUL-ALIGNED VERSION)
    html_blueprint_data = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>The Unlabeled Somatic Blueprint</title>
        <style>
            body {{ background-color: #FDFBF7; color: #2C2523; font-family: 'Helvetica Neue', Arial, sans-serif; padding: 50px; max-width: 750px; margin: 0 auto; line-height: 1.6; }}
            h1 {{ color: #5C1D24; font-family: 'Georgia', serif; font-size: 2.4rem; font-weight: normal; border-bottom: 1px solid #E2DDD5; padding-bottom: 15px; margin-bottom: 30px; }}
            h2 {{ color: #5C1D24; font-family: 'Georgia', serif; font-size: 1.5rem; font-weight: normal; margin-top: 35px; }}
            p {{ font-size: 1.1rem; color: #4A3E3B; }}
            .metadata {{ font-style: italic; color: #7A6B66; background: #F7F4EF; padding: 15px 25px; border-radius: 4px; margin-bottom: 40px; border: 1px solid #E2DDD5; }}
            .educational-block {{ border: 1px dashed #5C1D24; background-color: #FFFDF9; padding: 25px; border-radius: 6px; margin-bottom: 35px; }}
            .journal-block {{ background-color: #F7F4EF; border-left: 4px solid #5C1D24; padding: 20px 30px; margin-bottom: 25px; font-style: italic; color: #2C2523; font-size: 1.1rem; border-radius: 0 4px 4px 0; }}
            footer {{ text-align: center; margin-top: 60px; font-family: 'Georgia', serif; color: #7A6B66; font-style: italic; border-top: 1px solid #E2DDD5; padding-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>My Unmasked Somatic Blueprint 🕊️</h1>
        <div class="metadata">
            <p><strong>Somatic Explorer:</strong> {st.session_state.client_responses.get('name', 'Anonymous')}</p>
            <p><strong>Current Season / Age:</strong> {st.session_state.client_responses.get('age', 'Unspecified')}</p>
            <p><strong>Primary Daily Landscape:</strong> {st.session_state.client_responses.get('chosen_path', 'Unspecified')}</p>
        </div>
        
        <div class="educational-block">
            <h2>🎭 The Architecture of Your Diverse States</h2>
            <p>It is completely normal to hold diverse postures (the Warrior executive, the anchoring matriarch, the soft lover) depending on the environment you inhabit. True somatic fatigue occurs when these distinct lines collapse into a state of role enmeshment. When your internal boundaries blur entirely, you carry your defensive operational momentum straight into your intimate and familial spaces until you no longer know where one role ends and the next begins. You aren't broken—your system is simply ready to decouple the roles you play from your true, sovereign identity. Remember: You are the driver, and you hold the keys to this entire vehicle.</p>
        </div>
        
        <h2>💼 Room One: Daily Work Reflection</h2>
        <div class="journal-block">"{st.session_state.client_responses.get('room1_journal', 'No entry captured.')}"</div>
        
        <h2>🧒 Room Two (A): Household & Parenting Dynamics</h2>
        <div class="journal-block">"{st.session_state.client_responses.get('room2_parenting_journal', 'No entry captured.')}"</div>
        
        <h2>🥀 Room Two (B): Intimacy & Sensual Vitality</h2>
        <div class="journal-block">"{st.session_state.client_responses.get('room2_intimacy_journal', 'No entry captured.')}"</div>
        
        <h2>🩺 Room Three: The Physical Body & Tissue Tension</h2>
        <div class="journal-block">"{st.session_state.client_responses.get('room3_journal', 'No entry captured.')}"</div>
        
        <h2>👑 Room Four: Identity & Core Internal Dialogue</h2>
        <div class="journal-block">"{st.session_state.client_responses.get('room4_journal', 'No entry captured.')}"</div>
        
        <footer>
            Compiled safely within The Unlabeled Exploration Container. Anchored in inherent goodness.
        </footer>
    </body>
    </html>
    """

    # Direct premium download button
    st.download_button(
        label="📥 Save a Premium Copy of My Blueprint",
        data=html_blueprint_data,
        file_name=f"{st.session_state.client_responses.get('name','My')}_Somatic_Blueprint.html",
        mime="text/html"
    )

    st.markdown("---")
    
    # INTENT LOGIC FOR BACKGROUND METRICS (PROSE REMOVED TO PREVENT DRYNESS)
    fumes_areas = []
    if "clear boundaries" not in st.session_state.client_responses.get('room1_mirror', '') and "I honor my role at home" not in st.session_state.client_responses.get('room1_mirror', '') and "spaciousness and trust" not in st.session_state.client_responses.get('room1_mirror', ''):
        fumes_areas.append("💼 Work Alignment")
    if "calm authority" not in st.session_state.client_responses.get('room2_parenting_mirror', '') and "functional unit" not in st.session_state.client_responses.get('room2_parenting_mirror', ''):
        fumes_areas.append("🧒 Family Alignment")
    if "healthy part" not in st.session_state.client_responses.get('room2_intimacy_mirror', '') and "deep safety" not in st.session_state.client_responses.get('room2_intimacy_mirror', ''):
        fumes_areas.append("🥀 Intimacy Alignment")
    if "attuned to my body" not in st.session_state.client_responses.get('room3_mirror', ''):
        fumes_areas.append("🩺 Somatic Attunement")
    if "anchored in my inherent worth" not in st.session_state.client_responses.get('room4_mirror', ''):
        fumes_areas.append("👑 Inner Dialogue Calibration")

    # THE SOUL-CENTERED ANCHORING MESSAGE (STANDALONE VALUE)
    st.subheader("🏎️ Reclaiming the Classic Vehicle")
    st.write(
        "Think of a priceless, vintage classic car. If a classic has been left out in the weather, used as a basic workhorse to "
        "haul massive emotional loads for decades, its engine might experience a little lag. But that doesn't mean its worth "
        "has dropped by a single dollar. Its inherent value remains absolute. The tragedy of our world is that we treat our possessions, "
        "our phones, and our careers with continuous maintenance and reverence, yet we treat our own physical bodies and spirits "
        "like an afterthought because we were told that self-preservation is 'selfish.' "
    )
    st.write(
        "Breaking free from that lie requires stepping into a literal garage space—a place where it is completely safe to stop performing, "
        "take the pieces completely apart, empty out the accumulated layers of fear, shame, or unvoiced resentment, and custom-rebuild "
        "your world so you can live in complete alignment with your peace. True connection isn't just about your marriage, your team, or your children. "
        "It is multi-dimensional. It encompasses your relationship with the Divine, your relationship with friendships, and—most importantly—your "
        "relationship with your own soul. You are fully capable of being your own greatest cheerleader."
    )

    st.markdown("---")
    
    # THE PARTNERSHIP INVITATION
    st.subheader("🏛️ The 30-Day Somatic Release Container (An Autonomy Trial)")
    st.write(
        "Most mainstream coaching programs operate on an artificial hierarchy that forces you to become completely dependent on the coach, "
        "demanding heavy, long-term investments before you've even cleared your baseline stress. We reject that approach entirely.\n\n"
        "I am not a savior, and I don't run a generic factory program. I am a master guide who has walked every inch of this pavement—navigating "
        "my own complete career turnarounds, relationship restarts, and deep physical health crises. I know how much it hurts to do it alone, "
        "and I know how much easier the road becomes when someone walks alongside you. This 30-day container is an intentional partnership trial "
        "designed exclusively for **The Release Phase**, guaranteeing you **nearly 4 full hours of live, dedicated 1-to-1 real estate** split purposefully across your month:"
    )
    
    st.markdown("#### 1. The Live Somatic Release Session (90 - 120 Minutes)")
    st.write("We begin with a profound live 1-to-1 container. Think of this as an intentional internal massage for your nervous system. We clear the immediate processing pressure to completely quiet your internal noise, handing you raw, unforced clarity into exactly how your system is currently running.")
    
    st.markdown("#### 2. The 3-Week Independent Trial (Your True Power)")
    st.write("Following your session, you take the wheel entirely yourself. Backed by your bespoke personal recording and daily somatic resources, you will spend just 15 to 30 minutes a day exclusively connecting with your own body and reflections. For three weeks, we deliberately do not speak. This protected space is where your system realizes that you already hold the master key inside you—proving you have the power to protect your own peace.")
    
    st.markdown("#### 3. The Live Week 4 Alignment Check (90 Minutes)")
    st.write("Once your nervous system has settled, we come back together for a second extensive 90-minute live deep-dive session. Armed with the perspective of your independent trial, we will see exactly what your lifestyle requires next. Because every woman is unique, this is where we custom-design your path forward, determining exactly how much support your classic system desires to step into the deeper blocks: **Restore, Rebuild, Ride, and Protect** your ultimate freedom.")
    
    st.markdown("---")
    st.markdown("### 🕊️ Container Logistics & Booking")
    st.write(
        "The complete investment for this foundational 30-day autonomy trial, encompassing both extended live sessions and your bespoke integration assets, is **$750**."
    )
    
    st.markdown("---")
    st.subheader("Choose Your Next Step Below:")
    
    # UPGRADED HIGH-INTEGRITY BUTTONS WITH CANDY'S EXACT TEXT
    if 'submitted' not in st.session_state:
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🕊️ I am ready. Let's do this."):
                try:
                    st.session_state.client_responses['user_intent'] = "READY_TO_BOOK"
                    webhook_url = st.secrets["WEBHOOK_URL"]
                    requests.post(webhook_url, json=st.session_state.client_responses)
                    st.session_state.submitted = "BOOKING"
                    st.rerun()
                except:
                    st.error("Connection link timed out. Please try again.")
                    
        with col2:
            if st.button("🌳 This was great, but I'm not ready to commit yet. Send me some resources."):
                try:
                    st.session_state.client_responses['user_intent'] = "WANTS_RESOURCES_ONLY"
                    webhook_url = st.secrets["WEBHOOK_URL"]
                    requests.post(webhook_url, json=st.session_state.client_responses)
                    st.session_state.submitted = "RESOURCES"
                    st.rerun()
                except:
                    st.error("Connection link timed out. Please try again.")
    else:
        if st.session_state.submitted == "BOOKING":
            st.success("✨ Your unmasked somatic profile has been securely transmitted straight to Candy's private desk! Check your email right now for your calendar invitation to select your session time.")
        else:
            st.success("✨ Your request has been securely logged! Candy's private desk has been notified. Check your email shortly to download your custom somatic resource packet.")
            
        if st.button("Restart Exploration Journey 🔄"):
            st.session_state.room_step = 1
            st.session_state.client_responses = {}
            if 'submitted' in st.session_state: del st.session_state.submitted
            st.rerun()
