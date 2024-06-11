from setuptools import setup


setup(
    name="eggsample-01-tofu",
    install_requires="eggsample",
    entry_points={"eggsample": ["tofu = eggsample_01_tofu"]},
    py_modules=["eggsample_01_tofu"],
)
