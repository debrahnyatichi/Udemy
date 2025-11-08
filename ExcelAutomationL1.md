**Excel Automation Lesson 1**

**Introduction to Excel Automation with Python**

Excel Automation: Using code to automatically create, edit, format or analyze excel files instead of doing manually

**Examples:**
1. Generating monthly reports automatically
2. Cleaning and transforming large datasets
3. Creating charts and pivot tables programaticaly
4. Repetitive data entry tasks

**Benefits of Python for Excel tasks**
1. **Efficiency**:handle thousands of rows in seconds
2. **Reproductivity**: code can be reused for multiple files
3. **Intergration**: works well with databases, APIs and other file formats
4. **Advanced analysis**: use python libraries(NumPy, pandas, matplotlib) for analytics/visualization
5. **Cross-platform**: works on windows,mac and linux

**Commonly Used Libraries for Excel Automation**
1. **openpyxl:** Read/write Excel `.xlsx` files, formatting, and charts  
2. **pandas:** Data analysis; powerful for reading/writing Excel using dataframes  
3. **xlsxwriter:** Create new Excel files with advanced formatting and charts  
4. **pywin32:** (Windows-only) Controls Excel via COM automation (useful for Excel macros)

**Guideline:**
- Use `pandas` for data manipulation  
- Use `openpyxl` or `xlsxwriter` for styling and formatting  
- Use `pywin32` only if you need to control the actual Excel application (like clicking buttons)  

**Setting Up a Python Environment( with vscode and venv)**
STEP 1: create a project folder
mkdir automation
cd automation

STEP 2: Create a virtual Environment
python -m venv (venv or any name you want; in my case i used auto)

STEP 3: Activate venv
windows powershell: auto/Scripts/activate
Mac/linux: source auto/bin/activate

STEP 4: 
**Install the libraries**
pip install openpyxl pandas xlsxwriter pywin32
**Check Installations**
pip list

**Quick Demo**
create.py: creating a simple excel table using pandas
read.py: reading an excel file
