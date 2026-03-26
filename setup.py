from setuptools import setup, find_packages

setup(
    name="hailuo3",
    version="3.0.0",
    description="AI-Powered 4K Video Generator",
    author="Hailuo Team",
    url="https://github.com/sora-git-dev/hailuo-30",
    packages=find_packages(),
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.36.0",
        "diffusers>=0.24.0",
    ],
    python_requires=">=3.10",
)
