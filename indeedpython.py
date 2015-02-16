
import mechanize

# br is the current page, throughout the application

br = mechanize.Browser()
response = br.open("http://www.indeed.com/")

#response = response.read()

br.form = list(br.forms())[0]

# prints all the information about the form we have currently selected
# for control in br.form.controls:
#     print control.value
#     print control.type
#     print control.name

# changing values in a control:
br["q"] = "Software Engineer"
br["l"] = "Chicago, IL"
# submits the form with the changes made

print br
br.submit()

print br

# prints out every link on the page
# for link in br.links():
#     print link.text, link.url

# prints the links on the page that have the text 'Software Engineer'
for link in br.links(text_regex="Software Engineer"):
	print link.text, link.url

	# CURRENTLY DOES NOT WORK BECAUSE THE SECOND LINK OPENS A POP-UP
	# need to click on every link first
	#br.follow_link(link)  # takes EITHER Link instance OR keyword args
	#print "link entered"
	#br.back()





