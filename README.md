# aftereffects-version-check

A Python script to determine the After Effects Version used to save the project.

This script is rewritten and now actually calculates the project version instead of just comparing a HEX string in a data table.

After some more data analysis I finally understood how the project version is encoded in the project file. The analysis will be added later in here.

I have kept the JSON data for further analysis and to look up the year the software version was released. 

## How to run

`py afx-version-check.py PROJECTFILE.aep`

## Examples

Under the folder **aftereffects_projects** there are some project files to test the script
For example: `py afx-version-check.py aftereffects_projects/2023_23-3-0_build53.aep`

## Analysis

to be done...