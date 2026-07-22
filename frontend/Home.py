import streamlit as st
import base64
from pathlib import Path

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# Base Directory
# -------------------------------------------------

BASE_DIR = Path(__file__).parent

# -------------------------------------------------
# Load CSS
# -------------------------------------------------

def load_css():
    css_file = BASE_DIR / "styles" / "home.css"

    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------------------------------
# Load Background Image
# -------------------------------------------------

image_path = BASE_DIR / "images" / "home_page.jpg"

with open(image_path, "rb") as image:
    encoded = base64.b64encode(image.read()).decode()
# -------------------------------------------------
# Hero Background
# -------------------------------------------------

st.markdown(
f"""
<div class="hero-container"
style="background-image:
linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.55)),
url('data:image/jpeg;base64,{encoded}');">

<div class="navbar">

<div class="logo">
🌾 Crop Yield Prediction
</div>

<div class="menu">
    <a href="/" target="_self">Home</a>
    <a href="/Predict" target="_self">Predict</a>
</div>

</div>

<div class="hero-content">
    <h1>AI-Powered Crop Yield Prediction</h1>
    <h2>Harnessing Data & Machine Learning</h2>
    <p>
    Predict agricultural crop yields using historical
    rainfall, temperature and pesticide information
    through Machine Learning.
    </p>
</div>

</div>

""",
unsafe_allow_html=True
)

# -------------------------------------------------
# Button
# -------------------------------------------------

left, center, right = st.columns([3,2,3])

with center:

    if st.button("Start Prediction", use_container_width=True):
        st.switch_page("pages/1_Predict.py")

# -------------------------------------------------
# Scroll Indicator
# -------------------------------------------------

st.markdown("""

<div class="scroll">
↓
<br>
Scroll Down
</div>

""", unsafe_allow_html=True)

# -------------------------------------------------
# Feature Section
# -------------------------------------------------

st.markdown("""

<section class="section">

<h2 class="section-title">
Why Choose Our Platform?
</h2>

<div class="feature-container">
<div class="feature-card">
<div class="icon">🤖</div>

<h3>AI Powered</h3>

<p>
Built using a trained Random Forest Regression model to
predict crop yield accurately.
</p>

</div>
<div class="feature-card">

<div class="icon">⚡</div>

<h3>Fast Prediction</h3>

<p>

Instant predictions using a FastAPI backend and a
responsive Streamlit interface.

</p>

</div>

<div class="feature-card">

<div class="icon">🌍</div>

<h3>Global Dataset</h3>

<p>

Supports crop yield prediction across more than
100 countries.

</p>

</div>

</div>

</section>

""", unsafe_allow_html=True)


# -------------------------------------------------
# Statistics
# -------------------------------------------------

st.markdown("""

<section class="stats-section">

<h2 class="section-title">

Project Statistics

</h2>

<div class="stats-container">

<div class="stat-card">

<h1>101</h1>

<p>Countries</p>

</div>

<div class="stat-card">

<h1>10</h1>

<p>Crop Types</p>

</div>

<div class="stat-card">

<h1 class="rf">RF</h1>

<p>Random Forest Model</p>

</div>

</div>

</section>

""", unsafe_allow_html=True)

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("""

<div class="footer">

<h3>🌾 AI Powered Crop Yield Prediction</h3>

<p>
Developed by <b>Umesh</b>
</p>

<p>
Built with
</p>
                        
<p>
Python • Streamlit • FastAPI • Scikit-learn
</p>

<p>
© 2026 All Rights Reserved
</p>

</div>

""", unsafe_allow_html=True)
