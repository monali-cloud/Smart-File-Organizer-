# Smart-File-Organizer-
A real-world Python automation project that automatically organizes files in a folder into structured categories such as Images, Videos, Documents, Music, Archives, Programs, and Others. This project is designed to improve productivity, reduce manual file management, and demonstrate practical Python automation skills.

##🎯 Project Objective

The goal of this project is to build a smart automation system that:

Scans a target folder

Identifies file types

Creates category folders automatically

Moves files into appropriate folders

Handles duplicate filenames safely

This simulates real-world automation used in operating systems, cloud storage systems, and enterprise file management software.

🧠 Key Features

📂 Automatic file categorization

🧠 Smart file-type detection

📁 Auto folder creation

🔁 Duplicate file handling

⚙ Modular code structure

🖥 Cross-platform support (Windows, Linux, macOS)

🧩 Easily extensible system

##🏗 Project Structure
smart_file_organizer/
│
├── organizer.py # Main execution file
├── config.py # File category configuration
├── utils.py # Utility/helper functions
└── README.md # Project documentation

##⚙ How It Works

User provides a folder path

System scans all files

File extensions are detected

Files are matched with predefined categories

Category folders are created automatically

Files are moved to respective folders

Unknown file types go to Others folder

##▶ How To Run

python organizer.py

Enter folder path in this format:
C:/Users/Monali/Downloads

##🧪 Example Output

📂 Organizing: C:/Users/Monali/Downloads


✅ photo.jpg → Images
✅ resume.pdf → Documents
✅ song.mp3 → Music
📦 unknown.xyz → Others


🎉 Organization complete!


##🛠 Technologies Used

Python 3

OS Module

Path Handling

File System Automation

Modular Programming Design

##🚀 Future Enhancements

GUI Interface (Tkinter)

AI-based file classification

Date-wise sorting

File size-based organization

Cloud sync integration

Scheduler automation

Logging system

Undo/Restore feature

##📌 Learning Outcomes

File handling in Python

OS-level automation

Modular coding

Clean architecture

Automation scripting

Real-world problem solving

CLI tool development

##👩‍💻 Author

Monali Nagardhankar
Python Developer | Automation Enthusiast | AI Learner

##⭐ If you like this project, consider adding it to your GitHub portfolio and improving it with advanced features!
