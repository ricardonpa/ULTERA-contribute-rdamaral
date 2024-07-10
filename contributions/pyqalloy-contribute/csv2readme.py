import os, sys
import csv, datetime

def writeReadme(path: str):
    '''This function reads all CSV files in a directory and writes the README.md file in the root of the repository.'''

    # Lists to hold the collected data
    files = []
    names = []
    emails = []
    comments = []
    line_counts = []

    # Iterate over all files in the path
    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            # Construct full file path
            filepath = os.path.join(path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                # Initialize line counter for the current file
                line_count = 0
                # Initialize variables to store Name, Email, and Comment for the current file
                current_name = ''
                current_email = ''
                current_comment = ''
                for i, row in enumerate(reader):
                    if i == 0:
                        current_name = row[1].strip()  # Extract Name
                    elif i == 1:
                        current_email = row[1].strip()  # Extract Email
                    elif i == 4:
                        current_comment = row[1].strip()  # Extract Comment
                    # Count lines starting from line 8
                    if i >= 7:
                        line_count += 1
                # Append the extracted data for the current file to the lists
                files.append(filename)
                names.append(current_name)
                emails.append(current_email)
                comments.append(current_comment)
                line_counts.append(line_count)

    # Writes README.md preamble
    readme = f'''
## This Dataset Contributions

**Name:** {' / '.join(set(names))}
<br>
**Email:** {' / '.join(set(emails))}
    '''

    for i, comment in enumerate(comments):
        readme += f'''
```
File: {files[i]}
Datapoints: {line_counts[i]}
Comment: {comment}
```
    '''

    readme += f'''
**Last time updated:** {datetime.datetime.now().strftime("%m-%d-%Y %I:%M%p").lower()}

## The ULTERA Database
This template repository was developed for contributing to the [**ULTERA Database**](https://ultera.org) carried under the [**DOE ARPA-E ULTIMATE program**](https://arpa-e.energy.gov/?q=arpa-e-programs/ultimate) that aims to develop a new generation of materials for turbine blades in gas turbines and related applications. 

The main scope of this dataset is collecting data on compositionally complex alloys (CCAs), also known as high entropy alloys (HEAs) and multi-principle-element alloys (MPEAs), with extra attention given to (1) high-temperature (refractory) mechanical data, (2) phases present under different processing conditions. Although low-entropy alloys (incl. binaries) are typically not presented to the end-user (or counted in statistics), some are present and used in ML efforts; thus **all high-quality alloy data contributions are welcome!**

## How to Contribute?
Contributing is pretty much restructuring your data into a spreadsheet. 

Before you start:

1. Fork the [ULTERA-contribute](https://github.com/PhasesResearchLab/ULTERA-contribute/tree/main) repository, renaming your fork with a unique identifier, i.e., ULTERA-contribute`-yourUniqueIdentifier`, e.g.: `-AMK`, `-amkrajewski`, `-adamkrajewski`, etc.

2. Enable `GitHub Actions` for your fork by (1) going to `Settings > Actions (General) > Actions permissions`, (2) Select `Allow all Actions and Reusable Workflows` and save, and (3) Scroll down to `Workflow permissions`, select `Read and write permissions`, and save.

3. (Optional/Recommended) Enable the `Issues` page for your fork by (1) going to `Settings`, (2) scrolling down to `Features`, and (3) checking the box next to Issues. This will allow others to let you know if they find any problems with your data, or just want to ask questions.

Once your forked repository is ready:

1. Make a copy of [`ULTERA_Template.xlsx`](./ULTERA_Template.xlsx) and rename it to something describing what you are uploading to help you remember what is inside, e.g., `refractory_bcc_heas.xlsx`, `CrMoNiBased_DuctilityAndHardness.xlsx`, `HardnessCollectionHEA.xlsx`. 

PS: _Avoid_ putting any version number or year in the name, as it will make correcting errors in the datasets much more difficult.

2. Fill out your spreadsheet copy with your datapoints, folowing the quick-guide and examples provided in the template.

3. Repeat steps 1 and 2 until you have completed adding all of your data to your repository. 

4. Once you're done, commit your changes to your repository. The [@PhasesResearchLab/ULTERA](https://github.com/orgs/PhasesResearchLab/teams/ULTERA) team will get a notification of your contributions and automatically process the data into the ULTERA database.

For further instructions on the contribution proccess or *if you want to contribute without making your data public*, please refer to [`ULTERA_Manual.pdf`](./ULTERA_Manual.pdf). 

In case you have any questions, please do not hesitate to [open an issue](https://github.com/PhasesResearchLab/ULTERA-contribute/issues) to get help!
    '''

    # Overwrite README.md in the roof of the repository with readme
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(readme)

if __name__ == '__main__':
    writeReadme(sys.argv[1] + '/contributions')