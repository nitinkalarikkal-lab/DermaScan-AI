# DERMASCAN AI (AI SKIN EXPERT)

**MAIN PROJECT REPORT**

Submitted in partial fulfillment of requirement for the award of the degree of

**[YOUR DEGREE NAME]**

By
**[YOUR NAME]**

Under the supervision of
**[GUIDE NAME]**

---

# INDEX

1. **INTRODUCTION**
    1.1. ABOUT THE PROJECT
    1.2. SCOPE OF THE PROJECT
    1.3. SALIENT FEATURES OF THE SYSTEM
2. **SYSTEM ANALYSIS**
    2.1. WHAT IS SYSTEM ANALYSIS
    2.2. IDENTIFICATION OF NEED
    2.3. PRELIMINARY INVESTIGATION
    2.4. EXISTING SYSTEM
    2.5. PROPOSED SYSTEM
    2.6. FEASIBILITY STUDY
3. **METHODOLOGY & SYSTEM REQUIREMENTS**
    3.1. SOFTWARE LIFE CYCLE
    3.2. HARDWARE REQUIREMENTS
    3.3. SOFTWARE REQUIREMENTS
4. **SYSTEM DESIGN & DEVELOPMENT**
    4.1. PROJECT DESCRIPTION
    4.2. DATA FLOW DIAGRAM
    4.3. MODULES
    4.4. DATABASE DESIGN
5. **CODING**
6. **TESTING**
7. **FUTURE ENHANCEMENT**
8. **CONCLUSION**
9. **BIBLIOGRAPHY**

---

# 1. INTRODUCTION

## 1.1. ABOUT THE PROJECT

Dermascan AI is designed to revolutionize the preliminary diagnosis of skin diseases and enhance patient-doctor interaction by connecting patients and dermatologists through a centralized digital platform. The system ensures efficient detection of skin conditions, streamlined appointment handling, and accessible healthcare, ensuring medical advice reaches those in need promptly.

The project aims to create an automated, transparent, and accessible solution to dermatological concerns by leveraging Artificial Intelligence. By integrating deep learning for image analysis, automated appointment processing, data analytics, and feedback mechanisms, the system enhances coordination among stakeholders and contributes to proactive health management. Administrators oversee users, doctors, and system reports while ensuring efficient doctor approvals, complaint resolution, and system optimization through analytics.

Doctors manage their professional profiles, update consultation schedules, and view patient appointments while providing essential medical care. The system allows them to streamline their practice and reach a broader patient base. Patients upload images of skin lesions for instant AI analysis, track their skin health history, and book appointments efficiently while providing feedback on their consultation experience. The system also includes feedback and complaint features, ensuring continuous improvement of quality standards.

All these roles function together to create a structured and efficient dermatological healthcare system that reduces anxiety, improves accessibility, and ensures patients receive timely medical attention.

## 1.2. SCOPE OF THE PROJECT

The scope of this project extends beyond simple image classification, aiming to create a scalable and sustainable solution applicable to both urban and rural healthcare settings. It supports patients who may lack immediate access to specialists by offering structured insights into their skin health. By enhancing coordination between patients and doctors and leveraging technology, the system plays a critical role in promoting early detection of skin diseases and ensuring professional care is accessible to all.

## 1.3. SALIENT FEATURES OF THE SYSTEM

*   **User Management:**
    *   **Admin:** Manages doctors, patients, complaints, and views system statistics.
    *   **Doctors:** Tools for updating profiles, managing schedules, viewing appointments, and tracking earnings.
    *   **Patients:** Register, upload skin images for analysis, book appointments, and submit feedback.

*   **AI-Based Skin Disease Detection:** Tracks and analyzes user-uploaded images using Deep Learning models to identify potential skin diseases with a confidence score, ensuring immediate preliminary results.

*   **Doctor Appointment & Scheduling:** Enables doctors to set availability (dates, times, fees) and allows patients to book slots seamlessly, streamlining the consultation process.

*   **Integrated Complaint System:** Allows users and doctors to raise issues and receive timely resolutions from administrators.

*   **Data Analytics and Reporting:** Provides detailed reports on patient registration, active doctors, appointment volume, and other key metrics to drive informed decision-making.

