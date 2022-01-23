import subprocess #importing subprocess


#getting meta data
meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])
#decoding ,eta data
data =meta_data.decode('utf-8',errors ="backslashreplace")

#splitting data line by line
data = data.split('\n')

#create a list of profiles
profiles =[]

#traverse the data
for i in data:
         #find "all user profile in each "
         if "All User Profile" in i:
             # if found 
             # split item
             i=i.split(":")

             #item at index i will be the wifi name
             i=i[1]

             #fprmating the name
             #first and last  character is use less
             i=i[1:-1]

             #appending the wifi name in the list
             profiles.append(i)

             # printing heading
             print("{:<30}| {:<}".format("Wi-Fi Name","Password"))
             print("_________________________________")

             #transvering profi
             for i in profiles:
                 #try catch block begins
                 # try block
                try:
                     #getting meta with password using wifi
                             results = subprocess.check_outut( ['netsh','wlan','show','profile', i ,'key = clear'] )
                     #decoding and spliting data line by line
                             results = results.decode('utf-8', errors ="backlashreplace")
                             results = results.split('\n')
                     #finding passord from the result list
                             results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                     #if their is password it will print password
                             try:
                                          print("{:<30} {:<}".format(i, results[0]))

                         #else it will print blank in front of password
                             except IndexError:
                                        print("{:<30}| {:<}".format(i, ""))

                           #called when this process get failed
                except subprocess.CalledProcessError:
                                 print("Encoding Error Occured")
                                 



 # ******use this in your command prompt ( netsh wlan show profiles)