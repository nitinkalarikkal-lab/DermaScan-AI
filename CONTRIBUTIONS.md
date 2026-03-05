# Team Contributions - Dermascan AI

This document outlines the contributions of each team member towards the development of the Dermascan AI project. The technical implementation of the AI/Machine Learning model was handled by external professionals; the student team focused on integrating this model into a functional web application, designing the system, and ensuring robust performance.

## Project Overview
**Project Name:** Dermascan AI
**Team Size:** 4 Members

---

## Member 1: **Backend Architect & Database Design**
**Primary Responsibility:** Designing the data structure and managing server-side operations.

**Key Contributions:**
*   **Database Schema:** Created the relational database models in `app/models.py` (Users, Doctors, Appointments, Feedback).
*   **User Management:** Implemented authentication (Login/Signup/Logout) and role-based access control.
*   **Admin Customization:** Configured the Django Admin panel (`app/admin.py`) for easy management of data.
*   **Security:** Ensured secure handling of sensitive data (password hashing, CSRF protection).

## Member 2: **Frontend Designer (UI/UX)**
**Primary Responsibility:** Creating the visual interface and optimizing user experience.

**Key Contributions:**
*   **Responsive Design:** Developed the HTML structure and CSS styling for a seamless experience on desktop and mobile.
*   **Template Creation:** Built the core templates (e.g., `user_complaint.html`, `doctor_header.html`, `index.html`) using Django's template language.
*   **Visual Assets:** Managed static assets (images, icons) and ensured a consistent color scheme/typography.
*   **Interactivity:** Implemented JavaScript for client-side interactions and dynamic content updates.

## Member 3: **Logic Developer & System Integration**
**Primary Responsibility:** Connecting the frontend to backend and integrating the AI model.

**Key Contributions:**
*   **Model Integration:** Wrote the Python logic in `app/views.py` to load the professional `.h5` model and generate predictions from user uploads.
*   **Business Logic:** Developed the core views for handling appointments, bookings, and image processing.
*   **Data Flow:** Managed URL routing (`app/urls.py`) to ensure correct navigation between pages.
*   **Form Handling:** Implemented form validations and error handling for user inputs.

## Member 4: **Project Lead, Testing & Documentation**
**Primary Responsibility:** Project coordination, quality assurance, and reporting.

**Key Contributions:**
*   **Requirements Analysis:** Conducted the feasibility study and defined the system requirements (SRS).
*   **Documentation:** Authored the Project Report (`Dermascan_AI_Project_Report.md`) and Presentation (`Dermascan_AI_Presentation_v2.pptx`).
*   **Quality Assurance (QA):** Performed Blackbox and Whitebox testing to identify and fix bugs.
*   **Deployment:** Configured `settings.py` for local deployment and managed the `manage.py` execution environment.

---

## Updated Viva Questions & Answers

**Q: Did you build the AI model yourselves?**
A: No, the core ML model training was handled by professionals to ensure high accuracy. Our team focused on **integrating** this powerful model into a user-friendly web application, handling the data pipeline, and building the full system around it.

**Q: What was [Member 3]'s role then?**
A: [Member 3] worked on the *application logic*—taking the user's image, processing it, feeding it to the model, and displaying the results back to the user. They bridged the gap between the raw model and the web interface.

**Q: Who designed the database?**
A: [Member 1] designed the schema to handle users, doctors, and appointments efficiently.

**Q: Who is responsible for the look and feel?**
A: [Member 2] designed all the templates and styles to ensure the application is easy to use.
