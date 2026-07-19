import ui_components
print("UI Components imported successfully")
print(dir(ui_components))  # Ye dekho ke hero_section available hai ya nahi
import streamlit as st

from ui_components import (
    set_custom_css,
    hero_section,
    section_header,
    prediction_card,
    bullet_section,
    recommendation_card,
    
)

from utils import (
    predict_cluster,
    cluster_names,
    segment_details,
    plot_customer_clusters
)
st.set_page_config(
    page_title="AI Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)

set_custom_css()

hero_section()

st.divider()
section_header("📥 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70,
        value=30,
        step=1
    )

with col2:
    income = st.number_input(
        "Annual Income (k$)",
        min_value=15,
        max_value=137,
        value=60,
        step=1
    )

with col3:
    spending = st.slider(
        "Spending Score",
        min_value=1,
        max_value=100,
        value=50
    )

st.write("")
# Centered predict button (with fixed width)
btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
with btn_col2:
    predict = st.button(
        "🔍 Predict Customer Segment",
        use_container_width=False
    )

if predict:

    cluster = predict_cluster(
        age=age,
        income=income,
        spending=spending
    )
    segment = cluster_names[cluster]
    # st.success(
    #     f"Predicted Segment: **{cluster_names[cluster]}**"
    # )

    details = segment_details[cluster]
    st.divider()
    #Prediction Result

    section_header("🎯 Prediction Result")

    prediction_card(segment)

    #Customer Details

    with st.expander("📄 View Customer Details", expanded=False):

        st.subheader(details["title"])

        st.write(details["description"])
        st.write("")


        #Customer Characteristics

        bullet_section(
            "Customer Characteristics",
            details["characteristics"]
        )

        st.write("")


        #Marketing Strategy

        bullet_section(
            "Recommended Marketing Strategy",
            details["marketing"]
        )

        st.write("")


        #Business Recommendation

        recommendation_card(
            details["business"]
        )


    st.divider()


    #Cluster Visualization

section_header("📊 Customer Position in Clusters")

with st.container(border=True):

    st.markdown(
        """
        <div style="padding-bottom:10px;">
            <p style="
                color:#64748B;
                font-size:16px;
                margin-bottom:15px;
            ">
                The graph below shows the customer's location relative to the six identified customer segments.
                The red ✕ represents the current customer.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    fig = plot_customer_clusters(
        income=income,
        spending=spending
    )
left, center, right = st.columns([1, 4, 1])

with center:
    st.pyplot(fig, use_container_width=True)

st.divider()