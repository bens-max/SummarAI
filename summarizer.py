import ollama

def summarize(extracted_text):
    print()
    print("SUMMARY".center(230,"="))
    print()
    response = ollama.generate(
        model = "gemma3:4b",
        prompt = f'''You are an expert document analyst and summarizer.

Your task is to analyze the following extracted text from a document and produce a high-quality summary.

Before writing the summary, internally perform the following steps. Do not include these steps or your reasoning in the output.

1. Determine the type of document (e.g., article, research paper, report, syllabus, question paper, manual, legal document, resume, meeting notes, book chapter, etc.).
2. Understand the primary purpose of the document.
3. Identify the intended audience, if it can be inferred.
4. Identify the main sections or logical structure of the document.
5. Extract the key ideas, concepts, arguments, objectives, or information.
6. Ignore repetitive information, formatting artifacts, page numbers, headers, footers, and unnecessary details.
7. Preserve the author's original intent and logical flow.
8. Do not add facts, interpretations, or opinions that are not supported by the document.
9. If examples are only supporting a larger idea, summarize the idea rather than listing every example.
10. Adapt the style of the summary to the document type.

Generate the summary using the following format.

First paragraph:
Briefly explain what the document is and its overall purpose.


Then provide a well-organized summary that:

• Captures the main ideas accurately.
• Preserves the meaning and intent of the original document.
• Follows the logical order of the source.
• Removes unnecessary details and repetition.
• Is significantly shorter than the original.
• Is easy to understand without reading the full document.
• Uses complete, coherent paragraphs instead of copying sentences.
• Uses simple, professional language.
• Mentions important sections or topics when appropriate.
• Does not include your reasoning process.
• Does not use markdown tables.

If the document is:
- a question paper, summarize the examination structure, marking scheme, modules, and topics being assessed rather than listing every question.
- a syllabus, summarize the curriculum, course objectives, assessment pattern, learning outcomes, and major subjects covered.
- an article or essay, summarize the central argument, major sections, supporting ideas, and overall conclusion.
- a research paper, summarize the problem, methodology, findings, and conclusion.
- a report, summarize the purpose, observations, findings, recommendations, and conclusion.

Return only the final summary.

Document Text:

{extracted_text}'''

    )
    return response["response"]