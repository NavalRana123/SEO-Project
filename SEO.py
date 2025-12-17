import streamlit as st

st.set_page_config(page_title="Business Website", layout="centered")

st.markdown("""
    <style>
        .main {
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2 {
            color: #0E76A8;
        }
        .section {
            padding: 20px 0;
            border-bottom: 1px solid #ddd;
        }
        .quote-button {
            background-color: #0E76A8;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            text-align: center;
            cursor: pointer;
            display: inline-block;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome to Your Business Website")
    
with st.container():
    st.subheader("🏠 Home")
    st.write("Welcome to our business hub where ideas meet execution. We deliver custom solutions to drive your brand forward.")

with st.container():
    st.subheader("📄 Pages")
    st.write("""
    - **Home** – Overview and highlights  
    - **About Us** – Our story and mission  
    - **FAQ** – Common questions answered  
    - **Privacy & Terms** – Legal and policy info  
    """)

with st.container():
    st.subheader("💼 Services")
    st.write("""
    - Web Development  
    - SEO & Digital Marketing  
    - Graphic & Logo Design  
    - Mobile App Development  
    - IT Consulting  
    """)

with st.container():
    st.subheader("🖼️ Portfolio")
    st.write("""
    - E-commerce platforms with 10k+ monthly visits  
    - Branding kits for startups  
    - SEO projects with 3x traffic growth  
    - Mobile apps with 50k+ downloads  
    """)

with st.container():
    st.subheader("📞 Contact")
    st.write("""
    - 📧 Email: info@yourcompany.com  
    - 📱 Phone: +91-9876543210  
    - 📍 Location: Your City, Your Country  
    """)

with st.container():
    st.subheader("📝 Get a Quote")
    with st.form("quote_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        project = st.text_area("Describe your project")
        submitted = st.form_submit_button("Request Quote")
        if submitted:
            st.success("✅ Thank you! We'll contact you shortly.")

st.markdown("<br><center>© 2025 Your Company Name</center>", unsafe_allow_html=True)