*   **Real-Time Status Updates:** Enables live updates on appointment status (Pending/Approved/Rejected) and payment processing.

*   **Feedback & Rating System:** Offers a mechanism for patients to rate doctors and provide reviews, ensuring quality control and trust within the platform.

*   **Online Chat Consultation:** Facilitates secure, real-time communication between patients and doctors for follow-up questions, prescription clarifications, and continuous care.

---

# 2. SYSTEM ANALYSIS

## 2.1. WHAT IS SYSTEM ANALYSIS

System analysis is a process of gathering and interpreting facts, diagnosing problems and the information to recommend improvements on the system. It is a problem-solving activity that requires intensive communication between the system users and system developers. System analysis or study is an important phase of any system development process. The system is studied in detail and analyzed. The system analyst plays the role of the interrogator and dwells deep into the working of the present system. The system is viewed as a whole and the input to the system is identified.

The outputs from the organizations are traced to the various processes. System analysis is concerned with becoming aware of the problem, identifying the relevant and decisional variables, analyzing and synthesizing various factors and determining an optimal or at least a satisfactory solution or program of action.

A detailed study of the process must be done by various techniques like interviews, questionnaires etc. The data collected by these sources must be scrutinized to arrive to a conclusion. The conclusion is an understanding of how the system functions. This system is called the existing system. Now the existing system is subjected to close study and problem areas are identified. The designer now functions as a problem solver and tries to sort out the difficulties that the enterprise faces. The solutions are given as proposals. The proposal is then weighed up with the existing system analytically and the best one is selected. The proposal is presented to the user for endorsement by the user. The proposal is reviewed at the user’s request and suitable changes are made. This is loop that ends as soon as the user is satisfied with the proposal.

Preliminary study is the process of gathering and interpreting facts, using the information for further studies on the system. Preliminary study is problem solving activity that requires intensive communication between the system users and the developers. It does various feasibility studies. In these studies, a rough figure of the system activities can be obtained, from which the decision about the strategies to be followed for effective system study and analysis can be taken.

## 2.2. IDENTIFICATION OF NEED

When problems are identified, it is usually towards the end of the project-in system testing or even conversion. The people who are most active during system development are programmers. This was one reason a great deal of attention has been given to improving the maintainability of programming. However, the problem typically begins during the initial stages of the project. So, there is a need for establishing an overall framework that will lead to successful implementation.

There are several steps to establish a project.

### 2.2.1. Understand the problem:
Use experienced staff rather than trainees for the initial investigations. Each project should be studied to evaluate the degree of change, the scope of the project, and the cost of late completion. Projects that involve a high degree of change and require a close working relationship with user staff normally require only a written objective, a target data and a responsible person. How much management is needed in either project is a decision that involves a delicate balance between risk and cost.

### 2.2.2. Specify project responsibility:
The user executives should sponsor the project and be responsible for the right amount of user involvement. A qualified project manager is the leader responsible for project success. They report directly to the user executive.

### 2.2.3. Selected Project Manager:
Project managers are responsible for the day-to-day activities and for meeting the objectives within the constraints of time, cost and quality. The duties include developing a project task both technical and leadership skills are required.
Technical ability is crucial during the initial (creative) phase of the project whereas leadership is required throughout the life cycle of the project.

## 2.3. PRELIMINARY INVESTIGATION

The preliminary investigation is the process of studying the system request and preparing a recommendation. The purpose of preliminary investigation is to determine if the systems request is worth pursuing into the analysis phase and to perform some initial project management planning tasks.

First, in receiving a system request, the review team must ensure that they fully understand the problem or opportunity. In many cases the system request does not identify the underlying problem. The system request may only identify a possible solution. For example, a system request may state there is a need for creating secured passwords by the users that are difficult for attackers to guess.

Costs of the project also need to be considered in this phase. Typically, little is known about the final costs of the project since many of the critical decisions about hardware; software and implementation have not been made at this point. As part of the economic feasibility analysis the budget of the project was evaluated but exact costs were determined.

Similar to costs a complete schedule of all phases through implementation would be difficult to create for a system project as part of the preliminary investigation. However, a schedule for just the analysis phase should be created during the preliminary investigation.

## 2.4. EXISTING SYSTEM

