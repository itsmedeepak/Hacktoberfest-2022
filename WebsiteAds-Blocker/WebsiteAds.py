def unblock_websites(websites_to_unblock):
     host_file = host_files['Windows']
     with open(host_file, 'r+') as hostfile:
         content_in_file = hostfile.readlines()
         hostfile.seek(0)
         for line in content_in_file:
             if not any(site in line for site in websites_to_unblock):
                 hostfile.write(line)
             hostfile.truncate()
     with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
         file_content = blocked_websites_txt.readlines()
         blocked_websites_txt.seek(0)
         for line in file_content:
             if not any(site in line for site in websites_to_unblock):
                 blocked_websites_txt.write(line)
             blocked_websites_txt.truncate()
     Label(unblck_wn, text='Website is Blocked!', font=("Times", 13), bg='Aquamarine').place()
