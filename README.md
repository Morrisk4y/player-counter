# python player count from logfile
Counts keywords in a log file to identify how many players are online, 100% working for mordhau log file

so how this python script works is
in a loop
it connects to a sftp server #sftp server required
gets the file name

reads the file name
counts words in word1 and word2 # these can be sentences also.

reads if that count already exists in output.txt file
if no
types the count into a output.txt file for next run

then sends the playercount through discord webhook

