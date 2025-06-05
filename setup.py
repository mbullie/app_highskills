from setuptools import setup, find_packages

setup(
    name='app_highskills',
    version='0.0.1',
    description='A Frappe application for high skills management',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add your dependencies here
    ],
    classifiers=[
        'Framework :: Frappe',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False
)