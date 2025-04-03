from setuptools import setup, find_packages

setup(
    name="odin-crawler",
    version="1.0.0",
    description="A comprehensive web crawling and security analysis platform",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/odin-crawler",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Core Django
        'Django>=4.2,<5.0',
        'djangorestframework>=3.14',
        
        # Payment Processing
        'razorpay>=2.8.0',
        
        # Web Scraping & Automation
        'beautifulsoup4>=4.12.0',
        'selenium>=4.10.0',
        'webdriver-manager>=3.8.6',
        'requests>=2.31.0',
        'scapy>=2.5.0',
        
        # Security & Cryptography
        'cryptography>=41.0.0',
        'pycryptodome>=3.18.0',
        
        # Network & Utilities
        'psutil>=5.9.0',
        'python-dateutil>=2.8.0',
        'python-dotenv>=1.0.0',
        'dnspython>=2.4.0',
        'python-whois>=0.9.0',
        'nmap>=0.7.1',
        
        # Audio Processing
        'SpeechRecognition>=3.10.0',
        'googletrans>=3.0.0',
        
        # Tor Integration
        'stem>=1.8.0',
        'socksipy-branch>=1.1',
        
        # Data Processing
        'pandas>=2.0.0',
        'numpy>=1.24.0',
        
        # Image Processing
        'Pillow>=10.0.0',
        'opencv-python-headless>=4.7.0',
    ],
    extras_require={
        'dev': [
            'ipython>=8.12.0',
            'black>=23.3.0',
            'flake8>=6.0.0',
            'pytest>=7.3.0',
            'pytest-django>=4.5.0',
            'sphinx>=7.0.0',
        ],
        'production': [
            'gunicorn>=20.1.0',
            'whitenoise>=6.4.0',
            'psycopg2-binary>=2.9.6',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'odin-crawler=manage:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/odin-crawler/issues',
        'Source': 'https://github.com/yourusername/odin-crawler',
    },
)