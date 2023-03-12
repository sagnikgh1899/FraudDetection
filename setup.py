import os
from setuptools import setup, find_packages

PACKAGES = find_packages()

opts = dict(name='FraudDetection',
            maintainer='Sagnik Ghosal, Ishank Vasania, Prerit Chaudhary, Neel Shah',
            maintainer_email='fraud.detect@gmail.com',
            description='A Fraud Detection Tool Designed to Analyze Medical Claims',
            long_description='This tool is a fraud detection system designed to analyze medical insurance claims to '
                             'identify potential fraudulent activities.',
            url='https://github.com/sagnikgh1899/FraudDetection',
            # download_url="",
            license='MIT',
            # classifiers="CLASSIFIERS",
            author='Sagnik Ghosal, Ishank Vasania, Prerit Chaudhary, Neel Shah',
            author_email='fraud.detect@gmail.com',
            version='1.2',
            packages=['pandas', 'numpy', 'pyod', 'suod', 'bokeh', 'flask', 'plotly', 'seaborn', 'matplotlib'],
            package_data="None",
            # install_requires=["python3", "jupyter notebook"],
            requires=['pandas', 'numpy', 'pyod', 'suod', 'bokeh', 'flask', 'plotly', 'seaborn', 'matplotlib'])

if __name__ == '__main__':
    setup(**opts)
