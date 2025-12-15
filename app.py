import streamlit as st
from pathlib import Path

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
ASSETS_DIR = Path(__file__).parent / "assets"

REG_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSe0IJagBJw5RD2C4YsVLz4eN2E1Agrsi5bS0szarnifK0AKw/viewform?usp=dialog"
ABSTRACT_LINK = REG_LINK  # use a different form if you have separate link

st.set_page_config(
    page_title="CHEMFRONT‑2025 | Conference Portal",
    page_icon="🧪",
    layout="wide",
)

# Small helper so missing images do not break the app
def safe_image(path_str, **kwargs):
    path = ASSETS_DIR / path_str
    if path.is_file():
        st.image(str(path), **kwargs)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
with st.sidebar:
    safe_image("logo_pkc.png", width=120)
    safe_image("logo_chemfront.png", width=120)
    st.markdown("### CHEMFRONT‑2025")
    st.caption("Frontiers of Chemistry in Biology, Physics, and Materials")

    page = st.radio(
        "Navigate",
        ["Home", "Themes", "Abstract & Poster", "Registration", "Committees", "Gallery & Venue"],
    )

    st.markdown("---")
    st.markdown("**Important Dates**")
    st.markdown(
        """
- Abstracts: 18 Jan 2026  
- Registration: 25 Jan 2026  
- Conference: 29–30 Jan 2026 [file:31]
        """
    )


