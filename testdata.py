import urllib2
import json

response = urllib2.urlopen('http://localhost:8080/api/json')
#response = urllib2.urlopen('http://ecombd.intuit.net/job/eos-QDC/api/json')
#response = urllib2.urlopen('http://rescue-pp.intuit.net/view/PDS/job/PDS%20Application%20Stop%20and%20Start%20Jobs/api/json')
data = json.load(response)
jobs_failed = {}
jobs_notbuilt = {}
listjob_list = []
for myjobs in data["jobs"]:
        listjob_list.append(myjobs["name"])
        listjob_list.append(myjobs["color"])
        temp = {}
        #temp["url"] = str(myjobs["url"])
        if(myjobs["color"] == "red"):
                temp["color"] = str(myjobs["color"])
                temp["url"] = myjobs["url"]
                jobs_failed[myjobs["name"]] = temp
                for failedjobs in jobs_failed.keys():
                        print failedjobs
                        #print "List Failed Jobs URL :",jobs_failed[failedjobs]["url"]
                        failedurl = jobs_failed[failedjobs]["url"] + "api/json"
                        #print failedurl
                        response = urllib2.urlopen(failedurl)
                        data = json.load(response)
                        

        if(myjobs["color"] == "notbuilt"):
                temp["color"] = myjobs["color"]
                jobs_notbuilt[myjobs["name"]] = temp


#print "All Data :", data
print "List jobs name and color : " ,listjob_list
print "Jobs Failed Are :",jobs_failed
print "Jobs not Built so far :",jobs_notbuilt
