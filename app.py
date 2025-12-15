# app.py
import streamlit as st
import pandas as pd
import datetime as dt
from google.oauth2 import service_account
from googleapiclient.discovery import build

# -----------------------------
# CONFIG
# -----------------------------
SHEET_ID = "1gyAsrf-9Itqb33pjSxBkRppXlxyeUYE8brUPGUPoHaI"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
REG_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSe0IJagBJw5RD2C4YsVLz4eN2E1Agrsi5bS0szarnifK0AKw/viewform?usp=dialog"
# Replace with the actual abstract/poster form link if separate
ABSTRACT_LINK = REG_LINK  

@st.cache_resource
def get_sheets_service():
    creds = service_account.Credentials.from_service_account_file(
        "service_account.json", scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    return service

def append_row(sheet_name, row_values):
    """Append a row to a sheet tab."""
    service = get_sheets_service()
    body = {"values": [row_values]}
    service.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range=f"{sheet_name}!A1",
        valueInputOption="USER_ENTERED",
        body=body,
    ).execute()

# Ensure tabs exist (only runs on demand; harmless if they already exist)
def ensure_tab(sheet_name, header):
    service = get_sheets_service()
    spreadsheet = service.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    sheet_titles = [s["properties"]["title"] for s in spreadsheet["sheets"]]
    if sheet_name in sheet_titles:
        return
    # Add new sheet/tab
    requests = [
        {
            "addSheet": {
                "properties": {
                    "title": sheet_name,
                }
            }
        }
    ]
    body = {"requests": requests}
    service.spreadsheets().batchUpdate(
        spreadsheetId=SHEET_ID, body=body
    ).execute()
    # Set header row
    append_row(sheet_name, header)

def log_click(sheet_name, name, email, purpose):
    ensure_tab(sheet_name, ["Timestamp", "Name", "Email", "Purpose"])
    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    append_row(sheet_name, [timestamp, name, email, purpose])

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="CHEMFRONT-2025 | Conference Portal",
    page_icon="🧪",
    layout="wide",
)

st.sidebar.title("CHEMFRONT-2025")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Themes", "Abstract & Poster", "Registration", "Committees"],
)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    st.title("CHEMFRONT‑2025")
    st.subheader("Frontiers of Chemistry in Biology, Physics, and Materials")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(
            """
CHEMFRONT‑2025 is a two‑day international conference organized by the Department of Chemistry,  
Prabhat Kumar College, Contai, as part of the centenary celebration of the institution.  
The event will be held on **29–30 January 2026** and will bring together scientists,  
academicians, researchers, and students to discuss recent advances at the interfaces of  
chemistry with biology, physics, and materials science. [file:31]
            """
        )
        st.markdown(
            """
**Venue:** Prabhat Kumar College, Contai, Purba Medinipur, West Bengal, India. [file:31]  

The conference emphasizes interdisciplinary research areas such as functional materials,  
green and sustainable chemistry, bioinspired systems, advanced spectroscopic techniques,  
and data‑driven analytical methods. [file:31]
            """
        )
    with col2:
        st.info(
            "**Key Dates**  \n"
            "- Abstract submission deadline: 18 January 2026  \n"
            "- Registration deadline: 25 January 2026  \n"
            "- Conference dates: 29–30 January 2026 [file:31]"
        )

# -----------------------------
# THEMES
# -----------------------------
elif page == "Themes":
    st.title("Themes & Sub‑themes")

    st.markdown("### Chemistry at the Interface of Biology")
    st.markdown(
        """
- Metal‑based therapeutics and bioinorganic systems  
- Chemical biology, molecular recognition, and enzyme mechanisms  
- Biomolecular interactions, including DNA/RNA–protein binding  
- Biosensors, biochemical sensing, and medicinal chemistry  
- Natural products and phytochemical investigations [file:31]
        """
    )

    st.markdown("### Chemical Physics and Theoretical Chemistry")
    st.markdown(
        """
- Quantum chemistry, molecular modelling, and reaction dynamics  
- Spectroscopy, photophysics, and electronic structure  
- Thermodynamics, statistical mechanics, and computational materials chemistry [file:31]
        """
    )

    st.markdown("### Green and Sustainable Chemistry")
    st.markdown(
        """
- Environment‑friendly synthetic methodologies and catalysis  
- Renewable energy materials for solar, hydrogen, and fuel‑cell technologies  
- Waste management, recycling, and pollution remediation  
- Biodegradable and sustainable materials [file:31]
        """
    )

    st.markdown("### Emerging Materials in Chemistry")
    st.markdown(
        """
- Nanomaterials, nanotechnology, and hybrid composites  
- Metal–organic frameworks and supramolecular architectures  
- Functional polymers, smart materials, and catalytic systems  
- Photonic, electronic, and optoelectronic materials [file:31]
        """
    )

    st.markdown("### Analytical and Instrumental Chemistry")
    st.markdown(
        """
- Modern spectroscopic and chromatographic techniques  
- Electrochemical sensors and advanced imaging approaches  
- Chemometrics and data‑driven analytical workflows  
- Environmental and forensic analysis [file:31]
        """
    )

