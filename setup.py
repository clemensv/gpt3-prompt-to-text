from setuptools import find_packages, setup

setup(
    name="gpt3-prompt-to-text",
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=False,
    install_requires=["openai", "setuptools_scm"],
    setup_requires=["setuptools_scm"],
    entry_points={
        "console_scripts": [
            "gpt3-prompt-to-text = gpt3_prompt_to_text.gpt3_prompt_to_text:main"
        ]
    },
)
