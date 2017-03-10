# abraham
[![Build Status](https://travis-ci.org/ingenieroariel/abraham.svg?branch=master)](https://travis-ci.org/ingenieroariel/abraham)

DBC files for Lincoln MKZ and Ford Fusion

This is a crowdsourced repository to decode Ford Fusion's and Lincoln MKZ can bus, we will share data dumps for the different models here and creae issues for each of the id codes.

Issues will have the following format: <can id>. For example, for id 0x83: `x83 Steering Wheel Buttons Right Side`, we will share links to data dumps that contain that code and use the ticket description to explain it fully. Once it is explained and added to the `.dbc` file we can close the ticket.

# Adding data dumps.

The data dumps should be created with `cansniffer` using the following command:
`candump can0 -l`.

If you are creating a data dump for a particular command, you have to put it in that command's folder and create a txt file that explain what was going on. Data dumps should end with the `.candump` extension and explanations with the `.txt` extension.


# How do I help?

 - Read this before you start: http://www.ioactive.com/pdfs/IOActive_Adventures_in_Automotive_Networks_and_Control_Units.pdf
 - Help close tickets by creating lines in the DBC that can correctly parse each id.
 - Add your own data dumps as pull requests and reference interesting bits in the pull requests.
