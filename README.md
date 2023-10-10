# aftereffects-version-check

A Python script to determine the After Effects Version used to save the project.

I share this little script in the expectation that the community shares more data on the different After Effects builds.

## How to run

`py afx-version-check.py PROJECTFILE.aep`

## Examples

Under the folder **aftereffects_projects** there are some project files to test the script
For example: `py afx-version-check.py aftereffects_projects/2023_23-3-0_build53.aep`

## How to contribute

1. Get a HEX-Editor
2. Open your After Effects project file in the HEX-Editor and go to the position 20(as Decimals) or 32(as HEX)
3. The bytes should begin with **00 5E**, **00 5D** or **00 5C**
4. Copy these bytes including the next 5 bytes. You and up with something like this **00 5E 00 04 0B 39 86**
5. Take your new information and add a new line in the **ae-builds.json** file according to the other examples
6. Example: **00 5E 00 04 0B 39 86** will be `{"hex": "005E00040B3986", "version": "2023, v23.3.0"},`
7. Whereas **23.3.0** is the version given in After Effects under "Help" -> "About After Effects"
8. Commit your addition or just write and issue containing your new data

Thank you.