The current dermatological healthcare system is often fragmented and inefficient. Some key issues in the existing system include:

*   **Lack of Accessibility:** Patients in remote areas struggle to find specialized dermatologists without traveling long distances.
*   **Inefficient Appointment Management:** Manual booking systems lead to long waiting times and scheduling conflicts.
*   **Delayed Diagnosis:** Due to the scarcity of specialists, initial screening of skin conditions is often delayed, potentially aggravating the issue.
*   **Absence of Digital Records:** Most medical history is maintained in physical files, making it difficult to track the progression of skin conditions over time.
*   **Limited Awareness:** Lack of immediate information or preliminary screening tools causes unnecessary anxiety among patients about benign skin issues.

## 2.5. PROPOSED SYSTEM

In the proposed **Dermascan AI** system, Patients, Doctors, and the Admin play key roles in ensuring efficient skin disease diagnosis and connection. Separate registration and login functionalities are provided for each type of user, allowing them to access features relevant to their role.

*   **Patients** can register, upload images of skin lesions for **AI-based analysis**, and receive immediate probability scores for potential conditions. They can browse registered doctors, view availability, book appointments, chat online with doctors for consultations, and provide feedback.
*   **Doctors** manage their professional profiles, set consultation schedules (date/time/fees), and view patient appointments. They can approve or reject appointment requests, chat with patients, and manage their patient history.
*   **The Admin** oversees the overall system, managing user roles, verifying doctor credentials to ensure trust, and monitoring system statistics. The admin can also handle complaints and generate reports to analyze the platform's usage.

## 2.6. FEASIBILITY STUDY

All projects are feasible when given unlimited resources and infinite time. It is both necessary and prudent to evaluate the feasibility of a project at the earliest possible time. An estimate is made of whether the identified user needs may be satisfied using current software and hardware technologies. The study will decide if the proposed system will be cost effective from the business point of view and if it can be developed in the given existing budgetary constraints. The feasibility study should be relatively cheap and quick. The result should inform the decision of whether to go ahead with a more detailed analysis.

The feasibility study is done in these phases.
1.  Operational feasibility
2.  Technical feasibility
3.  Economic feasibility.

### 2.6.1 TECHNICAL FEASIBILITY
Technical feasibility study deals with the hardware as well as software requirements. The scope was whether the work for the project is done with the current equipment and the existing software technology.

Our system requires modern software technologies such as **Python (Django Framework)**, **SQLite/MySQL**, and **TensorFlow/Keras** for AI processing. Since these are all open-source and widely available on standard operating systems (Windows 10/11, Linux), this system is technically feasible.

### 2.6.2 ECONOMIC FEASIBILITY
The purpose of the economic feasibility assessment is to determine the positive economic benefits to the organization that the proposed system will provide.

Our system is economically feasible since it utilizes open-source technologies, minimizing licensing costs. It provides significant value by optimizing doctor-patient connections and providing automated low-cost preliminary screening.

### 2.6.3 OPERATIONAL FEASIBILITY
The purpose of the operational feasibility study is to determine whether the new system will be used if it is developed and implemented.

Our system will operate after it is developed and be operative once it is installed. The system is designed with a user-friendly interface that requires no specific technical training for doctors or patients. Thus, this system is operationally feasible.

## 2.7. PROJECT PLANNING

Project planning is a part of Project management which relates to the use of Schedules such as Gantt charts to plan and subsequently report progress within the project environment. Initially the project scope is defined and the appropriate methods for completing the project are determined. Following this step the duration for the various tasks necessary to complete the work are listed and grouped into a work breakdown structure.

The logical dependencies between tasks are defined using an activity network diagram that enables identification of the theoretical path. Float or slack time in the schedule can be calculated using project management software.

Then the necessary resources can be estimated and costs for each activity can be allocated to each resource giving the total project cost. At this stage, the project schedule may be optimized to achieve the appropriate balance between resource usage and project duration to comply with the project objectives.

Once established and agreed the project schedule become what is known as the baseline schedule. Progress will be measured against the baseline schedule throughout the life of the project. Analyzing progress compared to the baseline schedule is known as earned value management.

---

# 3. METHODOLOGY & SYSTEM REQUIREMENTS

