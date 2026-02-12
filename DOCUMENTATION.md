# University Admissions Chatbot - Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Technology Stack](#technology-stack)
5. [Project Structure](#project-structure)
6. [Installation & Setup](#installation--setup)
7. [Usage Guide](#usage-guide)
8. [Module Documentation](#module-documentation)
9. [Data Format](#data-format)
10. [Features Explanation](#features-explanation)
11. [Future Enhancements](#future-enhancements)
12. [Contributing Guidelines](#contributing-guidelines)

---

## Project Overview

### What is the University Admissions Bot?

The **University Admissions Bot** is an intelligent, conversational AI-powered chatbot designed to help students quickly understand university admission requirements. Instead of reading lengthy, complex documentation, students can interact with the bot in natural language to get concise, easy-to-understand responses about:

- Admission eligibility criteria
- Required documents
- Application deadlines
- Program-specific requirements

### Purpose

The primary goal of this project is to:
- **Simplify** complex admission requirements into digestible information
- **Accelerate** student decision-making by providing instant responses
- **Reduce** barriers to entry by making admission information more accessible
- **Improve** user experience through conversational interaction

### Target Users

- High school and undergraduate students planning to apply for graduate programs
- Students needing quick access to admission information
- International students seeking clarity on requirements
- Career-switching professionals evaluating programs

---

## Features

### 1. **Admission Eligibility Checking**
Users can ask about eligibility criteria for various programs. The bot recognizes program aliases and returns relevant eligibility information instantly.

**Supported Programs:**
- **MS Computer Science** - Aliases: `cse`, `cs`, `computer science`
- **MBA** - Aliases: `mba`

**Example Query:** "Am I eligible for CSE?"

### 2. **Document Requirement Summaries**
The bot provides a comprehensive list of documents required for each program, eliminating confusion about what to prepare.

**Included Documents:**
- Academic Transcripts
- Statement of Purpose
- Letters of Recommendation
- Resume
- Test Scores (GRE/GMAT)
- English Proficiency Test Scores

### 3. **Application Deadline Information**
Users receive accurate application deadline dates for different programs, helping them plan their timeline effectively.

**Current Deadlines:**
- MS Computer Science: December 15
- MBA: January 10

### 4. **Conversational Interface**
Built on **Streamlit**, the interface provides an intuitive, chat-like experience with emoji indicators and formatted responses.

**Features:**
- Clean, centered layout
- Real-time message display
- Session-based chat history
- Formatted responses with visual cues

### 5. **Quick Eligibility Checker**
An interactive sidebar tool specifically for MS Computer Science that allows students to input their GPA and degree background for instant eligibility feedback.

**Parameters:**
- GPA: 0.0 - 4.0 scale
- Degree: Computer Science / Related Field / Other

---

## Architecture

### System Design

```
┌─────────────────────────────────────────┐
│        Streamlit UI (app.py)            │
│  ┌───────────────────────────────────┐  │
│  │  Chat Interface                   │  │
│  │  - Input Field                    │  │
│  │  - Chat History Display           │  │
│  │  - Eligibility Checker            │  │
│  └───────────────────────────────────┘  │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
    ┌───▼────────┐    ┌──────▼──────┐
    │  Chatbot   │    │ Data Loader │
    │ (chatbot.  │    │ (data_      │
    │   py)      │    │  loader.py) │
    └────┬───────┘    └──────┬──────┘
         │                    │
         │            ┌───────▼────────┐
         │            │  JSON Data     │
         │            │ (admissions_   │
         │            │  data.json)    │
         │            └────────────────┘
         │
    ┌────▼──────────────┐
    │  Support Modules  │
    │ ┌────────────────┐│
    │ │ compressor.py  ││
    │ │ memory.py      ││
    │ └────────────────┘│
    └────────────────────┘
```

### Data Flow

1. **User Input** → Streamlit Interface
2. **Query Processing** → Chatbot Module (pattern matching)
3. **Data Retrieval** → Data Loader (JSON access)
4. **Response Generation** → Formatted output
5. **History Management** → Session state storage

---

## Technology Stack

### Core Technologies

| Component | Technology | Version |
|-----------|-----------|---------|
| **Frontend Framework** | Streamlit | Latest |
| **Programming Language** | Python | 3.8+ |
| **Data Storage** | JSON | Native |
| **UI Styling** | CSS/HTML** | Streamlit Built-in |

### Key Libraries

- **streamlit**: Web application framework for creating interactive UIs
- **json**: Built-in library for data parsing and handling

### Why These Technologies?

- **Streamlit**: Rapid prototyping, minimal code required, excellent for chatbot interfaces
- **Python**: Rich ecosystem, easy to extend, beginner-friendly
- **JSON**: Lightweight, human-readable, perfect for small-to-medium datasets

---

## Project Structure

```
admission-chatbot/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project introduction
├── DOCUMENTATION.md            # This file
│
├── data/
│   └── admissions_data.json    # Program admission information
│
├── docs/
│   └── project_documentation.md # Additional documentation
│
└── src/
    ├── __pycache__/           # Python cache files
    ├── chatbot.py             # Core chatbot logic
    ├── compressor.py          # Information compression utility
    ├── data_loader.py         # JSON data loading
    └── memory.py              # Conversation history management
```

### File Descriptions

#### **app.py** (Main Application)
- Entry point for the Streamlit application
- Manages UI layout and components
- Handles chat history and session state
- Integrates all modules

#### **src/chatbot.py**
- Core logic for processing user queries
- Program alias recognition
- Response generation with formatted output

#### **src/data_loader.py**
- Loads admission data from JSON file
- Simple, reusable data access layer

#### **src/compressor.py**
- Utility for creating concise summaries
- Compresses verbose program information

#### **src/memory.py**
- Manages conversation history
- Stores recent messages for context

#### **data/admissions_data.json**
- Centralized data store for program information
- Contains eligibility, documents, and deadlines

---

## Installation & Setup

### Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Virtual Environment** (recommended)

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Darsh-18/Chatbot-Admissions.git
cd admission-chatbot
```

#### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
```

#### 3. Activate Virtual Environment

**On Linux/macOS:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

**Current Dependencies:**
- streamlit

To see all installed packages:
```bash
pip list
```

#### 5. Verify Installation
```bash
python --version
streamlit --version
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Command not found: streamlit | Ensure virtual environment is activated |
| Module not found errors | Run `pip install -r requirements.txt` again |
| Port 8501 already in use | Use `streamlit run app.py --logger.level=debug --server.port 8502` |
| JSON file not found | Verify `data/admissions_data.json` exists |

---

## Usage Guide

### For End Users (Students)

#### Basic Chat Interaction

1. **Ask about a program:**
   ```
   "Tell me about MS Computer Science"
   "What's the eligibility for CSE?"
   "What documents do I need for MBA?"
   ```

2. **Get deadline information:**
   ```
   "When's the deadline for Computer Science?"
   "CS application deadline?"
   ```

3. **Quick eligibility check:**
   - Navigate to the "Quick Eligibility Check" section
   - Enter your GPA (0.0-4.0)
   - Select your bachelor's degree type
   - Click "Check Eligibility"

#### Understanding Bot Responses

The bot returns formatted responses with:
- 🎓 Program title
- ✅ Eligibility criteria
- 📄 Required documents list
- ⏰ Application deadline
- 💡 Suggested follow-up questions

#### Chat History

- All messages appear in chronological order
- Labeled with sender (You/Bot)
- Easy visual distinction with emojis
- Session persists until page refresh

### For Developers

#### Understanding the Codebase

1. **Query Flow:**
   - User enters text in Streamlit input field
   - `get_response()` function processes the query
   - Function searches for program aliases
   - Returns formatted response from JSON data

2. **Adding New Programs:**

   a. Update `data/admissions_data.json`:
   ```json
   "MS Data Science": {
       "eligibility": "Bachelor's in relevant field, GPA 3.2+",
       "documents": [...],
       "deadline": "November 30"
   }
   ```

   b. Update `src/chatbot.py` aliases:
   ```python
   PROGRAM_ALIASES = {
       ...
       "data science": "MS Data Science",
       "ds": "MS Data Science"
   }
   ```

3. **Modifying UI:**
   - Edit `app.py` to change layout
   - Streamlit components refresh automatically
   - CSS can be added via `st.markdown()` with unsafe_allow_html

#### Code Examples

**Example: Processing a Query**
```python
from src.data_loader import load_admission_data
from src.chatbot import get_response

# Load data
data = load_admission_data("data/admissions_data.json")

# Process query
response = get_response("Tell me about CSE", data)
print(response)
```

**Example: Accessing Raw Data**
```python
from src.data_loader import load_admission_data

data = load_admission_data("data/admissions_data.json")

# Get specific program
cs_program = data["MS Computer Science"]
print(cs_program["eligibility"])
print(cs_program["deadline"])
```

---

## Module Documentation

### chatbot.py

**Purpose:** Core chatbot logic for understanding and responding to queries

**Key Components:**

```python
PROGRAM_ALIASES = {
    "cse": "MS Computer Science",
    "computer science": "MS Computer Science",
    "cs": "MS Computer Science",
    "mba": "MBA"
}
```
Maps user-friendly aliases to official program names.

**Function: `get_response(user_query, admission_data)`**

| Parameter | Type | Description |
|-----------|------|-------------|
| `user_query` | string | Raw user input from chat |
| `admission_data` | dict | Loaded JSON data |
| **Returns** | string | Formatted response |

**Logic Flow:**
1. Convert query to lowercase
2. Search for matching program alias
3. If no match found, return error message
4. Retrieve program data
5. Format and return structured response

**Response Format:**
```
🎓 **Program Name – Admission Overview**

✅ **Eligibility:**  
[Eligibility text]

📄 **Required Documents:**  
[Document list]

⏰ **Application Deadline:**  
[Deadline date]

💡 *You can also ask:*  
[Suggested follow-up questions]
```

### data_loader.py

**Purpose:** Simple JSON data loading utility

**Function: `load_admission_data(file_path)`**

| Parameter | Type | Description |
|-----------|------|-------------|
| `file_path` | string | Path to JSON file |
| **Returns** | dict | Parsed JSON data |

**Usage:**
```python
data = load_admission_data("data/admissions_data.json")
```

### compressor.py

**Purpose:** Compress verbose program information into summaries

**Function: `compress_program_info(program_data)`**

| Parameter | Type | Description |
|-----------|------|-------------|
| `program_data` | dict | Program information dictionary |
| **Returns** | string | Compressed summary |

**Output Format:**
```
Eligibility: [Eligibility text]
Deadline: [Date]
Documents Required: [Comma-separated list]
```

### memory.py

**Purpose:** Manage conversation history for context

**Class: `ConversationMemory`**

**Methods:**

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `__init__()` | None | None | Initialize empty history |
| `add_message(message)` | message: str | None | Add message to history |
| `get_history()` | None | list | Get last 5 messages |

**Usage:**
```python
memory = ConversationMemory()
memory.add_message("User: Tell me about CSE")
history = memory.get_history()
```

---

## Data Format

### admissions_data.json Structure

```json
{
  "Program Name": {
    "eligibility": "String describing eligibility criteria",
    "documents": ["Document 1", "Document 2", ...],
    "deadline": "Date in any readable format"
  }
}
```

### Current Data

**MS Computer Science**
- **Eligibility:** Bachelor's degree in CS or related field, minimum GPA 3.0
- **Documents:** Academic Transcripts, Statement of Purpose, Letters of Recommendation, Resume, English Proficiency Test Scores
- **Deadline:** December 15

**MBA**
- **Eligibility:** Bachelor's degree in any discipline, minimum GPA 2.8
- **Documents:** Academic Transcripts, Statement of Purpose, Letters of Recommendation, Resume, GMAT Score
- **Deadline:** January 10

### Adding New Programs

1. Add entry to JSON:
```json
"MS Data Science": {
  "eligibility": "Bachelor's in Math, Statistics, CS or related field with GPA 3.2+",
  "documents": [
    "Academic Transcripts",
    "Statement of Purpose",
    "Letters of Recommendation",
    "Resume",
    "GRE Scores"
  ],
  "deadline": "November 30"
}
```

2. Update aliases in `src/chatbot.py`:
```python
"data science": "MS Data Science",
"ds": "MS Data Science"
```

---

## Features Explanation

### 1. Conversational Query Processing

**How It Works:**
- Searches user query (case-insensitive) for known program aliases
- Returns specific information if program found
- Provides helpful error message if program not recognized

**Supported Queries:**
- "Tell me about MS Computer Science"
- "What's required for CSE?"
- "Can I apply for computer science?"
- "MBA requirements?"
- "cs deadline?"

### 2. Program Alias System

**Why Aliases?**
- Users may not know official program names
- Different search terms should work
- Improves user experience and discoverability

**Alias Mapping:**
```
cse, cs, computer science → MS Computer Science
mba → MBA
```

**Extensibility:**
Add new aliases in `PROGRAM_ALIASES` dictionary for:
- Different spellings
- Abbreviations
- Program variations

### 3. Streamlit Session State

**What It Does:**
- Maintains chat history across interactions
- Preserves conversation context
- Resets on page refresh

**Implementation:**
```python
if "chat" not in st.session_state:
    st.session_state.chat = []
```

### 4. Eligibility Checker Widget

**Interactive Components:**
- GPA slider (0.0-4.0, 0.1 increments)
- Degree dropdown selector
- Check button trigger

**Logic:**
- Checks GPA >= 3.0
- Verifies degree type != "Other"
- Shows success/error message

**Current Criteria:**
```
Eligible IF:
  GPA >= 3.0 AND 
  Degree in ["Computer Science", "Related Field"]
```

### 5. Responsive UI Design

**Features:**
- Centered layout for focus
- Dark input field styling
- Emoji indicators (🎓, ✅, 📄, ⏰, 💡)
- Clear sender labels (🧑 You / 🤖 Bot)
- Visual dividers for sections
- Responsive to different screen sizes

---

## Future Enhancements

### Short-term Improvements

1. **Enhanced Query Understanding**
   - Implement NLP for context-aware responses
   - Handle multi-part questions
   - Support follow-up questions

2. **Expanded Program Database**
   - Add more graduate programs
   - Include undergraduate programs
   - Add international program variants

3. **Advanced Eligibility Checker**
   - Accept more criteria (GMAT, GRE scores)
   - Calculate admission probability
   - Personalized recommendations

4. **User Preferences**
   - Save favorite programs
   - Track application progress
   - Notification system

### Medium-term Features

1. **Multi-language Support**
   - Translate bot responses
   - Support for international students
   - RTL language support

2. **Document Upload & Review**
   - Preview required documents
   - Checklist for application
   - Document quality feedback

3. **Deadline Alerts**
   - Email notifications
   - Calendar integration
   - Smart reminders

4. **Analytics Dashboard**
   - Track popular programs
   - User behavior analysis
   - Improve response quality

### Long-term Vision

1. **AI-Powered Personalization**
   - ML models for recommendation
   - Custom eligibility assessment
   - Career path suggestions

2. **Application Portal Integration**
   - Direct application submission
   - Document management system
   - Status tracking

3. **Institutional Dashboard**
   - For universities to manage data
   - Real-time requirement updates
   - Application statistics

4. **Mobile Application**
   - Native iOS/Android apps
   - Offline functionality
   - Push notifications

---

## Contributing Guidelines

### How to Contribute

#### 1. Fork the Repository
```bash
git clone https://github.com/yourusername/Chatbot-Admissions.git
```

#### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

#### 3. Make Changes

**Code Style:**
- Follow PEP 8 conventions
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

**Example Contribution Structure:**
```python
def new_feature(parameter):
    """
    Brief description of what this does.
    
    Args:
        parameter: Description of parameter
    
    Returns:
        Return value description
    """
    # Implementation
    return result
```

#### 4. Test Your Changes
```bash
# Test the application manually
streamlit run app.py

# Test specific modules
python -m pytest tests/
```

#### 5. Commit Changes
```bash
git add .
git commit -m "Clear description of changes"
```

#### 6. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

### Reporting Issues

**When reporting bugs, include:**
- Clear description of the issue
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, Streamlit version)

**Example:**
```
Title: Bot crashes when special characters in query

Description: When I type "What's required?", the bot crashes with KeyError

Steps to Reproduce:
1. Open app.py
2. Type: What's required?
3. Press Enter

Expected: Bot should handle apostrophes
Actual: Application crashes

Environment: Python 3.9, Streamlit 1.28, Linux Ubuntu 20.04
```

### Requesting Features

**Feature Request Template:**
```
Title: [Feature] Brief description

Description: 
What should this feature do?

Use Case:
Why would users need this?

Proposed Implementation:
How might this be implemented?
```

---

## Appendix

### Frequently Asked Questions

**Q: Can I customize the admission data for my university?**
A: Yes! Edit `data/admissions_data.json` and update the program information with your university's requirements.

**Q: How do I add support for more programs?**
A: 
1. Add program entry to JSON
2. Add aliases to `PROGRAM_ALIASES` in `src/chatbot.py`
3. Test the new program

**Q: Can I deploy this as a web service?**
A: Yes! Use Streamlit Cloud, Heroku, or any Python hosting service.

**Q: Is there a database option instead of JSON?**
A: Yes! You can modify `data_loader.py` to connect to SQLite, PostgreSQL, or MongoDB.

**Q: How do I add authentication?**
A: Streamlit provides built-in authentication features via `streamlit-authenticator` library.

### Performance Optimization Tips

- Cache loaded data using Streamlit's `@st.cache_data` decorator
- Implement rate limiting for API-based expansion
- Use lazy loading for large program databases
- Optimize JSON for faster parsing

### Security Considerations

- Validate all user inputs
- Sanitize data in JSON files
- Don't store sensitive information
- Use environment variables for configuration
- Regular security audits

### Resources & References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Official Docs](https://docs.python.org/3/)
- [JSON Specification](https://www.json.org/)
- [GitHub Repository](https://github.com/Darsh-18/Chatbot-Admissions)

---

## Summary

The **University Admissions Bot** is a practical, educational project that demonstrates:
- Clean Python code organization
- Interactive UI development with Streamlit
- JSON-based data management
- Conversational AI basics
- Software engineering best practices

It serves as a strong foundation for building more advanced chatbots and can be extended with sophisticated NLP, databases, and ML models. Whether you're a student learning web development or building a real admissions tool, this project provides a solid starting point.

---

**Last Updated:** February 12, 2026  
**Version:** 1.0.0  
**Author:** Darsh Ramoliya  
**Repository:** [GitHub Link](https://github.com/Darsh-18/Chatbot-Admissions)
