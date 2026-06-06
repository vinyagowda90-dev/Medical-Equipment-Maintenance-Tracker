import streamlit as st

st.set_page_config(
    page_title="Medical Device Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medical Device Failure Analytics")

st.markdown("""
### Smart Healthcare Equipment Monitoring Dashboard

Analyze:
- Device Failures
- Maintenance Costs
- Downtime
- Device Age
- Failure Trends
- Predictive Maintenance
""")

st.image(
    "https://images.unsplash.com/photo-1576091160550-2173dba999ef",
    use_container_width=True
)
