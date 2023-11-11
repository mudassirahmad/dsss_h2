from setuptools import setup,find_packages

setup(
    name='math-quiz',
    version='0.1.0',    
    author='Mudassir Ahmed',
    author_email='mudassir.ahmed@fau.de',
    license='Appache',
    packages=find_packages(),
    install_requires=['setuptools==68.2.2'],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz.module:__main__',
        ],
    }

)