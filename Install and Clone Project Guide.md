**Step-by-Step Guide to Clone and Set Up a Project from GitHub**

---

### **1. Install Required Dependencies**

Run the following commands to install necessary dependencies:

```
pip install playwright
playwright install chromium
pip install pytest-playwright
pip install allure-pytest allure-python-commons
playwright install
```

---

### **2. Clone the Project from GitHub**

1. **Create a New Folder** where you want to store the project.
2. **Open Git Bash** inside the folder.
3. **Clone the repository** using the command:

```
git clone https://github.com/Xav-Pavan/Fuel_iX_CX_Automation.git
```

4. **Navigate into the cloned project directory**:

```
cd Fuel_iX_CX_Automation
```

---

### **3. Create and Switch to Your Own Branch**

5. **Create a new branch** for your modifications:

```
git branch new-branch-name  # Replace with your branch name
```

Example:

```
git branch Pavan_QA
```

6. **Switch to your new branch**:

```
git checkout new-branch-name
```

Example:

```
git checkout Pavan_QA
```

---

### **4. Open and Modify the Project**

7. **Open the project in PyCharm** or any preferred code editor.
8. **Make your changes** (update, delete, or add files).

---

### **5. Stage and Commit Changes**

9. **Stage specific files** (if you modified only some files):

```
git add filename
```

Example:

```
git add Fuel_iX_CX/pages/login_page.py
```

10. **Stage all modified files** (if you made multiple changes):

```
git add *
```

11. **Commit your changes with a meaningful message**:

```
git commit -m "Updated login page"
```

---

### **6. Push Your Changes to GitHub**

**(Only required once) Set up GitHub remote URL:**

```
git remote set-url origin https://Xav-Pavan:{token}@github.com/Xav-Pavan/Fuel_iX_CX_Automation.git
```

**Push your branch to GitHub:**

```
git push --set-upstream origin new-branch-name
```

Example:

```
git push --set-upstream origin Pavan_QA
```

---

### **7. Switching Back to the Master Branch**

If you need to switch back to the master branch:

```
git checkout master
```

---

✅ **Now your project is successfully cloned, modified, and pushed to GitHub!** 🚀

