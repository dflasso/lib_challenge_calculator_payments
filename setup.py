from setuptools import find_packages, setup



setup(
    name='lib_pay_calculator',
    packages=find_packages(include=['lib_pay_calculator']),
    version='0.0.1',
    description='Python library that calculate payments according day and schedule of hours worked',
    author='Dany Lasso',
    author_email='dannylasso.a@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    test_suite='nose.collector',
    tests_require=['nose'],
)