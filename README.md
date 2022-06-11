# interactions-colors
Simple Module for colors in embeds

## PyPI Section:

IMPORTANT TO MAKE THIS WORK:
- In PyPI:
    - Go to https://pypi.org/ and log in
    - Go to the "Account settings" tab
    - Scroll down till you reach "API tokens"
    - Add a new API token with your project name as the token name
    - Choose "Entire account (all projects)" scope
        - This is done since the project still is not created
            - The action will create it automatically
    - Click "Add token" and save it somewhere safe
- In GitHub repository:
    - Go to the "Settings" tab
    - Next, go to the "Secrets" side tab
    - Click "New repository secret"
    - (IMPORTANT) Set name to "PYPI_API_TOKEN"
    - Set value to your API token you got earlier
    - Click "Add secret"

What to do:
- Change file/directory name `import_name` with the package import name
- Add your code inside `import_name/` directory
- Add dependencies separated by newlines in `requirements.txt`
- Modify `setup.py` to your needs
- Optional:
    - Add ignored files/directories in `.gitignore`
    - Change license

How to make new PyPI releases?
- (IMPORTANT) Increment version in `setup.py`
- Make a new release in GitHub with same tag as version
- The action will automatically publish a new PyPI release for you!

## Extension Section:

This is a raw template that will get you started coding an extension.

I have put comments in the code to help you understand what to do.

You may need to rename some file and directory names to fit your needs.

Usage for the end user:
```py
import interactions

client = interactions.Client(...)
...
extension = client.load("interactions.ext.import_name", ...)  # the user can input arguments, btw
...
client.start()
```#   i n t e r a c t i o n s - c o l o r s  
 