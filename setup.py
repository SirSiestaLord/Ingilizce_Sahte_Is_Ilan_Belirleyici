from setuptools import setup, find_packages

setup(
    name="job_fraud_detection",
    version="1.0.0",
    author="Tuğcan Fikret Çağlayan",
    description="Yapay Zeka Destekli Sahte İş İlanı Analizi ve Anomali Tespiti Sistemi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'pandas',
        'scikit-learn',
        'numpy',
        'jinja2',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'train-model=model_train:train_and_save_model',
            'run-app=app:main',
        ],
    },
)