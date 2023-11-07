Project "Automation the 21vek website"

🔸 This project is an automated framework for working with the "21vek" website using the Python programming language and the Selenium framework.

🔸 Installation and launch of the project    
    1. Clone the repository to your computer - git clone https://github.com/Alesyya/python_test_project.git.
    2. Install the dependencies specified in the requirements.txt file using the pip install -r requirements.txt command.    
    3. Set up environment variables to access the 21st Century site.
    4. Run the Makefile using the command - make test_chrome.    
    5. Start allure - allure serve report/ 

🔸 Project structure
    - data - data about users.    
    - elements - auxiliary functions and classes for the header and footer.
    - helpers - auxiliary functions and classes for the project as a whole.    
    - pages - classes that describe various pages of the "21st century" website.
    - tests - a set of automated tests.    
    - conftest.py - file with project settings.
    - README.md - current file containing information about the project.    
    - Makefile - for running tests.
    - Dockerfile - to create a container image.

🔸 The architecture of the automated framework is based on the Page Object approach. Each page of the "21vek" website is represented by a separate class that contains methods for interacting with page elements.

🔸 When developing the project, I followed the PEP8 recommendations for coding style, naming variables, functions and files. The structure and organization of project folders and files was also observed for ease of work and navigation.

🔸 The project was created using the Git version control system. All development was carried out in a separate branch, after which the branch was merged into the main branch. The history of changes and commits is available in the project repository.

🔸 The project implements automated tests that cover the main functionality of the "21vek" website. The tests were developed taking into account test design techniques and techniques to achieve the greatest efficiency and reliability of testing.

🔸 To make it easier to track testing results and analyze errors during the framework’s operation, the project has implemented a reporting and logging system. It allows you to generate reports on passed tests, as well as record information about errors and exceptions.

🔸 The project provides a Dockerfile for easy installation and running of the project in a Docker container. This allows you to create isolated and portable environments for developing and testing your project.

Author:
- Alesya Lukashevich - automation qa engineer (python).

Contacts:
✉️ Email: Lukasheviich03@gmail.com
📞 Phone: +375 (33) 602-97-00