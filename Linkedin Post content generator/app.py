"""
AI LinkedIn Post Generator — Streamlit App
Schema aligned exactly with prompt_builder.py and user_inputs.py
"""

import streamlit as st
import re
from datetime import datetime

# ─────────────────────────────────────────────
# Page Config  (must be first Streamlit call)
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="LinkedIn Post Generator · AI",
    page_icon="🪄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap');

:root {
    --bg:           #0d0f14;
    --surface:      #141720;
    --surface-2:    #1c2030;
    --border:       #272c3d;
    --accent:       #4f8ef7;
    --accent-glow:  rgba(79,142,247,.18);
    --accent-2:     #a78bfa;
    --text:         #e8eaf2;
    --text-muted:   #7b82a0;
    --text-faint:   #3e4460;
    --font-display: 'DM Serif Display', serif;
    --font-body:    'DM Sans', sans-serif;
    --radius:       12px;
    --radius-lg:    20px;
    --shadow:       0 4px 24px rgba(0,0,0,.4);
    --shadow-glow:  0 0 40px rgba(79,142,247,.12);
}

html, body, [class*="css"] {
    font-family: var(--font-body);
    background-color: var(--bg);
    color: var(--text);
}

.stApp { background: var(--bg); }
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border);
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent;
}
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 980px; }

/* ── Sidebar ── */
.sidebar-logo {
    text-align: center;
    padding: 1.5rem 0 1rem;
}
.sidebar-logo .logo-mark {
    width: 56px; height: 56px;
    background: linear-gradient(135deg, var(--accent), var(--accent-2));
    border-radius: 16px;
    display: inline-flex; align-items: center; justify-content: center;
    font-size: 1.6rem;
    margin-bottom: .75rem;
    box-shadow: 0 8px 24px rgba(79,142,247,.3);
}
.sidebar-logo h2 {
    font-family: var(--font-display);
    font-size: 1.2rem; color: var(--text); margin: 0;
}
.sidebar-logo p { font-size: .78rem; color: var(--text-muted); margin: .3rem 0 0; }
.sidebar-divider { border: none; border-top: 1px solid var(--border); margin: 1rem 0; }
.sidebar-section h4 {
    font-size: .7rem; letter-spacing: .1em; text-transform: uppercase;
    color: var(--text-faint); margin: 0 0 .5rem;
}
.sidebar-section p, .sidebar-section li {
    font-size: .82rem; color: var(--text-muted); line-height: 1.6;
}
.sidebar-section ul { padding-left: 1.1rem; margin: 0; }
.sidebar-footer {
    text-align: center; font-size: .72rem;
    color: var(--text-faint); padding: 1rem 0;
}
.sidebar-footer span { color: var(--accent); }

/* ── Hero ── */
.hero {
    text-align: center; padding: 2.5rem 1rem 2rem; position: relative;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 70% 60% at 50% 0%, rgba(79,142,247,.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    background: var(--accent-glow);
    border: 1px solid rgba(79,142,247,.35);
    color: var(--accent);
    font-size: .72rem; font-weight: 600; letter-spacing: .08em;
    text-transform: uppercase; padding: .3rem .9rem;
    border-radius: 999px; margin-bottom: 1.1rem;
}
.hero h1 {
    font-family: var(--font-display);
    font-size: clamp(2rem, 4vw, 3rem); font-weight: 400;
    color: var(--text); margin: 0 0 .7rem; line-height: 1.15;
}
.hero h1 em { color: var(--accent); font-style: normal; }
.hero p {
    font-size: 1.05rem; color: var(--text-muted);
    max-width: 540px; margin: 0 auto; line-height: 1.65;
}

/* ── Metrics ── */
.metrics-row {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: .75rem; margin-bottom: 1.5rem;
}
.metric-card {
    background: var(--surface-2); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 1rem 1.25rem; text-align: center;
}
.metric-value {
    font-family: var(--font-display); font-size: 1.8rem;
    color: var(--accent); line-height: 1;
}
.metric-label {
    font-size: .73rem; color: var(--text-muted);
    margin-top: .3rem; text-transform: uppercase; letter-spacing: .07em;
}

/* ── Card ── */
.card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: var(--radius-lg); padding: 1.75rem 2rem;
    margin-bottom: 1.5rem; box-shadow: var(--shadow);
}