# -----------------------------
# ABSTRACT & POSTER
# -----------------------------
elif page == "Abstract & Poster":
    st.title("Abstract & Poster Information")

    st.markdown(
        """
**Abstract submission deadline:** 18 January 2026. [file:31]  

Participants can contribute through **oral** or **poster** presentations under  
different categories such as UG/PG students, research scholars/associates,  
and faculty members. Presentations will be evaluated by expert panels, and  
outstanding contributions in each category will receive awards supported by  
the Royal Society of Chemistry, along with complimentary RSC membership for  
one year for prize recipients. [file:31]
        """
    )

    st.markdown(
        """
**Poster guidelines:**  
Approximate size around **3 × 4 ft**; further layout and design guidance is  
provided in the official poster template. [file:31]
        """
    )

    st.markdown(
        """
You are requested to follow the official abstract and poster templates  
for formatting. The template links are provided in the brochure and may  
also be communicated via email by the organizers. [file:31]
        """
    )

    st.subheader("Submit via Google Form")

    with st.form("abstract_click_form"):
        name = st.text_input("Your Name (for log)", "")
        email = st.text_input("Email (for log)", "")
        submitted = st.form_submit_button("Go to Abstract / Poster Submission Form")
        if submitted:
            log_click("Clicks_Abstracts", name, email, "Abstract/Poster form opened")
            st.success("Click logged. The Google Form will open in a new tab.")
            st.markdown(f"[Open Abstract / Poster Submission Form]({ABSTRACT_LINK})")

# -----------------------------
# REGISTRATION
# -----------------------------
elif page == "Registration":
    st.title("Registration")

    st.markdown(
        """
Faculty members, research scholars, UG/PG students, and industry professionals  
are invited to register for CHEMFRONT‑2025. [file:31]  

Registration fees (approximate, as described in the brochure): [file:31]  
- UG/PG students  
- Research scholars  
- Faculty members  
- Industry participants  
- Foreign participants (in USD)
        """
    )

    st.markdown(
        """
Payment details, including bank account information and any additional  
instructions, are specified in the official brochure and communications  
from the organizing committee. [file:31]
        """
    )

    st.subheader("Register via Google Form")

    with st.form("registration_click_form"):
        name = st.text_input("Your Name (for log)", "")
        email = st.text_input("Email (for log)", "")
        submitted = st.form_submit_button("Go to Registration Form")
        if submitted:
            log_click("Clicks_Registration", name, email, "Registration form opened")
            st.success("Click logged. The Google Form will open in a new tab.")
            st.markdown(f"[Open Registration Form]({REG_LINK})")

# -----------------------------
# COMMITTEES
# -----------------------------
elif page == "Committees":
    st.title("Organizing Committees & Contacts")

    st.markdown("### President of the Conference")
    st.markdown(
        """
- Principal, Prabhat Kumar College, Contai [file:31]
        """
    )

    st.markdown("### Patron‑in‑Chief")
    st.markdown(
        """
- President of the Governing Body, Prabhat Kumar College [file:31]
        """
    )

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
The organizing committee consists of faculty members from the Department of  
Chemistry, Prabhat Kumar College, actively involved in teaching and research  
across diverse areas of chemical science. [file:31]
        """
    )

    st.markdown("### Advisory Committee & Resource Persons")
    st.markdown(
        """
The advisory committee and resource persons include distinguished scientists  
from institutes such as IITs, IISERs, IACS, Jadavpur University, the University  
of Calcutta, and other reputed universities and research centers in India and  
abroad. Their participation will ensure high‑quality scientific discussions  
through plenary, invited, and contributory talks. [file:31]
        """
    )

    st.markdown(
        """
For complete and up‑to‑date lists of committee members and invited speakers,  
please refer to the official conference brochure and announcements shared  
by the organizers. [file:31]
        """
    )
