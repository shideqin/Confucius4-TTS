from setuptools import setup, find_packages

setup(
    name="confuciustts",
    version="0.1.0",
    description="Confucius4-TTS: Multilingual and Cross-Lingual Zero-Shot TTS Engine",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="NetEase Youdao",
    url="https://github.com/netease-youdao/Confucius4-TTS",
    packages=find_packages(include=["confuciustts", "confuciustts.*",
                                     "external", "external.*"]),
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.7.0",
        "torchaudio>=2.7.0",
        "transformers>=4.52,<4.56",
        "huggingface_hub>=0.36",
        "safetensors>=0.7.0",
        "numpy>=1.26",
        "pyyaml>=6.0",
        "librosa>=0.10",
        "scipy>=1.15",
        "soundfile>=0.13",
        "sentencepiece>=0.2",
        "ema-pytorch>=0.7",
        "packaging>=26",
        "filelock>=3.25", "matplotlib",
        "fsspec>=2026",
        "inflect", "jaconv", "pykakasi", "protobuf>=3.19",
    ],
    extras_require={
        "train": [
            "pytorch-lightning", "tensorboard", "matplotlib", "datasets",
        ],
        "web": [
            "gradio",
        ],
        "vllm": [
            "vllm>=0.16.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
    ],
)
