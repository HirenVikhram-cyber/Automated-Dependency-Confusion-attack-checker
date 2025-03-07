# **Automated Dependency Checker**  

This script automates the process of extracting `requirements.txt` files from multiple GitHub organizations, checking package availability on PyPI, and identifying non-existent dependencies.

## **🚀 How It Works**  
The script performs the following steps:  
1. **Extracts `requirements.txt` file URLs** from multiple GitHub organizations.  
2. **Converts GitHub links** to raw URLs for direct file access.  
3. **Downloads `requirements.txt` files** from repositories.  
4. **Extracts package names**, removing unwanted characters and version constraints.  
5. **Checks if the packages exist** on PyPI.  
6. **Lists non-existent packages** in `non_existent_packages.txt`.  
7. **Cross-checks non-existent packages** with `requirements.txt` files.  
8. **Generates a final report** of missing dependencies.  

---

## **📌 Prerequisites**  
Before running the script, ensure you have:  
- **Python 3.11+** installed  
- **GitHub API Token** (Replace `TOKEN` in `scripter3.py`)  
- **`requests` and `PyGithub` Python modules** installed  
- ** org.txt (List your org names in this file)


## **📌 Excecution:**

Run the Dependency_confusion_check.sh Script and place the github org in org.txt