.card-title {
    font-family: var(--font-display);
    font-size: 2.15rem;
    font-weight: 400;
    color: #ffffff;
    letter-spacing: -0.03em;
    line-height: 1.15;
    margin-bottom: 1.4rem;
    text-transform: none;

    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.card-title::before {
    content: "";
    width: 5px;
    height: 32px;
    border-radius: 999px;
    background: linear-gradient(
        180deg,
        var(--accent),
        var(--accent-2)
    );
    box-shadow: 0 0 12px rgba(79,142,247,.25);
}


/* ── Debug box ── */
.debug-box {
    background: #111827; border: 1px solid #374151;
    border-radius: var(--radius); padding: 1rem 1.25rem;
    font-family: 'Courier New', monospace; font-size: .78rem;
    color: #6ee7b7; line-height: 1.7; margin-bottom: 1rem;
}

/* ── Form elements ── */
.stTextInput > label, .stTextArea > label,
.stSelectbox > label, .stSlider > label, .stCheckbox > label {
    font-size: .82rem !important; font-weight: 500 !important;
    color: var(--text-muted) !important; letter-spacing: .02em !important;
}
.stTextInput input, .stTextArea textarea {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    color: var(--text) !important;
    font-family: var(--font-body) !important;
    font-size: .9rem !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px var(--accent-glow) !important;
}
div[data-baseweb="select"] > div {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    color: var(--text) !important;
}
div[data-baseweb="select"] span { color: var(--text) !important; }
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: var(--accent) !important; border-color: var(--accent) !important;
}

