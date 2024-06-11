from setuptools import setup


setup(
    name="eggsample-02-spam",
    install_requires="eggsample",
    entry_points={"eggsample": ["spam = eggsample_02_spam"]},
    py_modules=["eggsample_02_spam"],
)