## 3.1. SOFTWARE LIFE CYCLE
The **Iterative Waterfall Model** or **Agile Methodology** is suitable for this project. The phases include:
1.  **Requirement Analysis:** Understanding the need for AI in dermatology.
2.  **System Design:** Designing the database (models) and user interface (views).
3.  **Implementation:** Coding the Django views, templates, and integration of the AI model.
4.  **Testing:** validating the login, upload, and prediction flows.
5.  **Deployment & Maintenance:** Hosting the application and updating the AI model.

## 3.2. HARDWARE REQUIREMENTS
*   **Processor:** Intel Pentium Core i3 and above
*   **RAM:** 8GB RAM and above
*   **Hard Disk:** 320 GB hard disk and above
*   **Keyboard:** Windows compatible
*   **Mouse:** Windows compatible
*   **Monitor:** VGA Color Monitor

## 3.3. SOFTWARE REQUIREMENTS
*   **Operating System:** Windows 8 or above
*   **Front End:** HTML, CSS, JavaScript
*   **Back End:** Python, Django
*   **Database:** SQLite / MySQL
*   **IDE:** VS Code
*   **Web Browser:** Google Chrome

## 3.4. FEATURES OF OPERATING SYSTEM

### WINDOWS 10
Windows 10 is a Microsoft operating system for personal computers, tablets, embedded devices and internet of things devices. Microsoft released Windows 10 in July 2015 as a follow-up to Windows 8. The company has said it will update Windows 10 continuously, rather than release a new, full-fledged operating system as a successor. Anyone adopting Windows 10 can upgrade legacy machines directly from Windows 7 or Windows 8 to Windows 10 without re-imaging or performing intrusive and time-consuming system wipes and upgrade procedures. To upgrade from a previous version of Windows 10, IT or users run the Windows 10 OS installer, which transfers any applications and software on the previous OS, as well as settings and preferences over to Windows 10. Organizations and users can pick and choose how they will patch and update Windows 10. IT or users can access a Windows 10 upgrade through the Windows Update Assistant to manually begin an upgrade or wait for Windows Update to offer an upgrade when it is set to run.

**Configuration Manager:** Windows 10 features built-in capabilities that allow corporate IT departments to use mobile device management system (MDS) software to secure and control devices running the operating system. In addition, organizations can use traditional desktop management software such as Microsoft System Center.

## 3.5. LANGUAGE OVERVIEW

### 3.5.1. PYTHON
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms and can be freely distributed.

**PYTHON’s Strength:**
Python is the language that is used by big brands throughout the whole world. Its demand is increasing day by day. Python is used by Google, Yahoo, Intel, IBM, Cisco, HP, NASA and many more big names in the list. Here we will discuss the various strengths and weaknesses of python.

In comparison to other languages, PYTHON has much strength, including the following:
*   **Performance:** Python is very fast. Python is a powerful and versatile higher-order programming language. Whether you’re developing a web application or working with machine learning, this language has you covered.
*   **Portability:** Portable Python can be installed on any USB storage device, local hard drive or network location.
*   **Extensible:** It is a very major strength of Python. It is developed in a way that allows the addition of new capabilities and functionality. It does let you interface Python with libraries written in other languages.
*   **Ease of learning:** Python may be utilized to rapidly create prototypes owing to its ease of use and readability. Python provides a much more efficient coding experience than languages such as C# and Java.
*   **Strong object-oriented support:** The support of object-oriented programming increases this language’s productivity. These characteristics make it less stressful to create a system and reduce development time.
*   **Interpreted:** Python is interpreted language which means it does not require any kind of compiler to run the program. Python converts its code into bytecode which gives instant results.
*   **GUI programming:** Python provides many solutions to develop a Graphical User Interface (GUI). Python shipped with a toolkit named tkinter which is widely used for GUI developments.

### 3.5.2. SQL DATABASE
Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network (including the Internet).

Structured Query Language (SQL) is a domain-specific language used in programming and designed for managing data held in a relational database management system (RDBMS). SQL consists of a data definition language, data manipulation language, and data control language. The scope of SQL includes data insert, query, update and delete, schema creation and modification, and data access control.

SQL was one of the first commercial languages for Edgar F. Codd's relational model. Despite not entirely adhering to the relational model as described by Codd, it became the most widely used database language. SQL became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987.