# --------------------------------------------------
# HOME
# --------------------------------------------------
if page == "Home":
    safe_image("banner_chemfront.png", use_column_width=True)

    col_logo, col_title = st.columns([1, 3], vertical_alignment="center")
    with col_logo:
        safe_image("logo_pkc.png", width=120)
    with col_title:
        st.title("CHEMFRONT‑2025")
        st.subheader("Frontiers of Chemistry in Biology, Physics, and Materials")

    st.markdown(
        """
CHEMFRONT‑2025 is a two‑day international conference organized by the Department of Chemistry,  
Prabhat Kumar College, Contai, as part of the centenary celebration of the institution.  
It aims to bring together researchers to discuss emerging directions in chemistry at the  
interfaces of biology, physics, and advanced materials. [file:31]
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### About the College")
        st.markdown(
            """
Prabhat Kumar College, established in 1926, is one of the oldest institutions of higher  
learning in Purba Medinipur, offering undergraduate and postgraduate programmes across  
arts, commerce, and science, with active research centres and community engagement. [file:31]
            """
        )
        st.markdown("### About the Department")
        st.markdown(
            """
The Department of Chemistry has a long tradition in teaching and research, with honours  
and postgraduate programmes, well‑equipped laboratories, and ongoing projects in diverse  
areas of chemical science. [file:31]
            """
        )
    with col2:
        safe_image("bg_auditorium.png", use_column_width=True, caption="Campus / Auditorium view")

    st.markdown("### Quick Actions")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🔗 Open Registration Form"):
            st.markdown(f"[Click here to register]({REG_LINK})")
    with c2:
        if st.button("🧾 Submit Abstract / Poster"):
            st.markdown(f"[Submit through Google Form]({ABSTRACT_LINK})")
    with c3:
        st.info("Share this app link with colleagues for quick access.")


# --------------------------------------------------
# THEMES
# --------------------------------------------------
elif page == "Themes":
    st.header("Conference Themes & Tracks")

    st.markdown(
        """
The conference scientific programme covers several broad themes at the frontiers of  
chemistry, reflecting its role in life sciences, physical processes, sustainable  
technologies, and materials innovation. [file:31]
        """
    )

    tcol1, tcol2 = st.columns(2)

    with tcol1:
        st.markdown("### Chemistry at the Interface of Biology")
        st.markdown(
            """
- Metal‑based therapeutics and bioinorganic systems  
- Chemical biology and molecular recognition  
- Biomolecular interactions, including DNA/RNA–protein binding  
- Enzyme chemistry and catalytic mechanisms  
- Biosensors, biochemical sensing, and medicinal chemistry  
- Natural products and phytochemical studies [file:31]
            """
        )

        st.markdown("### Chemical Physics & Theory")
        st.markdown(
            """
- Quantum chemistry and molecular modelling  
- Spectroscopy, photophysics, and reaction dynamics  
- Computational materials chemistry  
- Thermodynamics, statistical mechanics, and electronic structure [file:31]
            """
        )

    with tcol2:
        st.markdown("### Green & Sustainable Chemistry")
        st.markdown(
            """
- Green synthetic methodologies and eco‑friendly reaction design  
- Renewable energy materials (solar, hydrogen, fuel‑cell systems)  
- Waste management, recycling, and remediation  
- Environmental monitoring and pollution control  
- Sustainable catalysts and biodegradable materials [file:31]
            """
        )

        st.markdown("### Emerging Materials & Analytical Chemistry")
        st.markdown(
            """
- Nanomaterials, hybrid composites, MOFs, and supramolecular systems  
- Functional polymers, smart and catalytic materials  
- Photonic, electronic, and optoelectronic materials  
- Advanced spectroscopic and chromatographic techniques  
- Electrochemical sensors, mass spectrometry, and chemometrics‑driven analysis [file:31]
            """
        )


# --------------------------------------------------
# ABSTRACT & POSTER
# --------------------------------------------------
elif page == "Abstract & Poster":
    st.header("Abstract & Poster Information")

    st.markdown(
        """
Participants can contribute through **oral** and **poster** presentations under  
different categories such as UG/PG students, research scholars/associates, and  
faculty members. [file:31]
        """
    )

    st.markdown(
        """
- **Abstract submission deadline:** 18 January 2026  
- Abstracts should follow the official template shared by the organizers.  
- Posters are expected to have a size of roughly **3 × 4 ft** following the  
  guidelines in the poster template. [file:31]
        """
    )

    st.info(
        "Selected high‑quality contributions may be invited to submit full papers to "
        "partner journals, following their independent peer‑review process. [file:31]"
    )

    st.markdown("### Awards")
    st.markdown(
        """
Oral and poster presentations will be evaluated by expert panels, and the best  
presenters in each category will receive awards supported by the Royal Society  
of Chemistry. Prize winners are expected to receive complimentary RSC membership  
for one year. [file:31]
        """
    )

    st.markdown("---")
    st.markdown("### Submit via Google Form")

    col_form, col_img = st.columns([2, 1])
    with col_form:
        st.markdown(
            f"Use the following link to submit your abstract or poster details:<br>"
            f"[**Open Abstract / Poster Submission Form**]({ABSTRACT_LINK})",
            unsafe_allow_html=True,
        )
        st.caption("Please ensure your file and abstract follow the prescribed template. [file:31]")
    with col_img:
        safe_image("abstract_template_thumb.png", use_column_width=True, caption="Sample abstract template preview")
        safe_image("poster_template_thumb.png", use_column_width=True, caption="Sample poster template preview")


# --------------------------------------------------
# REGISTRATION
# --------------------------------------------------
elif page == "Registration":
    st.header("Registration")

    col_reg, col_sponsor = st.columns([2, 1])

    with col_reg:
        st.markdown(
            """
Faculty members, research scholars, UG/PG students, and industry participants  
from academic and research institutions are welcome to register. [file:31]
            """
        )
        st.markdown(
            """
**Indicative registration categories:** [file:31]  
- UG/PG students  
- Research scholars  
- Faculty members  
- Industry participants  
- Foreign participants (USD)  
- Accompanying persons
            """
        )
        st.markdown(
            """
The exact fee amounts and payment instructions are provided in the official brochure  
and communications from the organizing committee, including bank details for transfers. [file:31]
            """
        )

        st.markdown("### Register via Google Form")
        st.markdown(
            f"[**Click here to open the Registration Form**]({REG_LINK})",
            unsafe_allow_html=True,
        )

    with col_sponsor:
        st.markdown("### Sponsor")
        safe_image("logo_wiley.png", width=220, caption="Wiley – Conference Sponsor")
        st.caption("Wiley is listed as a sponsor of the conference. [file:31]")


# --------------------------------------------------
# COMMITTEES
# --------------------------------------------------
elif page == "Committees":
    st.header("Organizing Committees & Resource Persons")

    # President
    c1, c2 = st.columns([1, 3])
    with c1:
        safe_image("prof_amit_k_de.png", width=180, caption="President of the Conference")
    with c2:
        st.markdown("### President of the Conference")
        st.markdown("Principal, Prabhat Kumar College, Contai. [file:31]")

    # Patron
    c3, c4 = st.columns([1, 3])
    with c3:
        safe_image("prof_suprakash_giri.png", width=180, caption="Patron‑in‑Chief")
    with c4:
        st.markdown("### Patron‑in‑Chief")
        st.markdown("President of the Governing Body, Prabhat Kumar College. [file:31]")

    # Convenor
    c5, c6 = st.columns([1, 3])
    with c5:
        safe_image("prof_tithi_maity.png", width=180, caption="Dr. Tithi Maity")
    with c6:
        st.markdown("### Convenor")
        st.markdown(
            """
- Dr. Tithi Maity, Department of Chemistry, Prabhat Kumar College  
  **Phone:** +91‑7908864532  
  **Email:** chemfront2025pkc@gmail.com [file:31]
            """
        )

    st.markdown("### Organizing Committee")
    st.markdown(
        """
The organizing committee includes faculty members from the Department of Chemistry,  
covering a wide range of teaching and research expertise. [file:31]
        """
    )

    st.markdown("### Advisory Committee & Resource Persons")
    st.markdown(
        """
The advisory committee and resource persons comprise eminent scientists from IITs, IISERs,  
IACS, Jadavpur University, the University of Calcutta, Vidyasagar University, and other  
leading institutions. The detailed list is provided in the brochure. [file:31]
        """
    )

    st.markdown("#### Sample Resource‑Person Grid")
    rp_cols = st.columns(4)
    rp_entries = [
        ("rp_goutam_lahiri.png", "Prof. Goutam Lahiri\nIIT Bombay"),
        ("rp_samaresh_bhattacharya.png", "Prof. Samaresh Bhattacharya\nJadavpur University"),
        ("rp_nitin_chattopadhyay.png", "Prof. Nitin Chattopadhyay\nJadavpur University"),
        ("rp_chitta_ranjan_sinha.png", "Prof. Chitta Ranjan Sinha\nJadavpur University"),
    ]
    for col, (img, caption) in zip(rp_cols, rp_entries):
        with col:
            safe_image(img, use_column_width=True, caption=caption)


# --------------------------------------------------
# GALLERY & VENUE
# --------------------------------------------------
elif page == "Gallery & Venue":
    st.header("Gallery & Venue")

    st.markdown("### Nearby Places to Visit")
    st.caption("As listed in the conference brochure. [file:31]")

    gcols = st.columns(3)
    places = [
        ("place_digha_beach.png", "Digha sea beach"),
        ("place_jagannath_temple.png", "Jagannath temple"),
        ("place_mandarmani.png", "Mandarmoni"),
        ("place_talsari.png", "Talsari"),
        ("place_dariapur_lighthouse.png", "Dariapur lighthouse"),
        ("place_kapalkundala_temple.png", "Kapalkundala temple"),
    ]
    for i, (img, label) in enumerate(places):
        with gcols[i % 3]:
            safe_image(img, use_column_width=True, caption=label)

    st.markdown("---")
    st.markdown("### Venue & Location")

    st.markdown(
        """
**Venue address:**  
Prabhat Kumar College  
311, SH 4, Professor Colony, Post Karkuli,  
Contai, West Bengal 721401, India. [file:31]
        """
    )

    # Use the embed src generated from Google Maps "Share -> Embed a map"
    map_embed_src = (
        "https://www.google.com/maps/embed?pb="
        "!1m18!1m12!1m3!1d0!2d87.7403703!3d21.7768598!2m3!1f0!2f0!3f0!"
        "3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a0326f69188c8e7%3A0xc783bc5d86c61503!"
        "2sPrabhat%20Kumar%20College!5e0!3m2!1sen!2sin!4v1700000000000"
    )

    st.components.v1.iframe(map_embed_src, height=350)

    st.markdown(
        """
You can also open the location directly in Google Maps for navigation:  
[Open in Google Maps](https://www.google.com/maps/dir//311,+SH+4,+Professor+Colony,+Post,+Karkuli,+Contai,+West+Bengal+721401/) [web:27]
        """
    )
