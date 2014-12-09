#!/usr/bin/python
import qa
import cgi
import subprocess
import uuid
import urllib

def call( args ):
        cmd = subprocess.Popen(args, stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
        return cmd_out

args = cgi.FieldStorage(keep_blank_values = 1)
if args["request"].value == "question_list":
	cmd_out = call(["sh", "question", "list"])
	questions = cmd_out.split("\n")
	qa.show_question_list(questions)
if args["request"].value == "show_question":
	id = args["question_id"].value
	cmd_out = call(["sh", "question", "show", id])
	qa.show_question(cmd_out)
if args["request"].value == "vote_question":
	id = args["question_id"].value
	call(["sh", "question", "vote", args["vote"].value, id])
	cmd_out = call(["sh", "question", "show", id])
        qa.show_question(cmd_out)
if args["request"].value == "vote_answer":
        question_id = args["question_id"].value
        answer_id = args["answer_id"].value
        call(["sh", "question", "vote", args["vote"].value, question_id, answer_id])
        cmd_out = call(["sh", "question", "show", question_id])
        qa.show_question(cmd_out)
if args["request"].value == "add_question_form":
        title = "What is your question?"
        submit_link = "?request=add_question"
	cancel_link = "?request=question_list"
        qa.form(title, submit_link, cancel_link)
if args["request"].value == "add_answer_form":
        title = "What is your answer?"
        submit_link = "?request=add_answer&question_id=" + urllib.quote(args["question_id"].value)
	cancel_link = "?request=show_question&question_id=" + urllib.quote(args["question_id"].value)
        qa.form(title, submit_link, cancel_link)
if args["request"].value == "add_question":
        question_name = str(uuid.uuid1())
	#subprocess.call(["./question", "create", question_name, args["content"].value])
	subprocess.call(["sh", "question", "create", question_name, args["content"].value])
	cmd_out = call(["sh", "question", "list"])
        questions = cmd_out.split("\n")
        qa.show_question_list(questions)
if args["request"].value == "add_answer":
        answer_name = str(uuid.uuid1())
        #hasError = subprocess.call(["./question", "answer", args["question_id"].value, answer_name, args["content"].value])
	hasError = subprocess.call(["sh", "question", "answer", args["question_id"].value, answer_name, args["content"].value])
        if(hasError):       
                cmd_out = call(["sh", "question", "list"])
                questions = cmd_out.split("\n")
                qa.show_question_list(questions)
        else:
                id = args["question_id"].value
                cmd_out = call(["sh", "question", "show", id])
                qa.show_question(cmd_out)