### 3.5.3. HTML
HTML stands for Hyper Text Markup Language. It is used to design web pages using a markup language. HTML is a combination of Hypertext and Markup language. Hypertext defines the link between the web pages. A markup language is used to define the text document within tag which defines the structure of web pages.

**HTML has much strength, including the following:**
*   **Easy to learn:** It is simple. If you have zero coding knowledge, but you would like to become some sort of coder or programmer, it is best to learn HTML in the first place.
*   **Low Cost:** HTML is available at no cost under an open-source license or at low cost under a commercial license.
*   **Ease of Use:** HTML allows the style to be as flexible as possible.
*   **Portability:** It is platform independent.
*   **HTML Tags:** Each html tag has its own function to define elements on the page.

---

# 4. SYSTEM DESIGN & DEVELOPMENT

## 4.1. PROJECT DESCRIPTION
This application uses **HTML** as Front End. We use **PYTHON (Django)** at the back-end for processing the data. The aim of the undertaking is to automate the previously manual diagnosis and appointment system by using the assist of computerized gadgets and a complete fledged system, fulfilling their necessities, in order that their valuable facts/data may be stored for a protracted duration with clean gaining access to and manipulation of the same.

## 4.2. DESIGN AND DEVELOPMENT PROCESSES
System design is vital for efficient database management. In the present software, conceptualization of the system involved deciding different tables, forms layout for inputs and reports for output. The database tables are designed by using all the necessary fields in a compact and correct manner. Care should be taken to avoid redundancy and duplication of fields. All input screens are user friendly and designed. In such a way that even a layman can operate it. The size of all screens is standardized. The menu designed in the system are brief, compact and self-explanatory. Any novice can invoice the system. Pop-up menus are used to invoice various submenus.

The major concern of the user in the system is designing a system that is intangible and decision impelling. Their design is created to meet the objectives as time, cost and preciseness in the proposed system no formal application knowledge is not necessary. In this data entry operator can feed the relevant details asked by the system for particular task input. The system will store the data in computer files and can be processed when needed.

The importance of software design can be stated with single word quality. Design is a place where quality is fostered the software development. Design is the only way where the requirements are translated into software products. System developments are a series of operations performed to manipulate data to produce output from a computer system. This depends highly on the programming language use.

The principles activities performed during the development phase can be divided into two major related sequences. They are:
1.  External System Development
2.  Internal System Development

**EXTERNAL SYSTEM DEVELOPMENT**
The major external system development activities are:
1.  Implementation
2.  Planning
3.  Equipment Acquisition
4.  Installation

**INTERNAL SYSTEM DEVELOPMENT**
Internal system developments activities are:
*   Computer Program Development
*   Performance Testing

## 4.3. MODULES

### ADMIN
*   The admin can view complaints and send replies.
*   The admin is the super user of this system.
*   The admin can manage doctors and verify their credentials (approve/reject).
*   The admin can view system statistics (Total Patients, Active Doctors, Appointments).
*   The admin can view complaints and send replies.
*   The admin can analyze appointment reports and doctor performance.
*   The admin can change passwords and ensure system security.

### DOCTOR
*   The doctor can sign up and register within the system.
*   The doctor can view and edit their profile.
*   The doctor can manage their consultation schedule (Date, Time, Fees).
*   The doctor can view appointments and approve/reject them.
*   The doctor can view payment history.
*   The doctor can chat with patients to provide consultations and follow-up advice.
*   The doctor can send complaints regarding operational issues and view replies.

### PATIENT (USER)
*   Patients can sign up and register within the system.
*   Patients can log in to access their respective features.
*   Patients can view and edit their profile information.
*   **AI Scan:** Patients can upload skin images to get immediate AI diagnosis results.
*   Patients can browse registered doctors and view their profiles.
*   Patients can book appointments based on doctor availability.
*   Patients can track previous appointments/scans and view their status.
*   Patients can chat with doctors for online consultations.
*   Patients can provide feedback and ratings for doctors.

## 4.4. TABLE DESIGN
Table design refers to outside the logical data structures that are to be physically stored in the storage device. The design of the table includes decision making on the nature and content of the files such as whether it is to be used for storing master details, transaction details or reference information. Various factors are considered during the table design phase of system analysis.

