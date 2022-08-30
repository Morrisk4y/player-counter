import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import pysftp

#SFTP Conection config
Hostname = "Host url or ip"
Username = "username here"
Password = "Sftp password here"
Port = 1234

#Dont check for host key
cnOpts = pysftp.CnOpts()
cnOpts.hostkeys = None


#LOOP
while True:
    with pysftp.Connection(host=Hostname, username=Username, password=Password, port=Port, cnopts=cnOpts) as sftp:
        print("Connection successfully established ... ")
    # Switch to a remote directory
        sftp.cwd('log file directory here')

    # Obtain structure of the remote directory '/opt'
        directory_structure = sftp.listdir_attr()

    # Print data
        for attr in directory_structure:
            print(attr.filename, attr)

        sftp.get('logfilename.log here',preserve_mtime=True)

        print(" ")
        print("File Downloaded")

    time.sleep(5)

#Finds count of all keyword in word1
    file = open('logfilename.log here','r')
    word1 = 'Login request: ?Name'
    count = 0


    for line in file.readlines():
        if word1 in line:
            count = count+1

    print(count)

#Finds count of all keyword in word2
    file = open('logfilename.log here','r')
    word2 = 'Cleared caches for player'
    count2 = 0

    for line in file.readlines():
        if word2 in line:
            count = count-1

    print(count)

#opens the output file and reads if first line = count then dont do anything
    with open(r'output.txt') as f:
        firstline = f.readline().rstrip()
        print("Reading First Line:", firstline)

        if firstline == str(count):
            print("Players online no change")
            time.sleep(10)


# else if first line in output fle then write the new count value to output file
        else:
            with open(r'output.txt', 'w') as a:
                a.write(str(count))
                print("Writing to output file the Players count:", count)

#reads the new count value from first line in output file
            with open(r'output.txt') as b:
                newline = b.readline().rstrip()
                print("Players:", count)
                playersonline = ("Players online:" + str(count))

    #webhook url
                webhook = DiscordWebhook(url='Webhhook url here')
                embed = DiscordEmbed(title='embed title here', description=playersonline, color='03b2f8')
                webhook.add_embed(embed)
                response = webhook.execute(embed)
                time.sleep(10)
