import pdf_handler
import summarizer
from flask import Flask, render_template, request, redirect, url_for,session
from pathlib import Path
from livereload import Server

app = Flask(__name__)
app.secret_key = "benson_cs"

@app.route("/", methods=["GET","POST"])                                 #get=display web page, post=receive uploaded file

def home():

    if request.method == "POST":                                        #request=represents everything browser sents to flask
        print("Form submitted!")

        uploaded_file = request.files.get("pdf")                        #receiving file from web


        if uploaded_file and uploaded_file.filename:                    #a file was received AND that file has a filename aka short-circuit evaluation
            result = pdf_handler.extract_text_from_pdf(uploaded_file)   #receiving extracted text from pdf_handler to result

            if result is None:                                          #empty file
                return "Empty file. File contains no text"
            
            extracted_text, text_file = result                          #passing values received in result to extracted text and text file

            session["filename"] = uploaded_file.filename                #storing file name in session for printing in web interface
            session["text_file"] = text_file                            #storing the file name with .txt extension

            chunks = summarizer.chunks_text(extracted_text)
            print("Number of chunks:",len(chunks))

            summaries = summarizer.summarize_chunks(chunks)             #receiving generated summary from summarizer.py
            print("Number of summaries:",len(summaries))

            summary = "\n\n".join(summaries)
            print("Combined summaries length:",len(summary))

            final_summary = summarizer.combine_summaries(summary)
            print("Final summary length:",len(final_summary))

            output_directory = Path("output")
            output_directory.mkdir(exist_ok=True)

            previous_summaries = []

            for summary_file in output_directory.glob("*_summary.txt"):
                if summary_file.name != f"{Path(uploaded_file.filename).stem}_summary.txt":
                    previous_summary = summary_file.read_text(encoding = "utf-8")

                    previous_summaries.append(
                        f"Document: {summary_file.stem}\n"
                        f"Summary:\n{previous_summary}"
                    )

            previous_summaries_text= "\n\n".join(previous_summaries)

            if previous_summaries_text:
                related_documents = summarizer.find_realted_documents(
                    final_summary,
                    previous_summaries_text
                )

                print("Related Documents:")
                print(related_documents)
            else:
                print("No previous documents found.")

            summary_file = output_directory/f"{Path(uploaded_file.filename).stem}_summary.txt"

            summary_file.write_text(final_summary,encoding="utf-8")

            session["summary_file"] = str(summary_file)                 #storing summary in session


        elif request.form.get("query"):                                 #for query session
            text_file = session.get("text_file")                        #receiving the text file stored in session 

            if not text_file:                                           #query without file
                return "Upload a file first"
            
            text_file_path = Path(text_file)                            #reconverting into path from string
            text_file = text_file_path.read_text(encoding = "utf-8")    #reading the contents

            query = request.form.get("query")                           #receiving the query from web
            query_response = summarizer.query(text_file,query)          #passing query and extracted text to summarizer for query response

            query_file = Path("output")/f"{Path(session["filename"]).stem}_queries.txt"

            with query_file.open("a", encoding="utf-8") as file:
                file.write(f"Query:{query}\n\n")
                file.write(f"{query_response}\n\n")
                file.write("\n" + "-" * 60 + "\n\n")

            session["query_file"] = str(query_file)                     #storing query response in session


        else:
            return "Please upload a file first."
        
        return redirect(url_for("home"))                                #for refreshing

    
    summary_file = session.get("summary_file","")                       #display summary on web

    if summary_file:
        summary = Path(summary_file).read_text(encoding="utf-8")

    else:
        summary = ""

    query_file = session.get("query_file","")                   #display query response on web

    if query_file:
        query_response = Path(query_file).read_text(encoding="utf-8")

    else:
        query_response = ""

    filename = session.get("filename","")                               #display file name on web

    return render_template("index.html",summary_of_pdf=summary,query_response=query_response,filename=filename) 


@app.route("/clear",methods=["POST"])

def clear():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch("templates/")
    server.watch("static/")
    server.serve(host="127.0.0.1", port=5000, debug=True)