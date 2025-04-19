import streamlit as st
from PIL import Image

st.title("Cancer-related Blogs")

# Sample images for each blog (you can replace with actual image paths or URLs)
images = {
    "Understanding Cancer: The Basics": "assets/blog_img1.jpg",
    "How AI is Revolutionizing Cancer Detection": "assets/blog_img2.jpg",
    "The Importance of Regular Screenings for Cancer Prevention": "assets/blog_img3.jpg",
    "New Treatments in Oncology": "assets/blog_img4.jpg",
    "The Role of Nutrition in Cancer Recovery": "assets/blog_img5.jpg"
}

blogs = [
    {
        "title": "Understanding Cancer: The Basics",
        "content": """
        Cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body. 
        Not all tumors are cancerous; benign tumors do not spread to other parts of the body.
        There are over 100 types of cancer, including breast cancer, skin cancer, lung cancer, colon cancer, and prostate cancer.
        Early detection and treatment can significantly improve the prognosis for many types of cancer.
        """,
        "author": "Dr. John Doe",
        "link": "https://www.cancer.org/cancer/cancer-basics.html"
    },
    {
        "title": "How AI is Revolutionizing Cancer Detection",
        "content": """
        Artificial intelligence (AI) is transforming the way we approach cancer detection. With advanced algorithms, 
        AI can analyze medical images, identify patterns, and even predict cancer with higher accuracy than traditional methods.
        AI tools are being developed to assist radiologists and pathologists, helping to reduce the burden of manual analysis.
        However, AI is a complement, not a replacement, for expert medical judgment.
        """,
        "author": "Dr. Jane Smith",
        "link": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7604552/"
    },
    {
        "title": "The Importance of Regular Screenings for Cancer Prevention",
        "content": """
        Regular screenings are a key factor in cancer prevention and early detection. 
        Common screening tests include mammograms for breast cancer, colonoscopies for colon cancer, and Pap tests for cervical cancer.
        Early detection through screening increases the chances of successful treatment and survival.
        Always consult with your healthcare provider to understand which screenings are appropriate for you based on your age and risk factors.
        """,
        "author": "Dr. Emily Johnson",
        "link": "https://www.cancer.gov/about-cancer/screening"
    },
    {
        "title": "New Treatments in Oncology",
        "content": """
        Oncology has seen a rapid development in treatments over the last decade. 
        Immunotherapy, targeted therapy, and personalized medicine are at the forefront of cancer treatment. 
        These therapies target cancer cells specifically, reducing the damage to healthy cells and improving patient outcomes.
        Ongoing research continues to improve the efficacy of these treatments, bringing hope to patients worldwide.
        """,
        "author": "Dr. Michael Lee",
        "link": "https://www.cancer.org/latest-news/5-cancer-treatment-advances-from-the-past-year.html"
    },
    {
        "title": "The Role of Nutrition in Cancer Recovery",
        "content": """
        Proper nutrition plays a crucial role in cancer recovery and overall well-being. 
        Certain foods may help strengthen the immune system, reduce inflammation, and support the body during and after treatment.
        A balanced diet, rich in fruits, vegetables, and lean proteins, is recommended for cancer patients. 
        Consult with a dietitian to create a personalized plan tailored to your needs during recovery.
        """,
        "author": "Dr. Sarah Adams",
        "link": "https://www.oncologynutrition.org/"
    }
]

# Displaying each blog with an image and more information link
for blog in blogs:
    st.subheader(blog['title'])
    st.write(f"**Author:** {blog['author']}")
    st.image(Image.open(images[blog['title']]), use_column_width=True)  # Load the respective image
    st.write(blog['content'])
    st.markdown(f"[Read more about this topic here]({blog['link']})", unsafe_allow_html=True)
    st.markdown("---")

# Footer
st.markdown("Powered by [CureCanAI](https://yourwebsite.com)")
