# Python Project: PNG to Scalable SVG Converter

This project is a Python application that processes a low-resolution PNG image and generates a scalable SVG version. The SVG file is resolution-independent and can be used as a high-quality wallpaper or for other scalable applications.

---

## **Quick Start**

### **How to Use the Project**
Follow these steps to use and validate the project:

1. **Clone the Repository**  
   Clone the project to your local machine:
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2.Install Dependencies
Install required dependencies using poetry:
```bash poetry install

3.Ensure your input PNG file (screenshot.png) is placed in the project directory.

4.Run the Python Script
Process the input image and generate the SVG file:
```bash python -m checkio1.image_conversion

5.Run Tests
Validate the project functionality using pytest:
```bash poetry run pytest

6.Check Code Quality
Run pylint to analyze the code and improve its quality:
```bash poetry run pylint checkio1/

7.Generate Documentation
Generate project documentation using Sphinx:
```bash sphinx-apidoc -o docs/source/ checkio1
cd docs
make html

