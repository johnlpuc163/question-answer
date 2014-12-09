import urllib
def show_question_list(questions):
  	print "Content-type: text/html\n\n"
 	print "<html><head><title>Q&A</title></head>\n"
	print "<body>\n"
	#questions = ['id1/q1', 'id2/q2', 'id3/q1']
	#print questions
	print "<h2>Question list</h2>"
	print "<ul>"
	for question in questions:
		if question:
			#id, name = question.split("/")
			#print "<li><a href=\"?request=show_question&question_id=%s&name=%s\">%s</a></li>" % (id, name, question)
			print "<li><a href=\"?request=show_question&question_id=%s\">%s</a></li>" % (urllib.quote(question), question)
	print "</ul>"
	print "<a href='?request=add_question_form'>Add question</a>"
	print "</body></html>\n"


def show_question(question):
        print "Content-type: text/html\n\n"
        print "<html><head><title>Q&A</title></head>\n"
        print "<body>\n"
	#print question
	sections = question.split("====\n")
	print "<table>\n"
	info, content = sections[0].split("\n",1)
        count, question_id = info.split(" ", 1)
	print "<caption><u>%s</u></caption>\n" % content
	print "<tr>"
    	print "<th>question</th>"
    	print "<th>%s</th>" % count
	question_id = urllib.quote(question_id)
	print "<th><a href='?request=vote_question&question_id=%s&vote=up'>up</a></th>" % question_id
	print "<th><a href='?request=vote_question&question_id=%s&vote=down'>down</a></th>" % question_id
    	print "</tr>"
	sections.pop(0)
        sections.sort(key = lambda x: int(x.split(" ")[0]), reverse=True)
	#sections = sorted(sections, key = lambda x: int(x.split(" ")[0]))
        for i in range(0, len(sections)):
	#for i in range(1, len(sections)):
		info, content = sections[i].split("\n",1)
                count, answer_id = info.split(" ", 1)
		answer_id = urllib.quote(answer_id)
		print "<tr>"
		print "<td>%s</td>" % content
		print "<td>%s</td>" % count
		print "<th><a href='?request=vote_answer&question_id=%s&answer_id=%s&vote=up'>up</a></th>" % (question_id, answer_id)
        	print "<th><a href='?request=vote_answer&question_id=%s&answer_id=%s&vote=down'>down</a></th>" % (question_id, answer_id)
		print "</tr>"	
	print "</table>\n"
        print "<p><a href='?request=add_answer_form&question_id=%s'>Add answer</a></p>" % question_id
        print "<p><a href='?request=question_list'>Return to question list</a></p>"
	print "</body></html>\n"

def form(title, submit_link, cancel_link):
	print "Content-type: text/html\n\n"
        print "<html><head><title>Q&A</title></head>\n"
        print "<body>\n"
	print "<p>%s</p>" % title
	print "<form action='%s' method=post>" % submit_link
        print "<textarea name=content rows=5 cols=20></textarea>"
        print "<p><a href='%s'>Cancel</a>" % cancel_link
        print "<input type=submit value='Submit'></p>"
        print "</form>"
	print "</body></html>\n"
