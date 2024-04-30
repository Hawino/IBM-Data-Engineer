# Linux Commands and Shell Scripting - Final Project

## Scenario
In this scenario, you are a lead Linux developer at the top-tech company ABC International Inc. As one of ABC Inc.'s most trusted Linux developers, you have been tasked with creating a script called backup.sh which runs every day and automatically backs up any encrypted password files that have been updated in the past 24 hours.

## Task 1
Navigate to # [TASK 1] in the code.\
Set two variables equal to the values of the first and second command line arguments, as follows:\
Set targetDirectory to the first command line argument\
Set destinationDirectory to the second command line argument\
<img width="336" alt="01-Set_Variables" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/2daf529a-cff3-4153-a1b1-5c63fd82f2ea">

## Task 2
Display the values of the two command line arguments in the terminal.\
<img width="336" alt="02-Display_Values" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/2ff2f8ab-217b-49f1-8d4f-b0a05fa66eb8">


## Task 3
Define a variable called currentTS as the current timestamp, expressed in seconds.\
<img width="337" alt="03-CurrentTS" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/fe5e4574-b5be-4591-90b2-dfcfa5dfc683">

## Task 4
Define a variable called backupFileName to store the name of the archived and compressed backup file that the script will create.\
The variable backupFileName should have the value "backup-[$currentTS].tar.gz"
- For example, if currentTS has the value 1634571345, then backupFileName should have the value backup-1634571345.tar.gz.\
<img width="339" alt="04-Set_Value" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/9319e11f-202c-4001-863b-23df91f4e20e">

## Task 5
Define a variable called origAbsPath with the absolute path of the current directory as the variable's value.\
<img width="334" alt="05-Define_Variable" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/3a8ad4db-21c5-4bf4-95ee-9e74d69422ae">

## Task 6
Define a variable called destAbsPath whose value equals the absolute path of the destination directory.\
<img width="335" alt="06-Define_Variable" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/425e49d4-45ec-44d2-90ad-9151e22c43ba">

## Task 7
Change directories from the current working directory to the target directory targetDirectory.\
<img width="332" alt="07-Change_Directory" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/24c0fd31-50a7-47ef-8143-dce49dae81e2">

## Task 8
You need to find files that have been updated within the past 24 hours. This means you need to find all files whose last-modified date was 24 hours ago or less.\
To do make this easier:\
Define a numerical variable called yesterdayTS as the timestamp (in seconds) 24 hours prior to the current timestamp, currentTS.\
<img width="340" alt="08-YesterdayTS" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/20a05b61-9771-4905-8a1f-20f8423511ab">


## Task 9
Within the $() expression inside the for loop, write a command that will return all files and directories in the current folder.\
<img width="340" alt="09-List_AllFilesandDirectoriess" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/4e77d61e-148c-49c1-a2bc-f36510613f5a">


## Task 10
Inside the for loop, you want to check whether the $file was modified within the last 24 hours.\
To get the last-modified date of a file in seconds, use date -r $file +%s then compare the value to yesterdayTS.\
if [[ $file_last_modified_date > $yesterdayTS ]] then the file was updated within the last 24 hours!\
Since much of this wasn’t covered in the course, for this task you may copy the code below and paste it into the double round brackets (()):\
`date -r $file +%s` > $yesterdayTS\
<img width="348" alt="10-IF_Statement" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/17fd32ed-5707-463d-b8ef-efbbd176a1e8">


## Task 11
In the if-then statement, add the $file that was updated in the past 24-hours to the toBackup array.\
Since much of this wasn’t covered in the course, you may copy the code below and place after the then statement for this task:\
toBackup+=($file)\
<img width="338" alt="11-Add_File" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/fae4d82f-c9b2-4673-974a-5083898ffde4">


## Task 12
After the for loop, compress and archive the files, using the $toBackup array of filenames, to a file with the name backupFileName.\
<img width="339" alt="12-Create_Backup" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/70bdb247-250f-48fa-ae9b-844c452db79d">


## Task 13
Now the file $backupFileName is created in the current working directory.\
<img width="339" alt="13-Move_Backup" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/e8be8615-73e8-4e07-87fe-4dd61057d6e2">


## Task 14
Save the backup.sh file you're working on and make it executable.\
<img width="397" alt="15-executable" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/07e37d48-baba-417b-afbc-ddadae37f890">


## Task 15
<img width="429" alt="16-backup-complete" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/d59f870e-b5fe-4145-ada9-dcad72ea3f48">


## Task 16
Using crontab, schedule your /usr/local/bin/backup.sh script to backup the important-documents folder every 24 hours to the directory /home/project.\
<img width="430" alt="17-crontab" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/948144bb-1726-40e5-ad6d-7c35fa1ad73d">

