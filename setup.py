from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="Pratik",
    author_email="pratikchoudhary316@gmail.com",
    description="A chatbot for e-commerce interactions",  
    packages=find_packages(),
    install_requires=[
        'langchain-astradb',
        'langchain',
        'langchain-openai',
        'datasets',
        'pypdf',
        'python-dotenv',
        'flask',
        'google-generativeai',
        'langchain-google-genai'
    ]
    
)