Some of them are listed below:
*   Purpose of the table
*   Availability of hardware
*   File activity
*   File size
*   Output requirements
*   Input requirements
*   File organization

The table design also deals with the design of physical database. A key field determines how access is to be implemented. Suitable key fields are identified with various tables and are coded approximately. The type, width and size of the fields are identified. Techniques of file organization are suited so that the most appropriate storage device can be selected, and an efficient database design can be achieved. Specifying the data between them identifies the interface between the systems.

### 4.4.1. Database Tables

### Table: auth_user
Built-in Django table for authentication.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | int | - | Primary Key, Auto Increment, Not Null |
| username | varchar | 150 | Unique, Not Null |
| password | varchar | 128 | Not Null |
| email | varchar | 254 | Not Null |
| first_name | varchar | 150 | Not Null |
| last_name | varchar | 150 | Not Null |
| is_superuser | tinyint | 1 | Not Null (Boolean) |
| is_staff | tinyint | 1 | Not Null (Boolean) |
| is_active | tinyint | 1 | Not Null (Boolean) |
| last_login | datetime | 6 | Nullable |
| date_joined | datetime | 6 | Not Null |

### Table: app_user_profile
Stores patient details linked to the main auth_user model.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| name | varchar | 100 | Not Null |
| age | varchar | 100 | Not Null |
| gender | varchar | 100 | Not Null |
| phone | varchar | 100 | Not Null |
| email | varchar | 100 | Not Null |
| address | longtext | - | Not Null |
| status | varchar | 100 | Not Null |
| USER_ID_id | int | - | Unique, Foreign Key, Not Null |

### Table: app_doctor
Stores doctor professional details.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| name | varchar | 100 | Not Null |
| phone | varchar | 100 | Not Null |
| email | varchar | 254 | Not Null |
| address | longtext | - | Not Null |
| status | varchar | 100 | Not Null |
| regno | varchar | 100 | Not Null |
| smc | varchar | 100 | Not Null |
| USER_ID_id | int | - | Unique, Foreign Key, Not Null |

### Table: app_doctor_schedule
Manages doctor availability.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto_Increment, Not Null |
| date | varchar | 100 | Not Null |
| start_time | varchar | 100 | Not Null |
| end_time | varchar | 100 | Not Null |
| fees | varchar | 100 | Not Null |
| max_patients | int | - | Not Null |   
| DOCTOR_ID_id | bigint | - | Foreign Key, Not Null |

### Table: app_booking
Handles appointment transactions.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| date | varchar | 100 | Not Null |
| status | varchar | 100 | Not Null |
| token_number | int | - | Nullable |
| shedule_id_id | bigint | - | Foreign Key, Not Null |
| PATIENT_ID_id | bigint | - | Foreign Key, Not Null |

### Table: app_payment
Tracks payment status for bookings.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| PAYMENT_ID | varchar | 100 | Not Null |
| amount | varchar | 100 | Not Null |
| payment_date | varchar | 100 | Not Null |
| status | varchar | 100 | Not Null |
| BOOKING_ID_id | bigint | - | Foreign Key, Not Null |

### Table: app_complaint
User/Doctor complaints and Admin replies.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| Complaint_text | longtext | - | Not Null |
| Reply | longtext | - | Nullable |
| Date | varchar | 100 | Not Null |
| USER_ID_id | int | - | Foreign Key, Not Null |

### Table: app_feedback
General system feedback.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| Feedback_text | longtext | - | Not Null |
| Date | varchar | 100 | Not Null |
| DOCTOR_ID_id | bigint | - | Foreign Key, Nullable |
| PATIENT_ID_id | bigint | - | Foreign Key, Nullable |

### Table: app_rating
Star ratings and reviews for doctors.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| date | varchar | 100 | Not Null |
| stars | int | - | Not Null |
| review | longtext | - | Not Null, Default 'pending' |
| DOCTOR_ID_id | bigint | - | Foreign Key, Not Null |
| PATIENT_ID_id | bigint | - | Foreign Key, Not Null |

