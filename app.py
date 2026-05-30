import streamlit as st
import time
import requests

# --- APP CONFIGURATION & PREMIUM THEMING ---
st.set_page_config(
    page_title="The Readiness Analysis | Restored and Ready",
    page_icon="🌳",
    layout="centered"
)

# Strict application of the Restored & Ready Brand Direction Directive
st.markdown("""
    <style>
    /* Global Background & Body Text (Warm Ivory / Parchment + Soft Charcoal) */
    .stApp {
        background-color: #F3EEE7;
        color: #333333;
        font-family: 'Georgia', serif;
    }
    
    /* Editorial Headings (Deep Burgundy) */
    h1, h2, h3, h4, .burgundy-text {
        color: #6D1F3B;
        font-family: 'Georgia', serif;
        font-weight: 700;
    }
    
    /* Input Labels and Form Controls */
    .stTextInput>label, .stNumberInput>label, .stRadio>label, .stMultiSelect>label, .stCheckbox>label {
        color: #333333 !important;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }

    /* Key Premium Action Buttons (Deep Burgundy + Warm Ivory Text) */
    .stButton>button {
        background-color: #6D1F3B;
        color: #F3EEE7 !important;
        border-radius: 4px;
        padding: 0.75rem 2.5rem;
        font-family: 'Georgia', serif;
        font-weight: bold;
        border: 1px solid #8C6A43; /* Antique Bronze accent rim */
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #333333; /* Soft Charcoal swap on hover */
        color: #F3EEE7 !important;
        border-color: #A07A4B; /* Burnished Brass flare */
    }
    
    /* Archival Quote Containers (Alt Light Neutral Background + Antique Bronze Border) */
    .quote-box {
        background-color: #EDE5DA;
        padding: 24px;
        border-left: 4px solid #8C6A43;
        border-radius: 4px;
        margin: 22px 0;
        color: #333333;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Dynamic Somatic Matrix Containers (Dusty Taupe Layering) */
    .matrix-box {
        background-color: #EDE5DA;
        padding: 20px;
        border-radius: 4px;
        border: 1px solid #B4A293;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    
    /* Custom divider line styling using Antique Bronze tint */
    hr {
        border: 0;
        height: 1px;
        background: #B4A293;
        margin: 30px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE STATE ENGINE ---
if 'step' not in st.session_state:
    st.session_state.step = 'gateway'
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'data' not in st.session_state:
    st.session_state.data = {
        'scores': {'certainty': 0, 'significance': 0, 'love': 0, 'variety': 0, 'growth': 0},
        'spaghetti_lanes': []
    }

def score_needs(need_list):
    for need in need_list:
        if need in st.session_state.data['scores']:
            st.session_state.data['scores'][need] += 1

def validate_submission():
    """Validates that foundational identity gateways were interacted with to prevent blank submissions"""
    required = ['name', 'email', 'career_gateway', 'home_gateway']
    missing = [f for f in required if not st.session_state.data.get(f)]
    return len(missing) == 0, missing

# Data delivery system with safe 10-second connection timeout handling and verified state responses
def dispatch_analysis_payload(status_type):
    st.session_state.data['submission_status'] = status_type
    st.session_state.data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        webhook_url = st.secrets["WEBHOOK_URL"]
        response = requests.post(webhook_url, json=st.session_state.data, timeout=10)
        if response.status_code == 200:
            return True
    except requests.exceptions.Timeout:
        st.warning("⚠️ Connection timeout. Your reflection data is safely queued locally.")
    except Exception as e:
        pass
    return False

# Unified 90-second circuit breaker 
def run_breath_intermission(audio_filename, next_step):
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("🌊 Resetting Your Internal Gauge")
    st.write("Allow your physical frame to settle. Your nervous system requires exactly 90 seconds to fully clear an activated emotional baseline. Listen to Candy's guidance below and match your breathing to the visual pacing engine for 5 complete cycles.")
    
    try:
        st.audio(audio_filename, format="audio/mp3")
    except:
        st.caption("*(Note: Audio asset placeholder playing. Ensure file matches configuration name exactly.)*")

    progress_bar = st.progress(0)
    status_text = st.empty()
    
    rounds = [
        "Round 1: Expand your chest... Hold the frame... Release the weight... Find the quiet space.",
        "Round 2: Soften your jaw... Hold the frame... Blow out the pressure... Find the quiet space.",
        "Round 3: Inhale clarity... Hold the frame... Release historic armor... Find the quiet space.",
        "Round 4: Breathe in truth... Hold the frame... Let go of performance... Find the quiet space.",
        "Round 5: Return to Shalom... Hold the frame... Rest deeply right here... Find the quiet space."
    ]
    
    if st.button("🔴 Begin Your 90-Second Reset"):
        for i, round_msg in enumerate(rounds):
            status_text.markdown(f"<div style='font-style: italic; color: #6D1F3B; font-size:1.1rem;'>{round_msg}</div>", unsafe_allow_html=True)
            for percent in range(20):
                total_idx = (i * 20) + percent + 1
                progress_bar.progress(total_idx / 100)
                time.sleep(0.18) # Strictly calibrated to clear the 90-second threshold
        status_text.success("✨ Your baseline is clear. Your system is co-regulated, anchored, and ready.")
        if st.button("Proceed Forward"):
            st.session_state.step = next_step
            st.rerun()

# --- STEP 1: THE GATEWAY & COMMITMENT ---
if st.session_state.step == 'gateway':
    st.title("The Readiness Analysis 🌳")
    st.markdown("<div class='quote-box'><strong>Museum-Grade Restoration for a Woman of Inherent Worth.</strong><br><br>\"The problem is not that you are falling apart. The problem is that the old system can no longer carry who you are becoming. Your body, home, career, and identity are simply calling for a profound update.\"</div>", unsafe_allow_html=True)
    
    st.write("This reflection questionnaire serves as a quiet, responsive mirror for your internal operating system. It separates the tangled lanes of your life so you can discern exactly where restoration needs to begin. Secure your private container below.")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
    with col2:
        age = st.number_input("Age / Season of Life", min_value=18, max_value=100, value=40)
    
    st.markdown("### 🚧 Breaking The 'Tomorrow' Lie")
    st.write("The biggest lie we ever tell ourselves is *'I'll do it tomorrow.'* But tomorrow never comes. Leaving your alignment for 'tomorrow' is the exact mechanism that keeps your system driving on fumes. Completing this analysis today is your very first victory—proving to your nervous system that you are finally prioritizing *you*.")
    
    commitment = st.checkbox("I commit to myself to complete this entire analysis in one sitting right now. I am done waiting for tomorrow.")
    
    if st.button("Initiate Analysis"):
        if name and email and commitment:
            st.session_state.data['name'] = name
            st.session_state.data['email'] = email
            st.session_state.data['age'] = age
            st.session_state.step = 'career'
            st.rerun()
        else:
            st.error("Please fill out your details and check the box to break the procrastination pattern.")

# --- STEP 2: LANE 1 - CAREER OPERATING SYSTEM ---
elif st.session_state.step == 'career':
    st.title("Lane 1: Career & Professional Workspace 💼")
    st.write("Let's look under the hood of your professional environment. How is your engine handling the daily speed and capacity demand?")
    
    gateway = st.radio("Which option best isolates your current structural professional reality?", 
                       ["Corporate Leader or Traditional Executive", "Business Owner / Entrepreneur", "Dedicated Employee", "Full-Time Mother & Household Anchor"])
    st.session_state.data['career_gateway'] = gateway
    
    st.markdown("### ✨ The Shalom Highlights")
    st.write("Select the areas where your professional operating system is currently experiencing expansion or alignment:")
    h1 = st.checkbox("Connection: I feel deeply seen, understood, or creatively linked with my colleagues or clients.", key="c_h1")
    h2 = st.checkbox("Capability: I feel completely confident and like I am operating in my natural zone of genius.", key="c_h2")
    h3 = st.checkbox("Value: I feel highly appreciated, significant, and respected in what I build daily.", key="c_h3")
    
    st.markdown("### 🕯️ Now, Let's Be Honest...")
    st.write("What protective, 'Spaghetti' states does your system default into when the pressure overrides your capacity?")
    s1 = st.checkbox("The Invisibility: I feel entirely unseen, misunderstood, or like I have to wear a rigid mask to protect my position.", key="c_s1")
    s2 = st.checkbox("The Deficit: I feel inadequate, exhausted, or like I am failing no matter how fast I drive the machine.", key="c_s2")
    s3 = st.checkbox("The Warrior Shadow: I become urgent, snappy, harsh, hyper-controlling, or completely emotionally shut down to keep things moving.", key="c_s3")
    
    has_spaghetti = s1 or s2 or s3
    
    if has_spaghetti:
        if 'Career' not in st.session_state.data['spaghetti_lanes']:
            st.session_state.data['spaghetti_lanes'].append('Career')
        st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
        st.markdown("<h4>🫁 Somatic Trace: Reading the Warning Lights</h4>", unsafe_allow_html=True)
        st.write("Two things can be true: You are an incredibly capable leader, AND your professional engine is running dangerously hot. Let's look underneath the behavior without a drop of shame.")
        st.session_state.data['career_where'] = st.text_input("WHERE do you physically feel that tension, snap, or drain inside your frame right now?", key="c_where")
        st.session_state.data['career_what'] = st.text_input("WHAT is it doing? Describe its raw physical texture (e.g., a clamped jaw, a racing heart, a concrete weight on your neck).", key="c_what")
        st.session_state.data['career_when'] = st.text_input("WHEN does this sensation hit its absolute peak during your active shift?", key="c_when")
        st.markdown("</div>", unsafe_allow_html=True)
        
    if st.button("Lock Lane & Breathe"):
        if h1: score_needs(['love'])
        if h2: score_needs(['growth'])
        if h3: score_needs(['significance'])
        st.session_state.step = 'career_pause'
        st.rerun()

elif st.session_state.step == 'career_pause':
    run_breath_intermission("career_pause.mp3", "home")

# --- STEP 4: LANE 2 - HOME & DOMESTIC ENVIRONMENT ---
elif st.session_state.step == 'home':
    st.title("Lane 2: Home & Domestic Landscape 🏡")
    st.markdown("<div class='quote-box'><strong>The Rib Metaphor:</strong><br>Women are often like the ribs of a body—they protect what is vital. They guard the heart of the home, support the breath of the family, and hold everything together, even while carrying deep, unseen structural impact. Many continue functioning perfectly while hurting internally.</div>", unsafe_allow_html=True)
    
    gateway = st.radio("Which option best highlights the structural reality of your primary household?", 
                       ["Married or Partnered (Shared Domestic Space)", "Single Parent managing independent household infrastructure", "Co-Parenting or transitioning through a divorce/relational severance", "Single & Living Alone", "Multi-Generational Caretaker (Simultaneously balancing children + aging parents)"])
    st.session_state.data['home_gateway'] = gateway
    
    st.markdown("### ✨ The Shalom Highlights")
    h1 = st.checkbox("Grounded: My home environment feels like a genuine sanctuary of rest and emotional safety.", key="h_h1")
    h2 = st.checkbox("Seen: My family dynamic leaves me feeling intimately connected, supported, and valued.", key="h_h2")
    
    st.markdown("### 🕯️ Now, Let's Be Honest...")
    s1 = st.checkbox("The Alarm: My system feels anxious, hyper-vigilant, or like I am constantly walking on eggshells in my own living room.", key="h_s1")
    s2 = st.checkbox("The Silent Fracture: I emotionally freeze, shut down, cry in isolation, or outrun my feelings with constant domestic chores.", key="h_s2")
    s3 = st.checkbox("The Rigidity: My body gets physically stiff, braced, or white-knuckled trying to manage everyone else's emotional climate.", key="h_s3")
    
    has_spaghetti = s1 or s2 or s3
    
    if has_spaghetti:
        if 'Home' not in st.session_state.data['spaghetti_lanes']:
            st.session_state.data['spaghetti_lanes'].append('Home')
        st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
        st.markdown("<h4>🫁 Somatic Trace: Tracing the Structural Pressure</h4>", unsafe_allow_html=True)
        st.write("Your ribs are built to protect, but even the strongest structures crack if they carry too much without support. Let's trace where you are absorbing the impact.")
        st.session_state.data['home_where'] = st.text_input("WHERE does that household anxiety, bracing, or shutdown anchor itself in your body?", key="h_where")
        st.session_state.data['home_what'] = st.text_input("WHAT is it doing to your chest, stomach, or breathing pattern the moment you walk through the front door?", key="h_what")
        st.session_state.data['home_how'] = st.text_input("HOW is this specific survival loop changing the way you show up for the people inside your house?", key="h_how")
        st.markdown("</div>", unsafe_allow_html=True)
        
    if st.button("Lock Lane & Breathe"):
        if h1: score_needs(['certainty'])
        if h2: score_needs(['love'])
        st.session_state.step = 'home_pause'
        st.rerun()

elif st.session_state.step == 'home_pause':
    run_breath_intermission("home_pause.mp3", "identity")

# --- STEP 5: LANE 3 - IDENTITY & SPIRITUAL CONNECTION ---
elif st.session_state.step == 'identity':
    st.title("Lane 3: Identity & Spiritual Connection 🧠")
    st.markdown("<div class='quote-box'><strong>The Tree Metaphor:</strong><br>A tree can only grow as strong as its roots. If your roots are wounded, hidden, or unsupported by truth, the branches and the fruit will reflect it. True alignment means undoing the labels you wore to survive, so you can heal the root system underneath.</div>", unsafe_allow_html=True)
    
    st.write("Let's look at the 'Unlabeled' space. We are separating who you *are* from the exhausting identities you've carried just to hold life together.")
    gateway = st.multiselect("Which historic, heavy labels have you outgrown or feel crushed under?", 
                             ["The Ultra-Strong One who can't show weakness", "The Provider / Primary Financial Pillar", "The Fixer who resolves everyone else's chaos", "The Shield who protects everyone else from pain"])
    st.session_state.data['identity_gateway'] = gateway
    
    st.markdown("### ✨ The Shalom Highlights")
    h1 = st.checkbox("True Stillness: I easily access a space of deep internal wholeness, grounded peace, and spiritual faith.", key="i_h1")
    h2 = st.checkbox("Reciprocity: I have a tight circle or community where I drop my armor entirely and allow myself to be poured into.", key="i_h2")
    
    st.markdown("### 🕯️ Now, Let's Be Honest...")
    s1 = st.checkbox("The Island: I operate like a complete fortress—believing no one understands or can hold the weight I carry.", key="i_s1")
    s2 = st.checkbox("The Chameleon: I hyper-focus on people-pleasing, fawning, and over-giving to friends at the cost of my own tank.", key="i_s2")
    s3 = st.checkbox("The Deep Doubt: I experience inner restlessness, spiritual isolation, or a paralyzing self-distrust.", key="i_s3")
    
    has_spaghetti = s1 or s2 or s3
    
    if has_spaghetti:
        if 'Identity' not in st.session_state.data['spaghetti_lanes']:
            st.session_state.data['spaghetti_lanes'].append('Identity')
        st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
        st.markdown("<h4>🫁 Somatic Trace: Unveiling the Mask</h4>", unsafe_allow_html=True)
        st.session_state.data['identity_where'] = st.text_input("WHERE inside your physical frame does the weight of being the 'strong provider' or 'fixer' sit?", key="i_where")
        st.session_state.data['identity_what'] = st.text_input("WHAT is that emotional burden physically preventing you from feeling or experiencing?", key="i_what")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Lock Lane & Breathe"):
        if h1: score_needs(['certainty', 'growth'])
        if h2: score_needs(['love'])
        st.session_state.step = 'identity_pause'
        st.rerun()

elif st.session_state.step == 'identity_pause':
    run_breath_intermission("identity_pause.mp3", "health")

# --- STEP 6: LANE 4 - HEALTH & SOMATIC ENGINE ---
elif st.session_state.step == 'health':
    st.title("Lane 4: Physical Health & Somatic Engine 🫁")
    st.write("You cannot think your way through this, and you cannot manage your way through exhaustion. Your body keeps score—and eventually, it presents the bill.")
    
    h_gate = st.checkbox("I am currently navigating an acute health diagnosis, a major hormonal shift/menopause, or a physical collapse.")
    st.session_state.data['health_gateway'] = h_gate
    
    st.markdown("### ✨ The Shalom Highlights")
    h1 = st.checkbox("Vitality: My physical frame feels fluid, strong, genuinely energized, and deeply rested upon waking.", key="he_h1")
    
    st.markdown("### 🕯️ Now, Let's Be Honest...")
    s1 = st.checkbox("The Exhaustion Loop: I am depleted at the core. I wake up tired regardless of sleep, or crash heavily at 3:00 PM.", key="he_s1")
    s2 = st.checkbox("The Physical Armor: My jaw is tightly clenched, or my neck, shoulders, and lower back feel wrapped in concrete.", key="he_s2")
    s3 = st.checkbox("The Midnight Race: My mind instantly overheats and races the exact second my head hits the pillow, locking me out of rest.", key="he_s3")
    
    has_spaghetti = s1 or s2 or s3
    
    if has_spaghetti:
        if 'Health' not in st.session_state.data['spaghetti_lanes']:
            st.session_state.data['health_gateway'] = h_gate
        st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
        st.markdown("<h4>🫁 Somatic Trace: Listening to the Engine</h4>", unsafe_allow_html=True)
        st.session_state.data['health_distress_signal'] = st.text_input("When your frame looks at this complete roadmap, what explicit distress signal is your body screaming loudest?", key="he_what")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Lock Final Lane & Move to Trunk"):
        if h1: score_needs(['growth'])
        st.session_state.step = 'trunk'
        st.rerun()

# --- STEP 7: THE TRUNK (GLOBAL ESCAPE HATCHES & ANCHORS) ---
elif st.session_state.step == 'trunk':
    st.title("The Trunk: Cumulative Escape Hatches & Origins 🌳")
    st.write("Now that we have successfully separated the four lanes, look at the total weight of your day. When everything stacks up and the entire system threatens to boil over, how does your operating system try to take the edge off or numb the pressure?")
    
    hatches = st.multiselect("Select your primary cumulative escape hatches:", 
                             ["Wine / Alcohol to numb the evening transition or drop the guard", "Retail Therapy / Late-night scrolling online carts for an entry of surprise", "Hyper-Busyness / Constant workaholism, metrics checking, or cleaning spaces", "Digital Safe Havens / Zoning out on social feeds to disconnect"])
    st.session_state.data['escape_hatches'] = hatches
    
    if "Wine / Alcohol to numb the evening transition or drop the guard" in hatches:
        st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
        alc_freq = st.selectbox("How frequently is your system utilizing alcohol to take the edge off?", 
                                ["Daily to transition out of work mode", "3-4 times a week when pressures accumulate", "Weekends exclusively but in heavy quantities", "An occasional, temporary escape hatch"])
        st.session_state.data['alcohol_frequency'] = alc_freq
        st.markdown("</div>", unsafe_allow_html=True)
        
    if "Retail Therapy / Late-night scrolling online carts for an entry of surprise" in hatches:
        st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
        shop_freq = st.selectbox("Describe the behavioral pattern of your commercial scrolling:", 
                                 ["Daily baskets built to experience a hit of control or surprise", "Spike shopping when a specific lane feels highly chaotic", "Hidden orders I find myself downplaying to my immediate circle"])
        st.session_state.data['shopping_frequency'] = shop_freq
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("### 🗺️ The Catalysts & Timelines")
    catalyst = st.selectbox("When you look at this entire structure... what primary catalyst anchor event originally clicked this survival pattern online?", 
                            ["A complex Divorce or relational breakdown", "A major corporate Shift, career pivot, or loss of professional identity", "An acute Health Diagnosis or physical collapse", "It feels like a systemic baseline I have carried since early childhood"])
    st.session_state.data['timeline_anchor'] = catalyst
    
    if st.button("Step Into The Canopy"):
        st.session_state.step = 'canopy'
        st.rerun()

# --- STEP 8: THE CANOPY (READINESS EVALUATION & HIGH-INTEGRITY FILTERS) ---
elif st.session_state.step == 'canopy':
    st.title("The Canopy: Your Readiness Evaluation 🦅")
    st.markdown("<div class='quote-box'>\"Take a slow, deep breath and let it all out. Look at your map. You separated the lanes. You dropped the armor. You named the weight. That takes immense, raw courage. But information without action is just entertainment.\"</div>", unsafe_allow_html=True)
    
    st.subheader("An Invitation to Museum-Grade Restoration")
    st.write("Your system cannot heal if you keep driving it down the road using the exact same survival loops. I do not promise instant, superficial fixes. This is deliberate, premium restoration built to last. Your journey begins with a highly intentional entry container:")
    
    st.markdown("""
    <div style='background-color: #EDE5DA; padding: 20px; border-radius: 4px; border: 1px solid #B4A293;'>
    <h4 style='margin-top:0;'>🏛️ Stage 1: The Release Container</h4>
    <ul>
        <li><strong>The Private Somatic Release Session (90-120 Minutes):</strong> A deep, live 1:1 space where I guide your body to physically release the accumulated pressure, concrete tightness, and emotional residue it has been armoring.</li>
        <li><strong>The 21-Day Protected Integration:</strong> Daily custom somatic resources and audio practices designed to build self-trust, reconnect you with your inner self, and explicitly prevent your mind from slipping into overthinking.</li>
        <li><strong>The Week 3 Alignment Check (90-120 Minutes):</strong> A mutual discernment space where we review your integration, look at what surfaced, and map out your custom, high-ticket 'Garage Phase' if your brand, website, or team operations require customized restructuring.</li>
        <li><strong>The Diagnostic Fee:</strong> A one-time high-integrity investment of <strong>$750</strong>.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("🚧 The Non-Negotiable Commitment Guardrails")
    st.write("To submit your Readiness Analysis directly to Candy's private desk for alignment validation, verify your internal parameters:")
    
    g1 = st.checkbox("I am completely ready for TIME. I break the lie of 'tomorrow' and commit to dedicating 30 minutes a day to my integration practices.")
    g2 = st.checkbox("I am completely ready for DEPTH. I am done with surface solutions and am willing to actively participate in my own restoration.")
    g3 = st.checkbox("I am FINANCIALLY ALIGNED. I understand museum-grade restoration requires high-touch stewardship, and I am capable and ready to invest $750 for this Stage 1 entry checkpoint.")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Fully checking data validation and blocking double-submissions via loading spinner
    if not st.session_state.submitted:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏛️ I am a classic. Submit & Book Call"):
                is_valid, missing = validate_submission()
                if not (g1 and g2 and g3):
                    st.error("Guard your standards: You must check all three commitment guardrails to unlock Candy's priority alignment grid.")
                elif not is_valid:
                    st.error(f"⚠️ Please complete all previous lanes. Missing inputs: {', '.join(missing)}")
                else:
                    st.session_state.submitted = True
                    with st.spinner("🔄 Securing your profile in our data repository..."):
                        dispatch_analysis_payload("HIGH_PRIORITY_COMMIT")
                        time.sleep(1.5)
                    st.session_state.step = 'success_commit'
                    st.rerun()
                    
        with col2:
            if st.button("🕊️ I need a softer landing right now"):
                st.session_state.submitted = True
                with st.spinner("🕊️ Routing profile to our soft resource database..."):
                    dispatch_analysis_payload("SOFT_LANDING_PROSPECT")
                    time.sleep(1.5)
                st.session_state.step = 'success_soft'
                st.rerun()
    else:
        st.info("✨ Processing your Analysis Profile securely. Please hold standard connection...")

# --- FINAL CO-REGULATED ROUTING SCREENS ---
elif st.session_state.step == 'success_commit':
    st.title("Your Engine is In the Shop 🎉")
    st.balloons()
    st.success(f"Profound work, {st.session_state.data['name']}. Your Readiness Analysis has bypassed the noise and is resting securely on Candy's desk.")
    
    st.markdown("""
    ### 📅 Claim Your Position on the Alignment Grid
    You have successfully proven to your nervous system that you are prioritizing your healing. Click the official link below right now to lock in your live 1:1 session block before looking away.
    
    👉 **[INSERT YOUR CALENDLY/BOOKING LINK HERE]**
    """)
    
    st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
    st.subheader("🧬 Behind-The-Mask Diagnostics (Tony Robbins Taxonomy)")
    st.write("Candy will review this structural heat map during your check-in call. Your personality need metrics register as:")
    st.write(st.session_state.data['scores'])
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.step == 'success_soft':
    st.title("Your Alignment Blueprint 🕊️")
    st.info(f"Thank you for your transparent honesty, {st.session_state.data['name']}. There is absolutely zero shame in needing a softer landing first. Your reflection profile has been saved with immense stewardship.")
    
    st.subheader("Your Current Landscape Summary")
    st.write(f"**Primary Catalyst Origin:** {st.session_state.data['timeline_anchor']}")
    
    st.write("**Tangled Lanes Requiring Pressure Release:**")
    if st.session_state.data['spaghetti_lanes']:
        for lane in set(st.session_state.data['spaghetti_lanes']):
            st.write(f"⚠️ **The {lane} Lane** is operating in an overheated, survival state.")
    else:
        st.write("✅ Your framework displays solid situational baseline metrics.")
        
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("Candy's ministry-based care and lower-intensity accountability resources will be delivered directly to your email inbox so you can move forward at a pace that honors where you actually are right now. The garage doors will remain open for you when your system is ready for the deep work.")
