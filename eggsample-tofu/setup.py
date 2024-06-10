from setuptools import setup


setup(
    name="eggsample-tofu",
    install_requires="eggsample",
    entry_points={"eggsample": ["tofu = eggsample_tofu"]},
    py_modules=["eggsample_tofu"],
)
