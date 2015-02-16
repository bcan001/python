# testing mechanize with python
# NOTE: web scraping takes information from a websites available HTML

# IMPORTS THE MECHANIZE MODULE
import mechanize

# br is the current page, throughout the application

br = mechanize.Browser()
response = br.open("http://chicago.craigslist.org/")

#print response.read()      # the text of the page
#response1 = br.response()  # get the response again
#print response1.read()     # can apply lxml.html.fromstring()



# prints all the forms on the page:
for form in br.forms():
    print "Form name:", form.name
    print form

# prints all the links on a page:
for link in br.links():
    print link.text, link.url

# How to click on a link once you find one you want to click on:
#request = br.click_link(link)
#response = br.follow_link(link)
#print response.geturl()



#To go on the mechanize browser object must have a form selected:
#br.select_form("form1")         # works when form has a name
br.form = list(br.forms())[0]  # use when form is unnamed

# Iterate through the controls in the form:
# for control in br.form.controls:
#      print control
#      print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

# selecting a control:
# control = br.form.find_control("SelectControl")

# Having a select control tells you what values can be selected:
# if control.type == "select":  # means it's class ClientForm.SelectControl
#     for item in control.items:
#     print " name=%s values=%s" % (item.name, str([label.text  for label in item.get_labels()]))

# submitting a form that is SELECTED:
response = br.submit()
print response.read()
#br.back()   # go back


