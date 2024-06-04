import subprocess

# Function to run terminal commands
def run_command(command):
    subprocess.run(command, shell=True, check=True)

# Update package lists and upgrade installed packages
def update_system():
    print("Updating package lists and upgrading installed packages...")
    run_command("sudo apt update -y")
    run_command("sudo apt upgrade -y")

# Install essential packages
def install_essentials():
    print("Installing essential packages...")
    packages = [
        "build-essential",      # Build tools
        "python3-dev",          # Python development headers
        "python3-pip",          # Python package installer
        "git",                  # Version control system
        "curl",                 # Data transfer tool
        "wget",                 # Non-interactive network downloader
        "tmux",                 # Terminal multiplexer
        "vim",                  # Text editor
        "htop",                 # Interactive process viewer
        "gcc",                  # GNU Compiler Collection
        "g++",                  # GNU C++ Compiler
        "make",                 # Build automation tool
        "cmake",                # Cross-platform build system
        "openssh-server",       # SSH server
        "tree",                 # Display directory tree
        "jq",                   # Command-line JSON processor
        "net-tools",            # Networking utilities
        "iputils-ping",         # Network testing tools
        "dnsutils",             # DNS utilities
        "nmap",                 # Network exploration tool and security scanner
        "wireshark",            # Network protocol analyzer
        "tcpdump",              # Network traffic capture tool
        "hydra",                # Password cracking tool
        "john",                 # Password cracking tool
        "sqlmap",               # SQL injection tool
        "nikto",                # Web server vulnerability scanner
        "gdb",                  # GNU Debugger
        "strace",               # System call tracer
        "ltrace",               # Library call tracer
        "radare2",              # Reverse engineering framework
        "binutils",             # Binary utilities (e.g., objdump)
        "ruby",                 # Programming language
        "perl",                 # Programming language
        "php",                  # Programming language
        "default-jdk",          # Default Java Development Kit
        "default-jre",          # Default Java Runtime Environment
        "nodejs",               # JavaScript runtime
        "npm",                  # Node.js package manager
        "golang-go",            # Go programming language
        "rustc",                # Rust programming language
        "lua5.3",               # Lua programming language
        "ruby-dev",             # Ruby development headers
        "perl-doc",             # Perl documentation
        "php-cli",              # PHP command line interpreter
        "openjdk-11-jdk",       # OpenJDK 11 JDK
        "openjdk-11-jre",       # OpenJDK 11 JRE
        "nodejs-doc",           # Node.js documentation
        "golang-doc",           # Go documentation
        "rust-doc",             # Rust documentation
        "lua5.3-doc",           # Lua documentation
        # Add more packages as needed
    ]
    for package in packages:
        run_command(f"sudo apt install -y {package}")

    # Update pip
    print("Updating pip...")
    run_command("python3 -m pip install --upgrade pip")

    # Install Python packages using pip
    install_python_packages()