/* ── Generate button ── */
.stButton > button {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%) !important;
    color: #fff !important; border: none !important;
    border-radius: var(--radius) !important;
    font-family: var(--font-body) !important; font-size: .92rem !important;
    font-weight: 600 !important; padding: .7rem 2rem !important;
    letter-spacing: .03em !important;
    transition: opacity .2s, transform .15s, box-shadow .2s !important;
    box-shadow: 0 4px 20px rgba(79,142,247,.35) !important;
    width: 100%;
}
.stButton > button:hover {
    opacity: .92 !important; transform: translateY(-1px) !important;
    box-shadow: 0 8px 28px rgba(79,142,247,.5) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Post output ── */
.post-output {
    background: var(--surface-2);
    border: 1px solid var(--border); border-left: 3px solid var(--accent);
    border-radius: var(--radius); padding: 1.5rem 1.75rem;
    font-size: .93rem; line-height: 1.8; white-space: pre-wrap;
    color: var(--text); font-family: var(--font-body);
    box-shadow: var(--shadow-glow); margin-bottom: 1rem;
}

/* ── History ── */
.history-meta { font-size: .72rem; color: var(--text-faint); margin-top: .2rem; }

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--accent), var(--accent-2)) !important;
    border-radius: 999px !important;
}
details {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}
summary { color: var(--text) !important; font-size: .88rem !important; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Constants — copied exactly from user_inputs.py
# so both CLI and Streamlit share the same values
# ─────────────────────────────────────────────
VALID_TONES = [
    "Professional",
    "Inspirational",
    "Humorous",
    "Funny",
    "Angry",
    "Sad",
]

VALID_LENGTHS = [
    "Short (100–150 words)",
    "Medium (200–300 words)",
    "Long (400–500 words)",
]

VALID_FRAMEWORKS = [
    "AIDA (Attention, Interest, Desire, Action)",
    "PAS (Problem, Agitate, Solution)",
    "Storytelling",
    "Listicle",
    "How-to / Tips",
    "None",
]

# ─────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────
def init_session():
    defaults = {
        "generated_post":   None,
        "history":          [],
        "last_inputs":      {},
        "generation_count": 0,
        "show_debug":       False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────
def validate_inputs(inputs: dict) -> list[str]:
    """
    Returns a list of error strings.
    Empty list means inputs are valid.
    Checks every key that prompt_builder.py accesses:
        inputs['topic'], inputs['tone'], inputs['audience'],
        inputs['length'], inputs['framework']
    """
    errors = []
    required = {
        "topic":     "Topic cannot be empty.",
        "tone":      "Please select a tone.",
        "audience":  "Target audience cannot be empty.",
        "length":    "Please select a post length.",
        "framework": "Please select a copywriting framework.",
    }
    for key, msg in required.items():
        val = inputs.get(key, "").strip()
        if not val:
            errors.append(msg)
    return errors


def debug_log(inputs: dict) -> str:
    """Build a debug string showing the exact keys being sent to generate_post()."""
    lines = ["── inputs dict sent to generate_post() ──"]
    for k, v in inputs.items():
        lines.append(f"  {k!r:20} → {v!r}")
    return "\n".join(lines)


def word_count(text: str) -> int:
    return len(text.split())


def char_count(text: str) -> int:
    return len(text)


def make_filename(topic: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9]", "_", topic.strip())
    return f"LINKDIN_POST_{safe}.txt"

# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-mark">🪄</div>
        <h2>PostCraft AI</h2>
        <p>LinkedIn Content Generator</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-section">
        <h4>📖 How to use</h4>
        <ul>
            <li>Enter your post topic</li>
            <li>Set target audience, tone &amp; framework</li>
            <li>Choose post length</li>
            <li>Hit <strong>Generate</strong></li>
            <li>Copy or download your post</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-section">
        <h4>📐 Frameworks</h4>
        <ul>
            <li><strong>AIDA</strong> — Attention → Interest → Desire → Action</li>
            <li><strong>PAS</strong> — Problem → Agitate → Solution</li>
            <li><strong>Storytelling</strong> — Narrative arc</li>
            <li><strong>Listicle</strong> — Numbered tips</li>
            <li><strong>How-to</strong> — Step-by-step guide</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    # Debug toggle
    st.session_state.show_debug = st.toggle(
        "🛠️ Show debug info",
        value=st.session_state.show_debug,
        help="Shows the exact inputs dict passed to generate_post() — useful for diagnosing KeyErrors.",
    )

    st.markdown("""
    <div class="sidebar-footer">
        Built with ❤️ using; Gemini<br>
        © 2026 PostCraft
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Hero
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Powered by Gemini AI</div>
    <h1>🪄 AI <em>LinkedIn</em> Post Generator</h1>
    <p>Craft scroll-stopping LinkedIn content in seconds.
    Pick your framework, tone, and topic — let AI do the heavy lifting.</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Metrics Row
# ─────────────────────────────────────────────
last_wc = word_count(st.session_state.generated_post) if st.session_state.generated_post else 0
st.markdown(f"""
<div class="metrics-row">
    <div class="metric-card">
        <div class="metric-value">{st.session_state.generation_count}</div>
        <div class="metric-label">Posts Generated</div>
    </div>
    <div class="metric-card">
        <div class="metric-value">{len(st.session_state.history)}</div>
        <div class="metric-label">In History</div>
    </div>
    <div class="metric-card">
        <div class="metric-value">{last_wc}</div>
        <div class="metric-label">Last Word Count</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Input Form
# ─────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">📝 Configure your post</div>', unsafe_allow_html=True)

# Row 1 — Topic + Audience
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    topic = st.text_input(
        "Post Topic *",
        placeholder="e.g. Why consistency beats talent in tech careers",
        help="The central idea or theme of your LinkedIn post.",
    )

with col2:
    # Free-text audience — matches get_target_audience() which is also free text
    audience = st.text_input(
        "Target Audience *",
        placeholder="e.g. Software developers, Founders…",
        help="Who should this post speak to?",
    )

# Row 2 — Tone + Framework
col3, col4 = st.columns(2, gap="large")

with col3:
    # Options match VALID_TONES in user_inputs.py exactly
    tone = st.selectbox(
        "Tone *",
        VALID_TONES,
        index=0,
        help="Matches the tones available in the CLI version.",
    )

with col4:
    # Options match VALID_FRAMEWORKS in user_inputs.py exactly
    framework = st.selectbox(
        "Copywriting Framework *",
        VALID_FRAMEWORKS,
        index=0,
        help="The structural framework prompt_builder.py uses to shape the post.",
    )

# Row 3 — Length
# Options match VALID_LENGTHS in user_inputs.py exactly
length = st.selectbox(
    "Post Length *",
    VALID_LENGTHS,
    index=1,
    help="Matches the length options available in the CLI version.",
)

# Row 4 — Additional context (UI-only bonus; not in CLI but doesn't break it)
additional_context = st.text_area(
    "Additional Context (optional)",
    placeholder="Any specific stats, personal anecdotes, or points to include…",
    height=90,
)

st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Generate Button
# ─────────────────────────────────────────────
generate_clicked = st.button("✨ Generate LinkedIn Post", key="generate_btn")

# ─────────────────────────────────────────────
# Generation Logic
# ─────────────────────────────────────────────
if generate_clicked:

    # ── Build inputs dict — keys match prompt_builder.py EXACTLY ──
    # prompt_builder.py reads:
    #   inputs['topic']     → topic
    #   inputs['tone']      → tone
    #   inputs['audience']  → target_audience in template
    #   inputs['length']    → post_length in template
    #   inputs['framework'] → framework in template
    inputs = {
        "topic":              topic.strip(),
        "tone":               tone,
        "audience":           audience.strip(),
        "length":             length,
        "framework":          framework,
        # additional_context is passed along but prompt_builder.py
        # safely ignores unknown keys — it only calls .format() with
        # the five keys above.
        "additional_context": additional_context.strip(),
    }

    # ── Debug view ──
    if st.session_state.show_debug:
        st.markdown(
            f'<div class="debug-box">{debug_log(inputs)}</div>',
            unsafe_allow_html=True,
        )

    # ── Validate ──
    errors = validate_inputs(inputs)
    if errors:
        for err in errors:
            st.error(f"⚠️ {err}")
        st.stop()

    # ── Load model ──
    progress = st.progress(0, text="Initialising Gemini model…")
    try:
        from config import get_model
        model = get_model()
        progress.progress(30, text="Model loaded ✓  •  Building prompt…")
    except Exception as e:
        progress.empty()
        st.error(f"❌ Failed to load model: {e}")
        st.stop()

    # ── Generate ──
    try:
        from prompt_builder import generate_post
        progress.progress(55, text="Generating your post…")

        with st.spinner("Writing your LinkedIn post…"):
            post = generate_post(model, inputs)

        progress.progress(100, text="Done ✓")
        progress.empty()

        # Persist to session
        st.session_state.generated_post = post
        st.session_state.generation_count += 1
        st.session_state.last_inputs = inputs
        st.session_state.history.insert(0, {
            "topic":     inputs["topic"],
            "tone":      inputs["tone"],
            "audience":  inputs["audience"],
            "framework": inputs["framework"],
            "length":    inputs["length"],
            "post":      post,
            "timestamp": datetime.now().strftime("%H:%M · %d %b"),
        })

        st.success("🎉 Post generated successfully!")
        st.rerun()

    except KeyError as e:
        progress.empty()
        st.error(
            f"❌ Generation failed — missing key in inputs dict: {e}\n\n"
            f"Enable **🛠️ Show debug info** in the sidebar to inspect what was sent."
        )
        st.stop()

    except Exception as e:
        progress.empty()
        st.error(f"❌ Generation failed: {e}")
        st.stop()

# ─────────────────────────────────────────────
# Output Section
# ─────────────────────────────────────────────
if st.session_state.generated_post:
    post_text = st.session_state.generated_post

    st.markdown('<div class="card"><div class="card-title">📄 Generated Post</div>', unsafe_allow_html=True)

    with st.expander("👁️ Preview post", expanded=True):
        st.markdown(
            f'<div class="post-output">{post_text}</div>',
            unsafe_allow_html=True,
        )

    wc = word_count(post_text)
    cc = char_count(post_text)
    lc = post_text.count("\n") + 1

    st.markdown(f"""
    <div style="display:flex;gap:1.5rem;margin-bottom:1rem;font-size:.82rem;color:var(--text-muted);">
        <span>📝 <strong style="color:var(--text)">{wc}</strong> words</span>
        <span>🔤 <strong style="color:var(--text)">{cc}</strong> characters</span>
        <span>📏 <strong style="color:var(--text)">{lc}</strong> lines</span>
    </div>
    """, unsafe_allow_html=True)

    btn1, btn2, btn3 = st.columns([1, 1, 2], gap="small")

    with btn1:
        fname = make_filename(st.session_state.last_inputs.get("topic", "post"))
        st.download_button(
            label="⬇️ Download TXT",
            data=post_text,
            file_name=fname,
            mime="text/plain",
            use_container_width=True,
        )

    with btn2:
        escaped = post_text.replace("`", "\\`").replace("$", "\\$")
        copy_js = f"""
        <script>
        function copyPost(){{
            navigator.clipboard.writeText(`{escaped}`)
            .then(()=>{{const b=document.getElementById('cpbtn');b.innerText='✅ Copied!';setTimeout(()=>b.innerText='📋 Copy',1800);}})
            .catch(()=>alert('Copy failed — select and copy manually.'));
        }}
        </script>
        <button id="cpbtn" onclick="copyPost()"
            style="width:100%;padding:.5rem 1rem;background:#1c2030;border:1px solid #272c3d;
                   border-radius:12px;color:#e8eaf2;font-family:'DM Sans',sans-serif;
                   font-size:.82rem;cursor:pointer;">
            📋 Copy
        </button>
        """
        st.components.v1.html(copy_js, height=44)

    with btn3:
        if st.button("🔄 Regenerate", key="regen_btn", use_container_width=True):
            saved = st.session_state.last_inputs
            if saved:
                try:
                    from config import get_model
                    from prompt_builder import generate_post
                    with st.spinner("Regenerating…"):
                        new_post = generate_post(get_model(), saved)
                    st.session_state.generated_post = new_post
                    st.session_state.generation_count += 1
                    st.session_state.history.insert(0, {
                        **saved,
                        "post":      new_post,
                        "timestamp": datetime.now().strftime("%H:%M · %d %b"),
                    })
                    st.success("Post regenerated!")
                    st.rerun()
                except KeyError as e:
                    st.error(f"❌ Missing key during regeneration: {e}")
                except Exception as e:
                    st.error(f"❌ Regeneration failed: {e}")

    st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Post History
# ─────────────────────────────────────────────
if st.session_state.history:
    st.markdown('<div class="card"><div class="card-title">🕑 Session History</div>', unsafe_allow_html=True)

    for i, item in enumerate(st.session_state.history[:5]):
        with st.expander(f"📌 {item['topic']}  ·  {item['timestamp']}"):
            st.markdown(
                f'<div class="post-output" style="font-size:.85rem;">{item["post"]}</div>',
                unsafe_allow_html=True,
            )
            st.caption(
                f"Tone: {item.get('tone','—')}  ·  "
                f"Audience: {item.get('audience','—')}  ·  "
                f"Framework: {item.get('framework','—')}  ·  "
                f"Length: {item.get('length','—')}"
            )
            if st.button("↩️ Restore this post", key=f"restore_{i}"):
                st.session_state.generated_post = item["post"]
                st.rerun()

    if st.button("🗑️ Clear History", key="clear_hist"):
        st.session_state.history = []
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)