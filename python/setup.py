from setuptools import setup, find_packages

setup(
    name="geu_cog",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # 列出您的依赖包
        'attrs',
        'fastapi',
        'pydantic',
        'PyYAML',
        'requests',
        'structlog',
        'typing_extensions',
        'uvicorn'
    ],
)