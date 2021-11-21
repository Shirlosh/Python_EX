** PAY ATTENTION **

# the current API reached to the limit number of requests, consider to change API key at VirusTotal/VirusTotalProcess/ attribute 'API'

# to run vt alone input should be param instance dictionary (ie: 
'{"source_folder_path": "path", "iteration_entities_count": "counts"}'
)

# framework input path is hard coded at Framework -> framework.py


# some unhandled issue I found and haven't repaired :
    * sometimes an error occur when 2 process running together
    * the some of the output text disappear when I print it to the console (to file its work well)