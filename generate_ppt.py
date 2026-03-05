
import collections 
import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_presentation():
    try:
        prs = Presentation()
    except Exception as e:
        print(f"Error initializing Presentation: {e}")
        return

    # Helper to add slides
    def add_slide(title_text, content_list):
        layout = prs.slide_layouts[1] # Bullet layout
        slide = prs.slides.add_slide(layout)
        title = slide.shapes.title
        body = slide.placeholders[1]
        
        title.text = title_text
        tf = body.text_frame
        tf.word_wrap = True
        
        for i, item in enumerate(content_list):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            
            # Simple indefinite handling for sub-bullets
            clean_text = item.strip()
            if clean_text.startswith("-"):
                p.level = 1
                p.text = clean_text.lstrip("- ").strip()
            else:
                p.level = 0
                p.text = clean_text

    # Title Slide
    try:
        slide_layout = prs.slide_layouts[0] # Title Slide
        slide = prs.slides.add_slide(slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = "Dermascan AI (AI Skin Expert)"
        subtitle.text = "Revolutionizing Dermatological Care with Artificial Intelligence\n\nPresented By: [Your Name]\nGuided By: [Guide Name]"
    except Exception as e:
        print(f"Error creating title slide: {e}")

    # Content Slides
    slides = [
        ("Introduction", [
            "Overview: A centralized digital platform bridging patients and dermatologists.",
            "Goal: Provide accessible, efficient, and transparent skin disease diagnosis.",
            "Key Tech: Artificial Intelligence (Deep Learning) for preliminary diagnosis.",
            "Impact: Streamlines appointments and ensures prompt medical advice."
        ]),
        ("Problem Statement", [
            "Accessibility: Remote areas lack specialized dermatologists.",
            "Inefficiency: Manual booking leads to wait times and conflicts.",
            "Delayed Diagnosis: Scarcity of specialists delays screening.",
            "Records: Physical files are hard to track and maintain."
        ]),
        ("Proposed Solution", [
            "Automated Platform: Connects Patients, Doctors, and Admins.",
            "AI-Powered Analysis: Instant preliminary results for skin lesions.",
            "Digital Records: Secure, accessible history.",
            "Feedback Loop: Integrated rating system for quality assurance."
        ]),
        ("Salient Features", [
            "User Roles: Distinct features for Admin, Doctors, Patients.",
            "AI Disease Detection: Deep Learning analysis of skin images.",
            "Smart Scheduling: Dynamic appointment booking.",
            "Real-Time Communication: Chat and feedback systems.",
            "Analytics: Dashboard for system monitoring."
        ]),
        ("System Analysis", [
            "Feasibility:",
            "- Technical: Python, Django, TensorFlow (Open Source).",
            "- Economic: Cost-effective, minimal licensing.",
            "Methodology: Iterative Waterfall / Agile approach."
        ]),
        ("Technology Stack", [
            "Frontend: HTML5, CSS3, JavaScript, Bootstrap.",
            "Backend: Python, Django Framework.",
            "Database: SQLite / MySQL.",
            "AI Model: TensorFlow / Keras."
        ]),
        ("System Modules", [
            "Admin: Manage users, verify doctors, view stats.",
            "Doctor: Manage profile/schedule, view appointments, chat.",
            "Patient: Upload images (AI Scan), book appointments, feedback."
        ]),
        ("Database Design", [
            "User: Authentication and roles.",
            "Doctor: Professional details and credentials.",
            "Doctor_schedule: Availability management.",
            "Booking: Appointment transactions.",
            "SkinPredictionHistory: AI analysis logs.",
            "Payment & Feedback: Transaction and quality tracking."
        ]),
        ("Testing", [
            "Unit Testing: Verified individual models and views.",
            "Integration Testing: Checked data flow (Frontend <-> Backend).",
            "System Testing: Validated full user workflows.",
            "Compatibility: Tested on Chrome and Firefox."
        ]),
        ("Future Enhancements", [
            "Mobile App: For on-the-go access (iOS/Android).",
            "Advanced AI: Personalized care and progression tracking.",
            "Telemedicine: Integrated video consultations.",
            "Blockchain: Secure, immutable medical records."
        ]),
        ("Conclusion", [
            "Summary: Validated, user-friendly, and scalable solution.",
            "Benefit: Empowers patients and optimizes doctor workflows.",
            "Closing: Ensures medical advice reaches those in need promptly."
        ]),
        ("Bibliography", [
            "Books: Introduction to Computing (E. Balaguruswamy).",
            "Docs: Python.org, DjangoProject.com, W3Schools."
        ])
    ]

    for title, content in slides:
        add_slide(title, content)

    # Save
    try:
        output_file = 'Dermascan_AI_Presentation.pptx'
        prs.save(output_file)
        print(f"Presentation saved successfully as '{output_file}'")
    except Exception as e:
        print(f"Error saving presentation: {e}")

if __name__ == "__main__":
    try:
        create_presentation()
    except ImportError:
        print("Error: python-pptx library is not installed.")
        print("Please run: pip install python-pptx")
    except Exception as e:
        print(f"An error occurred: {e}")
