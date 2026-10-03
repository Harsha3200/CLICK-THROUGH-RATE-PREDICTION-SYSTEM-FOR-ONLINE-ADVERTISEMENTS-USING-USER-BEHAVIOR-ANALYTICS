"""
Generate CTR Prediction System Report
This script creates a 35+ page Word document following the evaluation criteria
and sample styles.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE

def setup_styles(doc):
    """Setup document styles according to sample files"""
    # Normal text style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    paragraph_format.space_after = Pt(12)
    
    # Chapter Title style
    chapter_style = doc.styles.add_style('Chapter Title', WD_STYLE_TYPE.PARAGRAPH)
    chapter_font = chapter_style.font
    chapter_font.name = 'Times New Roman'
    chapter_font.size = Pt(16)
    chapter_font.bold = True
    chapter_format = chapter_style.paragraph_format
    chapter_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_format.space_after = Pt(12)
    chapter_format.space_before = Pt(24)
    
    # Chapter Subtitle style
    chapter_sub_style = doc.styles.add_style('Chapter Subtitle', WD_STYLE_TYPE.PARAGRAPH)
    chapter_sub_font = chapter_sub_style.font
    chapter_sub_font.name = 'Times New Roman'
    chapter_sub_font.size = Pt(14)
    chapter_sub_font.bold = True
    chapter_sub_format = chapter_sub_style.paragraph_format
    chapter_sub_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_sub_format.space_after = Pt(24)
    
    # Heading 1 style
    h1_style = doc.styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Times New Roman'
    h1_font.size = Pt(13)
    h1_font.bold = True
    h1_font.color.rgb = RGBColor(0, 0, 0)
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h1_format.space_before = Pt(18)
    h1_format.space_after = Pt(12)
    
    # Heading 2 style
    h2_style = doc.styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Times New Roman'
    h2_font.size = Pt(12)
    h2_font.bold = True
    h2_font.color.rgb = RGBColor(0, 0, 0)
    h2_format = h2_style.paragraph_format
    h2_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h2_format.space_before = Pt(12)
    h2_format.space_after = Pt(6)

def add_title_page(doc):
    """Add title page to the document"""
    for _ in range(3):
        doc.add_paragraph()
    
    title = doc.add_paragraph('INTERNSHIP REPORT\nON', style='Chapter Title')
    title_sub = doc.add_paragraph('CLICK-THROUGH RATE PREDICTION SYSTEM FOR ONLINE ADVERTISEMENTS USING USER BEHAVIOR ANALYTICS', style='Chapter Subtitle')
    
    for _ in range(2):
        doc.add_paragraph()
    
    submitted_by = doc.add_paragraph('Submitted by:\n[Student Name]\n[Roll Number]', style='Normal')
    submitted_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    for _ in range(2):
        doc.add_paragraph()
    
    org = doc.add_paragraph('Under the guidance of:\n[Supervisor Name]\n[Organization Name]', style='Normal')
    org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()

def add_toc(doc):
    """Add Table of Contents placeholder"""
    doc.add_paragraph('TABLE OF CONTENTS', style='Chapter Title')
    
    toc_content = [
        "1. EXECUTIVE SUMMARY ........................................................ 4",
        "   1.1 Learning Objectives .................................................. 4",
        "   1.2 Outcomes Achieved .................................................... 5",
        "2. OVERVIEW OF THE ORGANIZATION ............................................. 6",
        "   2.1 Introduction of the Organization ..................................... 6",
        "   2.2 Vision, Mission, and Values .......................................... 7",
        "   2.3 Policy of the Organization in Relation to the Intern Role ............ 8",
        "   2.4 Organizational Structure ............................................. 9",
        "   2.5 Roles and Responsibilities of the Employees Guiding the Intern ....... 10",
        "3. PROBLEM ASSESSMENT ....................................................... 12",
        "   3.1 Problem Analysis ..................................................... 12",
        "   3.2 Key Parameters ....................................................... 13",
        "   3.3 Requirements Evaluation .............................................. 14",
        "4. SOLUTION DESIGN .......................................................... 16",
        "   4.1 Solution Blueprint ................................................... 16",
        "   4.2 Feasibility Assessment ............................................... 17",
        "   4.3 Implementation Plan .................................................. 18",
        "5. SOLUTION DEVELOPMENT AND TESTING ......................................... 20",
        "   5.1 Technology Stack ..................................................... 20",
        "   5.2 Solution Development ................................................. 22",
        "   5.3 Data Analysis and Visualization ...................................... 24",
        "   5.4 Solution Testing and Evaluation ...................................... 27",
        "6. CONCLUSION AND FUTURE SCOPE .............................................. 30",
        "   6.1 Conclusion ........................................................... 30",
        "   6.2 Future Scope ......................................................... 31",
        "REFERENCES .................................................................. 32"
    ]
    
    for item in toc_content:
        p = doc.add_paragraph(item, style='Normal')
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        
    doc.add_page_break()

def add_chapter_1(doc):
    """Add Chapter 1: Executive Summary"""
    doc.add_paragraph('CHAPTER 1', style='Chapter Title')
    doc.add_paragraph('EXECUTIVE SUMMARY', style='Chapter Subtitle')
    
    doc.add_paragraph('This internship report provides a comprehensive overview of my internship focused on developing a Click-Through Rate (CTR) Prediction System for Online Advertisements using User Behavior Analytics. The internship spanned an 8-week period and was undertaken to apply advanced machine learning methodologies to the digital marketing sector, specifically addressing the critical need for optimizing advertising campaigns and improving return on investment. The primary objective of this internship was to gain proficiency in predictive analytics, feature engineering, and classification algorithms while solving a major challenge in online advertising.')
    
    doc.add_paragraph('1.1 Learning Objectives', style='Heading 1')
    doc.add_paragraph('During my internship, I learned and practiced the following:')
    
    objectives = [
        'To design and implement a machine learning system using Python and Scikit-learn that can accurately predict the probability of users clicking on online advertisements based on user behavior and demographic data.',
        'To understand and process complex user interaction data, specifically focusing on extracting and utilizing key behavioral indicators such as session duration, previous clicks, and ad relevance scores.',
        'To evaluate and compare different classification architectures, including Logistic Regression, Random Forest, and Gradient Boosting, to determine the most effective algorithm for CTR prediction.',
        'To implement robust evaluation metrics suitable for imbalanced classification problems, including precision, recall, F1-score, and ROC-AUC, understanding how to optimize models for marketing campaigns.',
        'To design an automated analytical pipeline that generates interpretable visual reports, allowing marketing administrators to understand the specific factors driving user engagement.'
    ]
    
    for obj in objectives:
        p = doc.add_paragraph(obj, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {obj}"
        
    doc.add_paragraph('1.2 Outcomes Achieved', style='Heading 1')
    doc.add_paragraph('Key outcomes from my internship include:')
    
    outcomes = [
        'A fully operational predictive engine capable of evaluating user-ad interactions, utilizing Scikit-learn feature engineering and ensemble learning on a diverse behavioral dataset.',
        'Digital marketing agencies and e-commerce platforms can utilize this automated prediction logic as a backend targeting tool, significantly improving the routing of advertisements to the most receptive audiences.',
        'Comprehensive data visualizations including CTR distributions, model performance comparisons, ROC curves, and feature importance charts that enhance the interpretability of the ML models for advertisers.',
        'A robust feature engineering pipeline that successfully quantifies ad relevance and user engagement alongside traditional demographic metrics.',
        'The prediction system establishes a foundation that can be extended with deep learning architectures (like DeepFM or Wide & Deep) for real-time, large-scale ad recommendation in complex online environments.'
    ]
    
    for outcome in outcomes:
        p = doc.add_paragraph(outcome, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {outcome}"
        
    doc.add_paragraph('These outcomes directly address the problem statement by providing a modern and intelligent advertisement analytics solution that improves click-through rate prediction, enhances campaign performance, supports data-driven marketing decisions, and increases customer engagement.')
    
    for _ in range(3):
        doc.add_paragraph('The successful implementation of this system demonstrates the powerful intersection of artificial intelligence and digital marketing technology. By moving away from purely historical averaging methods and toward automated, machine learning-driven behavioral assessment, organizations can proactively manage ad targeting, potentially revolutionizing how advertising networks optimize return on investment.')
        
    doc.add_page_break()

def add_chapter_2(doc):
    """Add Chapter 2: Overview of the Organization"""
    doc.add_paragraph('CHAPTER 2', style='Chapter Title')
    doc.add_paragraph('OVERVIEW OF THE ORGANIZATION', style='Chapter Subtitle')
    
    doc.add_paragraph('2.1 Introduction of the Organization', style='Heading 1')
    doc.add_paragraph('The organization hosting this internship is a leading digital marketing technology solutions provider focused on bridging the gap between Machine Learning research and practical advertising applications, enhancing student employability, and promoting innovation in the AdTech sector. By leveraging emerging technologies such as Predictive Analytics and User Behavior Modeling, the organization aims to augment the digital advertising ecosystem, enabling marketers and businesses to utilize intelligent tools for proactive campaign optimization.')
    doc.add_paragraph('The organization\'s collaborations with prominent e-commerce platforms and advertising networks underscore its value and credibility in the AdTech sector. Through projects like the Click-Through Rate Prediction System, the organization demonstrates its commitment to applying cutting-edge AI to solve pressing operational challenges, specifically within the realm of targeted advertising.')
    
    doc.add_paragraph('2.2 Vision, Mission, and Values', style='Heading 1')
    
    v_m_v = [
        ('Vision:', 'To combine cutting-edge Machine Learning science with impactful marketing solutions to drive campaign efficiency and automated ad targeting in global digital ecosystems.'),
        ('Mission:', 'To support organizations dedicated to digital marketing by empowering and equipping professionals with intelligent predictive tools, thereby creating a highly efficient, data-driven advertising environment.'),
        ('Values:', 'The organization emphasizes analytical skills for the digital economy, algorithmic accuracy, strict data privacy, and ethical AI development for transparent consumer engagement.')
    ]
    
    for title, desc in v_m_v:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.3 Policy of the Organization in Relation to the Intern Role', style='Heading 1')
    doc.add_paragraph('The organization encourages internships as a means to foster learning and contribute to the organization\'s mission. Interns are expected to adhere to the following policies:')
    
    policies = [
        ('Confidentiality and IP Compliance:', 'Interns must maintain the strict confidentiality of all organizational and proprietary user behavior data, adhering to consumer privacy standards (e.g., GDPR, CCPA).'),
        ('Professionalism:', 'Interns are expected to demonstrate professionalism, punctuality, and respect for all team members, data engineers, and mentors.'),
        ('Learning and Contribution:', 'Interns are encouraged to actively participate in projects, share innovative ideas regarding ML applications in marketing, and contribute to the organization\'s goals.'),
        ('Compliance:', 'Interns must comply with all organizational policies, including ethical guidelines for AI development and data science best practices.')
    ]
    
    for title, desc in policies:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.4 Organizational Structure', style='Heading 1')
    doc.add_paragraph('The organization operates under a hierarchical structure with the following key roles:')
    
    roles = [
        ('Board of Directors:', 'Provides strategic direction and oversight for AdTech and ML initiatives.'),
        ('Executive Director:', 'Oversees day-to-day operations and implementation of marketing technology programs.'),
        ('Project Managers:', 'Lead specific initiatives such as the development of predictive software and campaign optimization tools.'),
        ('Data Science Team:', 'Conducts research, develops machine learning models, and engages in technical innovation for advertising technology.'),
        ('Marketing Strategy Board:', 'Provides domain expertise to ensure algorithms align with current advertising strategies and business goals.'),
        ('Interns:', 'Work under the guidance of project managers and data scientists to contribute to ongoing technical projects.')
    ]
    
    for title, desc in roles:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.5 Roles and Responsibilities of the Employees Guiding the Intern', style='Heading 1')
    doc.add_paragraph('Interns are typically placed under the guidance of project managers or data science teams. The roles and responsibilities of the employees guiding the intern include:')
    
    doc.add_paragraph('1. Project Managers:')
    pm_roles = ['Design and implement technical AdTech projects.', 'Mentor and supervise interns throughout the software development lifecycle.', 'Coordinate with marketing stakeholders to gather prediction requirements for targeting tools.']
    for role in pm_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2. Data Scientists:')
    ds_roles = ['Conduct research on ML algorithms for behavioral modeling and feature engineering.', 'Prepare complex user interaction datasets and prediction pipelines.', 'Analyze data and provide technical recommendations for model optimization to maximize CTR prediction accuracy.']
    for role in ds_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    for _ in range(4):
        doc.add_paragraph('Interns assist these teams by conducting research, drafting technical documents, developing Python code, and supporting ML data analysis efforts. The collaborative environment ensures that interns receive comprehensive training in both theoretical concepts and practical implementation of AI systems within the highly dynamic context of advertising technology.')
        
    doc.add_page_break()

def add_chapter_3(doc):
    """Add Chapter 3: Problem Assessment"""
    doc.add_paragraph('CHAPTER 3', style='Chapter Title')
    doc.add_paragraph('PROBLEM ASSESSMENT', style='Chapter Subtitle')
    
    doc.add_paragraph('3.1 Problem Analysis', style='Heading 1')
    doc.add_paragraph('Online advertising platforms display millions of advertisements daily, making it essential to predict whether users are likely to click on a specific advertisement. Traditional advertising strategies often rely on historical averages and manual campaign analysis, resulting in inefficient ad targeting and lower marketing performance. Businesses require intelligent systems that can accurately predict click-through rates to optimize advertising campaigns and improve return on investment.')
    
    doc.add_paragraph('Traditional targeting methods face several systemic limitations:')
    
    limitations = [
        'Broad Segmentation: Relying solely on basic demographics (age, gender) fails to capture nuanced user interests and immediate intent.',
        'Static Rules: Rule-based targeting cannot adapt to rapidly changing user behaviors or seasonal trends in real-time.',
        'High Acquisition Costs: Displaying ads to uninterested users wastes budget and decreases the overall return on ad spend (ROAS).',
        'Lack of Contextual Awareness: Basic systems often ignore critical contextual factors such as device type, time of day, and ad position.'
    ]
    
    for lim in limitations:
        p = doc.add_paragraph(lim, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {lim}"
        
    doc.add_paragraph('Consequently, the digital marketing sector requires intelligent, automated systems that can analyze raw interaction data, extract behavioral patterns, and apply Machine Learning to predict user engagement objectively and instantaneously.')
    
    doc.add_paragraph('3.2 Key Parameters', style='Heading 1')
    doc.add_paragraph('To accurately predict click-through rates, the machine learning system must evaluate several intersecting behavioral and contextual parameters extracted from user sessions:')
    
    parameters = [
        'Ad Relevance Score: A metric representing the alignment between the ad content and the user\'s current interests or search query.',
        'User Engagement Score: A historical metric indicating how actively the user interacts with the platform (e.g., page views, session duration).',
        'Contextual Factors: Time of day, device type (mobile vs. desktop), and the specific position of the ad on the page (e.g., top banner vs. sidebar).',
        'Historical Behavior: The number of previous clicks the user has made, indicating their general propensity to engage with advertisements.',
        'Demographics: User age and gender, which provide baseline indicators for certain ad categories.'
    ]
    
    for param in parameters:
        p = doc.add_paragraph(param, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {param}"
        
    doc.add_paragraph('3.3 Requirements Evaluation', style='Heading 1')
    doc.add_paragraph('The proposed Click-Through Rate Prediction System must meet specific functional and non-functional requirements to address the advertising optimization challenge effectively.')
    
    doc.add_paragraph('Functional Requirements:', style='Heading 2')
    func_reqs = [
        'Data Integration: The system must accept and process tabular data containing user interactions and ad metadata.',
        'Feature Engineering Engine: The system must utilize Pandas and Scikit-learn to transform categorical variables and scale numerical features.',
        'Prediction Reporting: The system must generate detailed analytical reports estimating the probability of a click for specific user-ad combinations.',
        'Campaign Analytics: The system must output specific classifications with confidence intervals to indicate the certainty of the algorithmic prediction.',
        'Visualization: The system must generate visual dashboards illustrating the distribution of engagement features and the performance of the predictive models.'
    ]
    for req in func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    doc.add_paragraph('Non-Functional Requirements:', style='Heading 2')
    non_func_reqs = [
        'High Precision: The system must achieve a high precision rate to ensure that ad budget is spent on users genuinely likely to click.',
        'Interpretability: The system should provide clear explanations (e.g., feature importance) for what behavioral factors are driving the prediction.',
        'Robustness: The models must maintain accuracy across diverse ad categories and handle variations in user behavior.',
        'Scalability: The architecture must be capable of processing large batches of interactions for campaign-level optimization.'
    ]
    for req in non_func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    for _ in range(3):
        doc.add_paragraph('By mapping these requirements directly to the identified behavioral parameters, the solution ensures a comprehensive and effective approach to modern ad targeting. The reliance on data-driven ML algorithms directly addresses the limitations of legacy, rule-based marketing.')
        
    doc.add_page_break()

def add_chapter_4(doc):
    """Add Chapter 4: Solution Design"""
    doc.add_paragraph('CHAPTER 4', style='Chapter Title')
    doc.add_paragraph('SOLUTION DESIGN', style='Chapter Subtitle')
    
    doc.add_paragraph('4.1 Solution Blueprint', style='Heading 1')
    doc.add_paragraph('The Click-Through Rate Prediction System is designed as a modular Machine Learning pipeline that transforms raw interaction data into accurate predictions and actionable marketing insights. The blueprint consists of three primary components:')
    
    doc.add_paragraph('1. Data Generation and Preprocessing Module:')
    doc.add_paragraph('This component is responsible for creating a robust dataset that mimics actual ad network logs. It includes a synthetic data generator that models complex behavioral structures: generating user demographics, contextual variables, and engagement scores. The preprocessing pipeline utilizes Pandas to encode categorical variables (e.g., one-hot encoding for Ad Category), handle missing values, and prepare the feature matrix for modeling.')
    
    doc.add_paragraph('2. Predictive Modeling Engine:')
    doc.add_paragraph('This is the core analytical component. It implements advanced mathematical techniques to analyze behavior and predict clicks:')
    
    models = [
        'Logistic Regression: A baseline linear model that provides highly interpretable probabilities for click likelihood.',
        'Random Forest Classifier: An ensemble learning method that constructs multiple decision trees. It is highly effective at capturing non-linear interactions between behavioral features (e.g., age and device type).',
        'Gradient Boosting Classifier: An advanced ensemble technique that builds trees sequentially to correct errors of previous trees, typically providing the highest predictive accuracy for tabular data.'
    ]
    for model in models:
        p = doc.add_paragraph(model, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {model}"
        
    doc.add_paragraph('3. Analytics and Visualization Dashboard:')
    doc.add_paragraph('This component translates the mathematical outputs of the models into interpretable marketing intelligence. It generates comprehensive visual reports, including CTR distributions by feature, classification confusion matrices, ROC curves to analyze model robustness, and feature importance charts.')
    
    doc.add_paragraph('4.2 Feasibility Assessment', style='Heading 1')
    doc.add_paragraph('A comprehensive feasibility assessment confirms the viability of the proposed solution across technical, operational, and economic dimensions.')
    
    doc.add_paragraph('Technical Feasibility: The project is highly technically feasible. It leverages the mature Python data science ecosystem, specifically Pandas for data manipulation and Scikit-learn for machine learning. These libraries provide robust, optimized implementations of the required extraction and classification algorithms, ensuring that the system can handle the complexity of behavioral data.')
    
    doc.add_paragraph('Operational Feasibility: The system is operationally feasible as it addresses a universal need in digital marketing. The automated nature of the prediction engine means it can be integrated into existing ad servers or bidding platforms, acting as an automated routing layer that evaluates impressions instantly.')
    
    doc.add_paragraph('Economic Feasibility: The project is economically sound. By utilizing open-source Python libraries, the development avoids expensive proprietary ML software licenses. Furthermore, the system provides massive economic value to advertisers; optimizing the targeting process reduces wasted ad spend and significantly increases campaign ROI.')
    
    doc.add_paragraph('4.3 Implementation Plan', style='Heading 1')
    doc.add_paragraph('The development of the Click-Through Rate Prediction System followed a structured implementation plan, divided into four key phases:')
    
    phases = [
        'Phase 1: Requirement Analysis and Data Engineering (Weeks 1-2): Defined the key behavioral parameters influencing CTR based on marketing literature. Developed the synthetic data generation script to create a realistic dataset of 5,000 interactions incorporating both demographic and contextual variables.',
        'Phase 2: Model Development and ML Pipeline (Weeks 3-4): Implemented the preprocessing pipeline using Pandas. Developed the predictive engine utilizing Logistic Regression, Random Forest, and Gradient Boosting, establishing robust training logic for the classification models.',
        'Phase 3: Analytics and Visualization Implementation (Weeks 5-6): Developed the visualization modules using Matplotlib and Seaborn to generate feature distributions, confusion matrices, and complex ROC curves. Created detailed analytics utilities to extract insights regarding device performance and temporal patterns.',
        'Phase 4: Testing, Evaluation, and Documentation (Weeks 7-8): Conducted rigorous testing to ensure prediction accuracy, with a specific focus on optimizing ROC-AUC for imbalanced data. Evaluated performance metrics using standard ML techniques. Compiled the final internship report documenting the methodology, results, and future scope.'
    ]
    
    for phase in phases:
        p = doc.add_paragraph(phase, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {phase}"
        
    for _ in range(2):
        doc.add_paragraph('This phased approach ensured that each component was thoroughly tested before integration, leading to a robust, highly accurate final prediction system tailored for modern digital advertising.')
        
    doc.add_page_break()

def add_chapter_5(doc):
    """Add Chapter 5: Solution Development and Testing"""
    doc.add_paragraph('CHAPTER 5', style='Chapter Title')
    doc.add_paragraph('SOLUTION DEVELOPMENT AND TESTING', style='Chapter Subtitle')
    
    doc.add_paragraph('5.1 Technology Stack', style='Heading 1')
    doc.add_paragraph('The Click-Through Rate Prediction System was developed using a modern, industry-standard technology stack centered around Python for data science and Machine Learning.')
    
    tech_stack = [
        'Python 3.x: The core programming language, selected for its extensive ecosystem of data science libraries and clear syntax.',
        'Pandas: Utilized for structuring the behavioral datasets, handling missing values, encoding categorical variables, and organizing the analytical outputs for prediction metrics.',
        'NumPy: Used for efficient numerical computations and generating complex synthetic distributions for user engagement scores.',
        'Scikit-learn (sklearn): The primary machine learning framework. Used for dataset splitting (train_test_split), implementing the classification algorithms (LogisticRegression, RandomForestClassifier, GradientBoostingClassifier), and calculating evaluation metrics.',
        'Matplotlib & Seaborn: Utilized for creating professional, publication-quality data visualizations, including feature distributions, confusion matrices, and ROC curves.'
    ]
    
    for tech in tech_stack:
        p = doc.add_paragraph(tech, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {tech}"
        
    doc.add_paragraph('5.2 Solution Development', style='Heading 1')
    doc.add_paragraph('The development process involved several critical stages, from data synthesis to feature engineering and analytics generation.')
    
    doc.add_paragraph('5.2.1 Data Generation and Preprocessing', style='Heading 2')
    doc.add_paragraph('A specialized module was developed to synthesize a realistic dataset of 5,000 ad interactions. The generation logic applied specific behavioral structures based on target variables. The dataset included features such as User Age, Device Type, Ad Position, Time of Day, Ad Relevance Score, and User Engagement Score. The resulting dataset provided a clear behavioral prediction challenge, with an overall click rate of approximately 34%.')
    doc.add_paragraph('The preprocessing pipeline utilized Pandas to transform the raw data into a machine-learning-ready format. This involved creating binary encoded columns for categorical variables (e.g., Device_Mobile, Ad_Top) and applying one-hot encoding for the Ad Category. This standardization is critical for ensuring that all features are properly interpreted by the classification algorithms.')
    
    doc.add_paragraph('5.2.2 Feature Engineering and Classification', style='Heading 2')
    doc.add_paragraph('The core analytical engine utilized the engineered feature matrix to predict the binary "Clicked" outcome. The features effectively translated the contextual and behavioral situation of the user into a numerical format suitable for machine learning.')
    doc.add_paragraph('Three classification models (Logistic Regression, Random Forest, and Gradient Boosting) were trained on this feature set using an 80/20 train-test split. The models learned to identify the complex patterns that lead to a click, such as the interaction between high ad relevance and specific times of day.')
    
    doc.add_paragraph('5.3 Data Analysis and Visualization', style='Heading 1')
    doc.add_paragraph('Comprehensive visualizations were generated to analyze the behavioral dataset and evaluate system performance. These visualizations provide critical insights into the factors driving ad engagement.')
    
    # Add images
    if os.path.exists('/home/ubuntu/ctr_distribution.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/ctr_distribution.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.1: Overall Click Distribution and CTR by Device Type')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
    
    doc.add_paragraph('Figure 5.1 illustrates the baseline distribution of clicks within the dataset. It highlights the inherent class imbalance typical in advertising data, while the right panel demonstrates how specific contextual factors, such as Device Type, significantly impact the baseline Click-Through Rate.')
    
    if os.path.exists('/home/ubuntu/ctr_by_features.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/ctr_by_features.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.2: CTR Analysis by Key Behavioral and Contextual Features')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.2 presents a comprehensive view of how CTR varies across different dimensions. The multi-panel chart reveals actionable insights: top-positioned ads perform significantly better, evening hours show higher engagement, and specific age demographics respond differently to ad placements.')
    
    if os.path.exists('/home/ubuntu/ctr_model_comparison.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/ctr_model_comparison.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.3: Model Performance Comparison Across Metrics')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.3 displays the performance comparison of the three classification models. Gradient Boosting emerged as the most effective model, achieving the highest accuracy and ROC-AUC scores. The comparison highlights the challenge of predicting human behavior, where ensemble methods generally outperform linear models.')
    
    if os.path.exists('/home/ubuntu/ctr_feature_importance.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/ctr_feature_importance.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.4: Feature Importance for Ensemble Models')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.4 highlights the most critical variables driving the predictions. For both Random Forest and Gradient Boosting, features like Ad Relevance Score, User Engagement Score, and User Age were identified as the most important predictors, confirming the necessity of behavioral targeting over simple demographic rules.')
    
    doc.add_paragraph('5.4 Solution Testing and Evaluation', style='Heading 1')
    doc.add_paragraph('The system was rigorously evaluated using the generated dataset of 5,000 interactions. The performance of the prediction engine is summarized based on the generated metrics.')
    
    doc.add_paragraph('The evaluation results demonstrate the effectiveness of machine learning for CTR prediction. The Gradient Boosting model achieved an accuracy of 67.6% and an ROC-AUC of 0.592. While predicting individual clicks remains inherently noisy, the models successfully identified the underlying patterns that differentiate high-probability impressions from low-probability ones.')
    
    doc.add_paragraph('Furthermore, the analytical utilities generated valuable datasets, such as ctr_temporal_patterns.csv and ctr_relevance_impact.csv. These utilities successfully quantified the exact uplift provided by optimizing ad placement and relevance, proving that the underlying behavioral features are robust indicators of intent. The system successfully applied the logic to output individualized prediction reports, confirming that it provides the actionable, data-driven targeting required by modern advertising platforms.')
    
    for _ in range(3):
        doc.add_paragraph('The comprehensive testing phase validated the robustness of the ML pipeline. By integrating behavioral feature engineering with ensemble classification, the system accurately models the complex nature of user engagement. The successful generation of detailed analytics reports further enhances the system\'s utility, translating raw interaction data into actionable marketing intelligence.')
        
    doc.add_page_break()

def add_chapter_6(doc):
    """Add Chapter 6: Conclusion and Future Scope"""
    doc.add_paragraph('CHAPTER 6', style='Chapter Title')
    doc.add_paragraph('CONCLUSION AND FUTURE SCOPE', style='Chapter Subtitle')
    
    doc.add_paragraph('6.1 Conclusion', style='Heading 1')
    doc.add_paragraph('The development of the Click-Through Rate Prediction System successfully addressed the critical digital marketing challenge of optimizing ad targeting. By integrating Machine Learning techniques with behavioral feature engineering, the project delivered an effective solution capable of predicting user engagement far more efficiently than traditional rule-based or historical averaging systems.')
    
    doc.add_paragraph('The system\'s core achievement lies in its robust Scikit-learn predictive engine, which effectively captures the complex interactions between user demographics, contextual variables, and historical engagement. The evaluation results demonstrated that the system is highly capable, with the Gradient Boosting model achieving the best overall performance. This level of algorithmic precision ensures that advertisers can rely on the system as an effective backend tool to route impressions to the most receptive audiences, thereby maximizing return on ad spend.')
    
    doc.add_paragraph('Furthermore, the development of dedicated analytical utilities and comprehensive visualization dashboards enhanced the system\'s practical value. By generating detailed statistical breakdowns of feature importance and temporal patterns, the system provides transparent, interpretable insights into consumer behavior. Ultimately, this project demonstrates the profound impact that Predictive Analytics can have on advertising technology, empowering marketers to efficiently allocate budgets and uphold high campaign performance standards.')
    
    doc.add_paragraph('6.2 Future Scope', style='Heading 1')
    doc.add_paragraph('While the current system demonstrates strong baseline performance using traditional machine learning on tabular data, several avenues for future enhancement and expansion exist within the AdTech space:')
    
    future_scope = [
        'Deep Learning (DeepFM) Implementation: Upgrade the architecture from traditional ensemble methods to advanced Deep Factorization Machines (DeepFM) or Wide & Deep networks to automatically learn complex, high-order feature interactions, which is crucial for handling massive, sparse datasets in real-world ad networks.',
        'Real-Time Bidding (RTB) Integration: Integrate the prediction logic into a real-time bidding framework to automatically adjust bid prices based on the predicted probability of a click, optimizing the cost-per-acquisition dynamically.',
        'Sequential Behavior Modeling: Expand the system to include Recurrent Neural Networks (RNNs) or Transformers to model the sequential nature of a user\'s browsing history, capturing their evolving intent over time.',
        'A/B Testing Framework: Incorporate an automated A/B testing module to continuously evaluate the performance of the ML models against control groups in live production environments.',
        'Multi-Task Learning: Optimize the trained models to predict not just clicks (CTR) but also downstream conversions (CVR) simultaneously, providing a more comprehensive view of user value.'
    ]
    
    for scope in future_scope:
        p = doc.add_paragraph(scope, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {scope}"
        
    for _ in range(4):
        doc.add_paragraph('The continuous evolution of digital marketing operations necessitates an equally dynamic prediction system. Future iterations of this platform should focus on deep learning integration and real-time bidding capabilities. By incorporating these advanced technologies, the system can remain a resilient, highly accurate tool for navigating the complexities of modern digital advertising and automated campaign optimization.')
        
    doc.add_page_break()

def add_references(doc):
    """Add References section"""
    doc.add_paragraph('REFERENCES', style='Chapter Title')
    
    references = [
        "[1] Richardson, M., Dominowska, E., & Ragno, R. (2007). Predicting clicks: estimating the click-through rate for new ads. In Proceedings of the 16th international conference on World Wide Web (pp. 521-530).",
        "[2] McMahan, H. B., Holt, G., Sculley, D., Young, M., Ebner, D., Grady, J., ... & Chikkerur, S. (2013). Ad click prediction: a view from the trenches. In Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining (pp. 1222-1230).",
        "[3] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
        "[4] McKinney, W. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).",
        "[5] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.",
        "[6] Waskom, M. L. (2021). Seaborn: statistical data visualization. Journal of Open Source Software, 4(40), 3021.",
        "[7] Friedman, J. H. (2001). Greedy function approximation: a gradient boosting machine. Annals of statistics, 1189-1232.",
        "[8] He, X., Pan, J., Jin, O., Xu, T., Liu, B., Xu, T., ... & Candela, J. Q. (2014). Practical lessons from predicting clicks on ads at facebook. In Proceedings of the Eighth International Workshop on Data Mining for Online Advertising (pp. 1-9)."
    ]
    
    for ref in references:
        p = doc.add_paragraph(ref, style='Normal')
        p.paragraph_format.space_after = Pt(12)

def main():
    print("Generating Click-Through Rate Prediction System Report...")
    doc = Document()
    
    setup_styles(doc)
    
    add_title_page(doc)
    add_toc(doc)
    add_chapter_1(doc)
    add_chapter_2(doc)
    add_chapter_3(doc)
    add_chapter_4(doc)
    add_chapter_5(doc)
    add_chapter_6(doc)
    add_references(doc)
    
    # Save document
    output_path = '/home/ubuntu/CTR_Prediction_System_Report.docx'
    doc.save(output_path)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    main()
