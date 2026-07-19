import streamlit as st


#Global CSS

def set_custom_css():

    st.markdown("""
    <style>

    .main{
        padding-top:2rem;
        padding-left:3rem;
        padding-right:3rem;
        padding-bottom:2rem;
        background-color:#F8FAFC;
    }

    .block-container{
        padding-top:2rem;
    }

    h1{
        color:#0F172A;
        text-align:center;
        font-weight:700;
    }

    h2,h3,h4{
        color:#1E293B;
    }

    p{
        color:#000;
        font-size:19px;
        font-weight: 200
    }

    div[data-testid="stNumberInput"]{
        background:white;
        border-radius:12px;
        padding:10px;
        border:1px solid #E2E8F0;
    }

    div[data-testid="stSlider"]{
        background:white;
        border-radius:12px;
        padding:10px;
        border:1px solid #E2E8F0;
    }
    div[data-testid="stExpander"]{

    border:1px solid #E2E8F0 !important;

    border-radius:18px !important;

    overflow:hidden;

    box-shadow:0 8px 24px rgba(15,23,42,.06);

    background:white;

}

div[data-testid="stExpander"] details summary{

    background:#F8FAFC;

    padding:18px;

    font-size:18px;

    font-weight:600;

    color:#1E293B;

}

div[data-testid="stExpander"] details summary:hover{

    background:#F1F5F9;

}
    
    /* Avoid forcing every Streamlit button to full width */
    div[data-testid="stButton"] > button{
        width:auto;
        max-width:100%;
        height:55px;
        border:none;
        border-radius:12px;
        background:#2563EB;
        color:white;
        font-size:18px;
        font-weight:600;
        transition:0.3s;
    }

    div[data-testid="stButton"] > button:hover{
        background:#1D4ED8;
        color:white;
    }

    /* Ensure button text is always visible */
    div[data-testid="stButton"] > button *{
        color:#FFFFFF !important;
    }

    .prediction-card{

        background:white;
        padding:25px;

        border-radius:15px;

        border-left:8px solid #2563EB;
        border-top:8px solid #2563EB;


        box-shadow:0px 4px 12px rgba(0,0,0,0.08);

        margin-top:15px;

        margin-bottom:20px;
        max-width:720px;
        margin-left:auto;
        margin-right:auto;


    }

    


    .prediction-title{

        color:#64748B;

        font-size:18px;

        font-weight:600;

    }

    .prediction-segment{

        color:#2563EB;

        font-size:34px;

        font-weight:700;

    }

    .section-card{

        background:white;

        padding:22px;

        border-radius:15px;

        box-shadow:0px 4px 10px rgba(0,0,0,0.06);

        margin-top:15px;

        margin-bottom:20px;

    }

   

    hr{
        margin-top:30px;
        margin-bottom:30px;
    }

    </style>
    """, unsafe_allow_html=True)


#Hero Section

#Hero Section

def hero_section():
    # Bilkul simple HTML
    st.markdown(
        """
        <div style="text-align:center; padding:35px 20px; background:linear-gradient(135deg,#2563EB,#1D4ED8); border-radius:18px;">
            <h1 style="color:white; font-size:42px;">🛍️ AI Customer Segmentation Dashboard</h1>
            <p style="color:#E2E8F0; font-size:20px;">Intelligent Customer Segmentation using Machine Learning</p>
            <p style="color:#F8FAFC; font-size:18px;">Analyze customer purchasing behavior using K-Means clustering</p>
        </div>
        """,
        unsafe_allow_html=True
    )


#Section Header

def section_header(title):

    st.subheader(title)


#Prediction Card

def prediction_card(segment):

    st.markdown(

        f"""

        <div class="prediction-card">

        <div class="prediction-title">

        🎯 Prediction Result

        </div>

        <br>

        <div class="prediction-segment">

        {segment}

        </div>

        </div>

        """,

        unsafe_allow_html=True

    )


#Info Card

def info_card(title, content):

    st.markdown(

        f"""

        <div class="section-card">

        <h4>{title}</h4>

        <p>{content}</p>

        </div>

        """,

        unsafe_allow_html=True

    )


#Bullet Section

def bullet_section(title, items):

    st.markdown(f"### {title}")

    for item in items:

        st.markdown(f"✅ {item}")


#Business Recommendation

def recommendation_card(text):

    st.info(text)


#Footer

def footer():

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(

        """

        <div class="footer">

        AI Customer Segmentation System

        <br>

        Developed using Python • Scikit-Learn • Streamlit

        </div>

        """,

        unsafe_allow_html=True

    )