### Table: app_chat
Messages between users.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| message | longtext | - | Nullable |
| timestamp | varchar | 100 | Not Null |
| is_read | tinyint | 1 | Not Null (Boolean) |
| image | varchar | 100 | Nullable |
| SENDER_ID_id | int | - | Foreign Key, Not Null |
| RECIEVER_ID_id | int | - | Foreign Key, Not Null |

### Table: app_skinpredictionhistory
Logs AI usage history.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| image_path | varchar | 500 | Not Null |
| label | varchar | 200 | Not Null |
| confidence | double | - | Not Null |
| created_at | datetime | 6 | Not Null |
| USER_ID_id | int | - | Foreign Key, Not Null |

### Table: app_skinchatmessage
Chat logs with the AI bot.
| Field Name | Data Type | Size | Constraints |
| :--- | :--- | :--- | :--- |
| id | bigint | - | Primary Key, Auto Increment, Not Null |
| role | varchar | 10 | Not Null |
| message | longtext | - | Not Null |
| created_at | datetime | 6 | Not Null |
| USER_ID_id | int | - | Foreign Key, Not Null |

---

# 5. CODING

## 5.1. CODING STANDARDS
The system is developed using standard coding practices to ensure readability, maintainability, and scalability.
*   **Naming Conventions:** Standard Python naming conventions (snake_case for functions/variables, CamelCase for classes) are followed.
*   **Comments:** Inline comments are used to explain complex logic.
*   **Modular Approach:** Features are separated into backend (Django views/models) and frontend (Templates).

## 5.2. FRONTEND DESIGN (BOOTSTRAP)
To ensure a responsive, modern, and consistent user interface across all devices (Mobile, Tablet, Desktop), the project extensively utilizes the **Bootstrap** framework.
*   **Responsive Grid:** Bootstrap's grid system is used to align elements perfectly on different screen sizes.
*   **Components:** Pre-built components like Navigation Bars, Cards, Modals, and Buttons are used to maintain a professional look.
*   **Styling:** Instead of writing extensive custom CSS lines, Bootstrap classes (e.g., `btn-primary`, `card`, `container`) are applied directly to HTML elements. This ensures the code remains clean and the design is uniform.

## 5.3. KEY BACKEND LOGIC (PYTHON/DJANGO)

**Sample 1: Doctor Registration (from `views.py`)**
This function handles the registration of new doctors, saving their credentials and professional details.
```python
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        regno = request.POST['reg_no'] # Medical License
        smc = request.POST['smc'] # State Medical Council
        username = request.POST['username']
        password = request.POST['password']

        # Check existing user
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return redirect('register')

        # Create Django User
        user = User.objects.create_user(username=username, password=password)
        user.groups.add(Group.objects.get(name='doctor'))

        # Create Doctor Profile
        Doctor.objects.create(USER_ID=user, name=name, address=address, email=email, 
                              phone=phone, regno=regno, status='pending', smc=smc)

        messages.success(request, 'Registration successfull')
        return redirect('login_view')

    return render(request,'register.html')
```

**Sample 2: Appointment Booking Logic**
This snippet demonstrates how an appointment is booked and saved to the database.
```python
def user_book_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        schedule_id = request.POST.get('schedule_id')
        date = request.POST.get('date')
        
        # Create Booking
        Booking.objects.create(
            PATIENT_ID=request.user.user_profile,
            shedule_id_id=schedule_id,
            date=date,
            status='Pending'
        )
        messages.success(request, "Appointment Request Sent!")
        return redirect('user_appointments')
```

---

# 6. TESTING

## 6.1. TYPES OF TESTING DONE

### Unit Testing
Individual components were tested to ensure they work as expected.
*   **Models:** Verified that data (Users, Doctors) is correctly saved and retrieved from the database.
*   **Views:** Tested individual views (Login, Register) to ensure they return the correct templates and context.

### Integration Testing
Tested the interaction between different modules.
*   **Booking Flow:** Verified that a booking created by a Patient appears immediately in the Doctor's dashboard.
*   **Admin Verification:** Verified that when an Admin approves a Doctor, the Doctor can subsequently log in.

### System Testing
The complete system was tested as a whole to verify that all requirements are met.
*   **Full Workflow:** From User Registration -> Skin Scan -> Doctor Booking -> Feedback.
*   **Browser Compatibility:** Tested on Google Chrome and Mozilla Firefox.

