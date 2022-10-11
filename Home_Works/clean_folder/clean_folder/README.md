LICENSE
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

BOT assistent

User input can consist of three arguments (from 1 to 3 arguments) 
argument_1 – command (required argument) 
argument_2 – another parameter (example name ‘Billi’)
argument_3 – another parameter (example phone number, format 067XXXXXXX – 10 digits)

Descriptions for commands with understand bot:

hello - answear: How can I help you?
add   “name telephone number” - save new contact. 
Example user input: add Billi 0671234567 
change “name telephone number” - change telephone number for existed contact.
Example user input: change Billi 0672345678
phone “name” - show telephone number. 
Example user input: phone Billi
show all  “show all” - contacts (name telephone number). 
Example user input: show all
See - n - show n records (you could use this command several times).
 Example user input: see 4
addnum “name telephone number” - add aditional tel number for certain contact.
Example user input: Billi 0661234567
del “name telephone number” - del tel number for certain contact.
Example user input: Billi 0661234567
addbirth “name birthday” - add date of birthday in data format. 
Example user input: Billi 01.01.1990
nextbirth “name” - show how many days left up to next birthday
Example user input: Billi
help - bot show commands explanations
Example user input: help
save “name” - save data base in file: name (without extention)
Example user input: save filename
load “name” - load data base from file: name (without extention)
Example user input: load filename
lookup “text” - find text in records (no difference which case of characters)
Example user input: load text
delrec “name” - delete record from AddressBook
Example user input: delrec Billi
addemail “name email” - add email to record
Example user input: addemail Billi billi@ukr.net
changeemail “name new_email” - change all emails on new one
Example user input: changeemail Billi billi_new@ukr.net
addadress “name text” - add adress to record
Example user input: addadress' Billi address_text
addnotes “tag text” - add notes to record
Example user input: addnotes task my task tomorrow
findtag “teg_text” - looking up notes by tages
Example user input: findtag task
sortnotes “teg_text” - sorting up notes by tages 
Example user input: sortnotes
delnotes “tag” - del notes by tages
Example user input: delnotes task
changenotes “tag_text” - change notes by tages 
Example user input: changenotes task all done
sortfiles “folder_path” - sort files in folder
Example user input: sortfiles' task C:\Desctop\Other
guess    - switch on guess mode ---> analizing taping and try to guess command
Example user input: guess
checkbirth “days_number “- display list of contacts, who have birthday in x days
Example user input: checkbirth 30
"good bye" or "close" or "exit" - bot stops work and messege "Good bye!"