# Function to install Python packages
def install_python_packages():
    print("Installing Python packages...")
    python_packages = [
        # Data Science and Machine Learning
        "numpy",                # Numerical computing library
        "pandas",               # Data analysis library
        "matplotlib",           # Plotting library
        "seaborn",              # Statistical data visualization
        "scipy",                # Scientific computing library
        "scikit-learn",         # Machine learning library
        "statsmodels",          # Statistical modeling library
        "tensorflow",           # Deep learning framework
        "keras",                # Deep learning framework
        "pytorch",              # Deep learning framework
        "xgboost",              # Gradient boosting library
        "lightgbm",             # Gradient boosting library
        "catboost",             # Gradient boosting library
        "nltk",                 # Natural Language Toolkit
        "spacy",                # NLP library
        "gensim",               # Topic modeling library
        "fasttext",             # Library for fast text representation and classification
        "transformers",         # State-of-the-art natural language processing for TensorFlow 2.x and PyTorch
        "opencv-python",        # OpenCV (computer vision library)
        "dlib",                 # Machine learning library for image processing
        "imutils",              # Utility functions for image and video processing

        # Web Development
        "flask",                # Web framework
        "django",               # Web framework
        "fastapi",              # Fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints
        "tornado",              # Web framework and asynchronous networking library
        "aiohttp",              # Asynchronous HTTP client/server framework
        "beautifulsoup4",       # HTML parsing library
        "requests",             # HTTP library
        "httpx",                # The next generation HTTP client for Python
        "scrapy",               # Web scraping framework
        "selenium",             # Web browser automation

        # DevOps and Automation
        "ansible",              # Configuration management, deployment, and task automation
        "fabric",               # Library for streamlining SSH for application deployment or systems administration tasks
        "docker",               # Python client for Docker API
        "kubernetes",           # Python client for Kubernetes API
        "paramiko",             # SSH library for Python
        "invoke",               # Pythonic task execution tool & library

        # Utilities
        "virtualenv",           # Virtual environments
        "pipenv",               # Dependency management tool
        "pyinstaller",          # Converts Python programs into stand-alone executables
        "click",                # Command-line interface creation kit
        "pytest",               # Testing framework
        "unittest",             # Unit testing framework
        "tox",                  # Virtual environment management and testing tool
        "fabric",               # Library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.
        "pylint",               # Python code analysis tool

        # Databases
        "sqlalchemy",           # SQL toolkit and Object-Relational Mapper
        "pymysql",              # MySQL database adapter for Python
        "psycopg2",             # PostgreSQL database adapter for Python
        "mongoengine",          # Object-Document Mapper for MongoDB
        "redis",                # Python client for Redis key-value store

        # Security
        "pycryptodome",         # Cryptographic library for Python
        "paramiko",             # SSH library for Python
        "tqdm",                 # Progress bar library

        # GUI Development
        "tkinter",              # Python's de-facto standard GUI (Graphical User Interface) package

        # AI and Machine Learning
        "opencv-python",        # OpenCV (computer vision library)
        "pillow",               # Python Imaging Library (PIL)
        "pyqt5",                # Python bindings for Qt5 application framework
        "pyqtgraph",            # Scientific Graphics and GUI Library

        # Miscellaneous
        "pyyaml",               # YAML parser and emitter for Python
        "docutils",             # Documentation utilities for Python projects
        "openpyxl",             # Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files
        "xlrd",                 # Library for developers to extract data from Microsoft Excel spreadsheet files
        "xlsxwriter",           # Python module for creating Excel XLSX files
        "pyodbc",               # ODBC interface for Python

        # Continuous Integration and Deployment
        "jenkins",              # Jenkins automation server package

        # Networking
        "pyshark",              # Python wrapper for tshark, allowing python packet parsing using wireshark dissectors
        "sockets",              # Python's socket interface

        # Social Media APIs
        "tweepy",               # Python library for accessing the Twitter API
        "facebook-sdk",         # Python library for Facebook Graph API

        # PDF and Document Manipulation
        "pyPDF2",               # PDF toolkit

        # Plotting Libraries
        "plotly",               # Interactive plotting library
        "bokeh",                # Interactive visualization library for modern web browsers

        # GIS and Mapping
        "geopandas",            # Geographic data manipulation library
        "folium",               # Python wrapper for Leaflet.js maps library

        # Web Scraping
        "scrapy",               # Web scraping framework

        # Time Series Analysis
        "statsmodels",          # Statistical models in Python

        # Game Development
        "pygame",               # Cross-platform set of Python modules designed for writing video games

        # Computer Vision
        "opencv-python",        # OpenCV (computer vision library)
        "scikit-image",         # Image processing in Python
    ]

    for package in python_packages:
        run_command(f"python3 -m pip install {package}")

# Configure git
def configure_git():
    print("Configuring git...")
    username = input("Enter your git username: ")
    email = input("Enter your git email: ")
    run_command(f"git config --global user.name '{username}'")
    run_command(f"git config --global user.email '{email}'")

# Main function to orchestrate setup process
def main():
    print("Welcome to the Ubuntu Setup Script!")
    print("Select an option:")
    print("1. Update system and install essential packages")
    print("2. Install Python packages")
    print("3. Configure Git")
    print("4. Exit")

    option = input("Enter your choice (1/2/3/4): ")

    if option == "1":
        update_system()
        install_essentials()
    elif option == "2":
        install_python_packages()
    elif option == "3":
        configure_git()
    elif option == "4":
        print("Exiting setup script.")
        return
    else:
        print("Invalid option. Exiting setup script.")

if __name__ == "__main__":
    main()
