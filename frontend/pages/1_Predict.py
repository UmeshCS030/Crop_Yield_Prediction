#---import libraries
import streamlit as st
import requests

from pathlib import Path

#---Configure the page
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# ---------- Load CSS ----------
css_file = Path(__file__).parent.parent / "styles" / "predict.css"

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown("""
<div class="page-header">

<div class="page-title">
        🌾 Crop Yield Prediction
</div>

<div class="page-subtitle">
    Enter the required information below.
</div>

</div>
""", unsafe_allow_html=True)


#----Create the input Form (by organizing the inputs into two columns)
col1, col2 = st.columns(2)

with col1:
    AREAS = [
    'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia',
    'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Belarus', 'Belgium', 'Botswana', 'Brazil',
    'Bulgaria', 'Burkina Faso', 'Burundi', 'Cameroon', 'Canada',
    'Central African Republic', 'Chile', 'Colombia', 'Croatia',
    'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
    'Eritrea', 'Estonia', 'Finland', 'France', 'Germany', 'Ghana',
    'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Honduras',
    'Hungary', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Italy',
    'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Latvia', 'Lebanon',
    'Lesotho', 'Libya', 'Lithuania', 'Madagascar', 'Malawi',
    'Malaysia', 'Mali', 'Mauritania', 'Mauritius', 'Mexico',
    'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal',
    'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Norway',
    'Pakistan', 'Papua New Guinea', 'Peru', 'Poland', 'Portugal',
    'Qatar', 'Romania', 'Rwanda', 'Saudi Arabia', 'Senegal',
    'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
    'Suriname', 'Sweden', 'Switzerland', 'Tajikistan', 'Thailand',
    'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Kingdom',
    'Uruguay', 'Zambia', 'Zimbabwe'
    ]

    CROPS = [
    'Maize',
    'Potatoes',
    'Rice, paddy',
    'Sorghum',
    'Soybeans',
    'Wheat',
    'Cassava',
    'Sweet potatoes',
    'Plantains and others',
    'Yams'
    ]

    area = st.selectbox(
        "🌍 Select Area",
        AREAS,
        index=AREAS.index("Sri Lanka")
    )

    item = st.selectbox(
        "🌾 Select Crop",
        CROPS,
        index=CROPS.index("Rice, paddy")
    )


    year = st.number_input(
        "📅 Year",
        min_value=1900,
        max_value=2100,
        value=2025
    )

with col2:

    rainfall = st.number_input(
        "🌧️ Average Rainfall (mm/year)",
        value=1800.0
    )

    pesticides = st.number_input(
        "🧪 Pesticides (tonnes)",
        value=250.0
    )

    temperature = st.number_input(
        "🌡️ Average Temperature (°C)",
        value=27.5
    )


#---Predict button
predict = st.button(
    "Predict Crop Yield",
    use_container_width=True
)

#---Create the JSON
if predict:

    data = {

        "Area": area,

        "Item": item,

        "Year": year,

        "average_rain_fall_mm_per_year": rainfall,

        "pesticides_tonnes": pesticides,

        "avg_temp": temperature

    }


    #---Send the request
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )


    #---Read the prediction
    prediction = response.json()


    #---Display Prediction
    st.markdown(
    f"""
    <div class="result-card">
    <div class="result-title">
        Predicted Crop Yield
    </div>

    <div class="result-value">
        {prediction['predicted_yield']:.2f}
    </div>

    <div class="result-unit">
        hectograms per hectare (hg/ha)
    </div>

    <div class="result-note">
        Prediction generated successfully using the trained Machine Learning model.
    </div>

    </div>
    """,
    unsafe_allow_html=True,
    )

