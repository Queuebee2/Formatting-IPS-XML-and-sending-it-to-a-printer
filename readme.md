
# Problem
In Individual Project Skill meetings, every student is given a sheet with their ratings, rated by the other students in the group.
The tutor has to go through many convoluted, time-consuming methods to create this sheet. The process involves downloading many XML files, opening them Individually in a program like Office Excel and then adjusting many settings to tune it for printing the desired output sheet.

It appears that this system is not well optimized and could use a rework, but this seems not possible at the moment. Instead of a full rework, a small script can be written to automate the process and alleviate the task of producing the rating sheets. Preferably the script is fast and portable, scales with the amount of information in the XML file and lets the user decide the output format.


### The data: XML
First I inspected the xml files manually. I find everything is cluttered so I look up a way to structure it so it is more readable, I find `XML Tools` in the `Notepad++` plugins section to do the job. Using `ctrl`+`shift`+`alt`+`b`, I can now easily format the XML to readable XML code.
I see there are a lot of complex _<formatting things I dont know the name of, I have never really looked into XML>_

### F column too wide
In Excel I find that column 'F' is wider than it needs to be. This impedes the printing process by making the whole document too wide to fit on a vertically oriented A4 sized paper sheet.

After editing the F columns manually and saving the XML as a different file and then comparing both XML's in a diffchecker, It seems that the solution to the too-wide problem is to change `280` to, say, `80`  in all occurrences of the following piece XML code:
```xml
<Column ss:AutoFitWidth="0" ss:Width="280" />
```
For the dataset I got to test this, this fixes the too-wide problem and reduces the width of each sheet to fit an A4 sheet vertically.

### Printing Problem
First of all, I don't really know how to print (formatted) stuff with python yet. Some issues that could occur: changing printer, printer access, sending an XML file to a printer causes it to print it as plaintext of the XML (unsure)

I'll look into this later bye
