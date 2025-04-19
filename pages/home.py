import streamlit as st

def contact_specialist_page():
    st.title("Contact a Specialist")
    st.write("Here are the details of the doctors available to assist you:")

    specialists = [
        {"name": "Dr. Suresh Advani", "specialty": "Medical Oncologist", "contact": "info@jaslokhospital.net"},
        {"name": "Dr. Ramesh Sarin", "specialty": "Surgical Oncologist", "contact": "contactus_delhi@apollohospitals.com"},
        {"name": "Dr. Vinod Raina", "specialty": "Medical Oncologist", "contact": "vinod.raina@fortishealthcare.com"},
        {"name": "Dr. Sanjay Sharma", "specialty": "Breast Oncologist", "contact": "appointments@maxhealthcare.com"},
        {"name": "Dr. Anil Heroor", "specialty": "Surgical Oncologist", "contact": "anil.heroor@fortishealthcare.com"},
        {"name": "Dr. Shona Nag", "specialty": "Medical Oncologist", "contact": "contactus@jehangirhospital.com"},
        {"name": "Dr. Rajendra Badwe", "specialty": "Surgical Oncologist", "contact": "rajendra.badwe@tmc.gov.in"},
        {"name": "Dr. Manjiri Mehta", "specialty": "Breast Surgeon", "contact": "manjiri.mehta@fortishealthcare.com"},
        {"name": "Dr. P.K. Julka", "specialty": "Medical Oncologist", "contact": "pk.julka@maxhealthcare.com"},
        {"name": "Dr. Kapil Kumar", "specialty": "Surgical Oncologist", "contact": "kapil.kumar@blkhospital.com"},
    ]

    for specialist in specialists:
        st.write(f"**{specialist['name']}** - {specialist['specialty']}")
        st.write(f"Contact: {specialist['contact']}")
        st.write("---")

    if st.button("Back to Home"):
        st.session_state.contact_specialist = False



def why_choose_us_page():
    st.title("Why Choose Us??")
    st.write("Below are the key elements used in cancer detection and their definitions:")

    # Definitions for each element in user_data
    definitions = {
        'radius_mean': 'Mean of distances from the center to the points on the perimeter of the tumor. A higher radius value in a cell image can indicate that the cancer has spread to other parts of the body.',
        'texture_mean': 'Standard deviation of gray-scale values, representing the consistency in pixel intensity.',
        'perimeter_mean': 'Average perimeter length of the tumor.',
        'area_mean': 'Mean area of the tumor region.',
        'smoothness_mean': 'Local variation in radius lengths, indicating the smoothness of the tumor boundary.',
        'compactness_mean': 'Measure of how compact the tumor is, calculated as perimeter^2 / area - 1.0.',
        'concavity_mean': 'Mean of the severity of concave portions of the tumor contour.',
        'concave points_mean': 'Mean number of concave points on the tumor contour.',
        'symmetry_mean': 'Mean symmetry of the tumor.',
        'fractal_dimension_mean': 'Mean of the "coastline approximation" of the tumor, representing the complexity of the shape.',
        'radius_se': 'Standard error of the mean radius.',
        'texture_se': 'Standard error of the mean texture.'
    }

  
    for key, description in definitions.items():
        st.write(f"**{key.replace('_', ' ').capitalize()}**: {description}")
        st.write("---")

    if st.button("Back to Home"):
        st.session_state.why_choose_us = False



def main_page():
    images = [
        "https://stgaccinwbsdevlrs01.blob.core.windows.net/newcorporatewbsite/blogs/october2023/detail-main-polotno-52-1.jpg",
        "https://cdn.labmanager.com/assets/articleNo/21809/aImg/40005/cancer-cell-l.jpg",
        "https://www.millenniumcancercenter.com/wp-content/uploads/2018/07/09-blog-blood-cancer.jpg",
    ]

    captions = [
        "Research on Cancer Development",
        "Microscopic View of Cancer Cells",
        "Types of Blood Cancer"
    ]

    html_code = """
    <style>
      .slider-container {{
        position: relative;
        width: 100%;
        height: 300px;
        overflow: hidden;
        margin: auto;
      }}

      .slides {{
        display: flex;
        transition: transform 1s ease;
      }}

      .slide {{
        min-width: 100%;
        position: relative;
      }}

      .slide img {{
        width: 100%;
        height: auto;
      }}

      .caption {{
        position: absolute;
        bottom: 10px;
        left: 20px;
        color: white;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 10px;
        font-size: 1.2em;
      }}
    </style>

    <div class="slider-container">
      <div class="slides" id="slides">
        {}
      </div>
    </div>

    <script>
      let currentIndex = 0;
      const slides = document.getElementById('slides');
      const slideCount = slides.children.length;

      function showNextSlide() {{
        currentIndex = (currentIndex + 1) % slideCount;
        slides.style.transform = `translateX(-${{currentIndex * 100}}%)`;
      }}

      setInterval(showNextSlide, 3000);
    </script>
    """

    slide_images = "".join(
        [f'<div class="slide"><img src="{img}" alt="Image {i+1}"/><div class="caption">{captions[i]}</div></div>' for i, img in enumerate(images)]
    )
    html_code = html_code.format(slide_images)
    st.components.v1.html(html_code, height=350)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Why Choose Us?"):
            st.session_state.why_choose_us = True

    with col2:
        if st.button("Contact a Specialist"):
            st.session_state.contact_specialist = True

    st.subheader("Resources")
    tab1, tab2, tab3 = st.tabs(["Common Symptoms", "Screening Methods", "Prevention Tips"])

    with tab1:
         st.write("Common Cancer Symptoms")
         st.write("- Unexplained weight loss")
         st.write("- Fatigue")
         st.write("- Fever")
         st.write("- Pain")
         st.write("- Skin changes")

    with tab2:
        st.write("Screening Methods")
        st.write("- Mammography")
        st.write("- Colonoscopy")
        st.write("- Pap smear test")
        st.write("- PSA test")
        st.write("- Low-dose CT scan")

    with tab3:
        st.write("Prevention Tips")
        st.write("- Regular check-ups")
        st.write("- Healthy diet")
        st.write("- Avoid smoking and alcohol")
        st.write("- Exercise regularly")

    st.subheader("About Cancer Detection")
    st.write("""
    Cancer detection involves various screening methods and tests to identify cancer in its early stages.
    Regular check-ups and awareness of potential symptoms are crucial for early detection.
    """)

    st.write("---")
    st.write("© 2024 Cancer Detection Info. All rights reserved.")
    st.write("Terms of Service | Privacy")

    footer_cols = st.columns(3)
    with footer_cols[0]:
         st.write("Use Case")
         st.write("UI Design, UX Design, Wireframing, Diagramming")

    with footer_cols[1]:
        st.write("Explore")
        st.write("Design, Prototyping, Development Features")

    with footer_cols[2]:
        st.write("Resources")
        st.write("Blog, Best Practices, Colors, Support")



if "contact_specialist" not in st.session_state:
    st.session_state.contact_specialist = False

if "why_choose_us" not in st.session_state:
    st.session_state.why_choose_us = False

if st.session_state.contact_specialist:
    contact_specialist_page()
elif st.session_state.why_choose_us:
    why_choose_us_page()
else:
    main_page()