## 6.2. TEST CASES

| TC ID | Test Description | Input Data | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC_01 | **User Registration** | Valid Name, Email, Password | User created, redirect to Login | User created | **Pass** |
| TC_02 | **Invalid Login** | Wrong Username/Password | Error Message "Invalid Credentials" | Error displayed | **Pass** |
| TC_03 | **Doctor Registration** | Valid License & Details | Doctor Profile created (Pending) | Created (Pending) | **Pass** |
| TC_04 | **Image Upload** | Select Skin Image (JPG/PNG) | Image uploaded, AI Analysis Starts | Analysis Result Shown | **Pass** |
| TC_05 | **Book Appointment** | Select Date & Doctor | Booking Status "Pending" | Saved as Pending | **Pass** |
| TC_06 | **Admin Approval** | Click "Approve" on Doctor | Doctor Status becomes "Approved" | Status Updated | **Pass** |
| TC_07 | **View Schedule** | Select Doctor | Show available slots | Slots Valid | **Pass** |

# 7. FUTURE ENHANCEMENT

Software technology is constantly evolving with new advancements shaping digital solutions. This drives developers to seek innovative approaches for designing and enhancing systems that allow continuous improvements. **Dermascan AI** can be extended to include additional functionalities that further streamline dermatological care and optimize diagnostic efficiency. The system is designed to be adaptable, ensuring it remains relevant even as new technologies emerge.

**Mobile Application Development**
A dedicated mobile application can be developed for all stakeholders, including Patients and Doctors. Patients can take photos of skin lesions directly using their phone camera and get instant analysis on the go. Doctors can manage appointments and view patient history from anywhere. The app can also provide real-time notifications for appointment reminders and medication alerts.

**Advanced AI & Personalization**
Artificial Intelligence and Machine Learning can be further incorporated to predict skin disease progression and offer personalized skincare recommendations. By analyzing historical data and user skin types, the system can suggest preventive measures and routine care products, transforming the platform from a diagnostic tool into a holistic skin health companion.

**Telemedicine & Video Consultation**
The system can integrate with real-time video conferencing tools to provide live virtual consultations. This would allow doctors to examine patients remotely in real-time, bridging the gap between digital analysis and physical examination, especially for patients in remote areas.

**Blockchain for Medical Records**
Blockchain technology can be integrated to enhance the security and privacy of sensitive patient data. Each diagnosis and medical record can be stored in a decentralized, immutable ledger, ensuring that patient data is tamper-proof and only accessible to authorized medical professionals, thereby increasing trust in the system.

By incorporating these enhancements, **Dermascan AI** can increase its diagnostic accuracy, strengthen patient trust, and create a more robust and scalable solution for addressing global skin health challenges.

---

# 8. CONCLUSION

The project **“Dermascan AI”** which has been developed to overcome the drawbacks of existing system that incorporates all the facilities to fulfil requirements identified during the analysis phase in the development of the project. The Web Application was validated for accuracy and the results are satisfactory. The users can rely on the Web Application since it offers the feature of expandability according to the forthcoming changes. The Web Application proved to be more user-friendly and flexible for the users since it eliminates the tiring task of continuous manual work. This provides a high degree of convenience and ease for the **patients and doctors**. Thus, the new features come out with numerous time benefits and productivity. Each task is divided into modules. The new modules developed can be easily linked to the Web Application.

---

# 9. BIBLIOGRAPHY

## BOOKS
*   **PYTHON:** E.Balaguruswamy, *Introduction to Computing and Problem Solving Using Python*
*   **PYTHON:** Richard L.Halterman, *Learning To Program With Python*
*   **PYTHON:** Martin C.Brown, *Python: The Complete Reference*
*   *Introducing HTML5* – Bruce Lawson & Remy Sharp
*   *HTML5 Black Book* – Dream Tech Press, 2016 Edition

## WEBSITES
*   [https://www.python.org/](https://www.python.org/)
*   [www.w3schools.com › python](https://www.w3schools.com/python/)
*   [www.pythonforbeginners.com](https://www.pythonforbeginners.com/)
*   [www.djangoproject.com](https://www.djangoproject.com/)
*   [https://www.w3schools.com/](https://www.w3schools.com/)
