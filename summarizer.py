import ollama
import re

def summarize(text):
    response = ollama.generate(
        model = "gemma3:4b",
        prompt = f'''You are an expert document analyst and summarizer.

Your task is to analyze the following extracted text from a document and produce a clear, well-structured summary along with the document's main headings and their key points.

Before writing the output, internally perform the following steps. Do not include these steps or your reasoning in the output.

Determine the type of document (e.g., article, research paper, report, syllabus, question paper, manual, legal document, resume, meeting notes, book chapter, etc.).
Understand the primary purpose of the document.
Identify the intended audience, if it can be inferred.
Identify the main sections or logical structure of the document.
Extract the key ideas, concepts, arguments, objectives, or information.
Identify the document's major headings or sections.
For each heading, identify the important points that belong to that section.
Ignore repetitive information, formatting artifacts, page numbers, headers, footers, and unnecessary details.
Preserve the author's original intent and logical flow.
Do not add facts, interpretations, or opinions that are not supported by the document.
If examples only support a larger idea, summarize the idea instead of listing every example.
Adapt the writing style to the type of document.

Generate the output using the following format.

SUMMARY\n

Begin with a short paragraph explaining what the document is and its overall purpose.

Then provide a well-organized summary that:

Captures the main ideas accurately.
Preserves the meaning and intent of the original document.
Follows the logical order of the source.
Removes unnecessary details and repetition.
Is significantly shorter than the original.
Uses simple, professional language.
Is written using multiple well-structured paragraphs instead of a single long paragraph.
Does not include markdown formatting such as **, *, _, or #.
Does not include your reasoning process.

MAIN HEADINGS AND KEY POINTS\n

After the summary, list each major heading found in the document.

For every heading:

Heading: <Heading Name>

Key point 1
Key point 2
Key point 3

Only include points that belong to that heading. Keep the bullet points concise while preserving the important information.

If the document does not contain explicit headings, infer logical section titles based on the content and organize the information under those headings.

If the document is:

a question paper, summarize the examination structure, marking scheme, modules, and topics being assessed rather than listing every question.
a syllabus, summarize the curriculum, course objectives, assessment pattern, learning outcomes, and major subjects covered.
an article or essay, summarize the central argument, major sections, supporting ideas, and overall conclusion.
a research paper, summarize the problem, methodology, findings, and conclusion.
a report, summarize the purpose, observations, findings, recommendations, and conclusion.

Additional formatting requirements:

Do not output any asterisks (*), markdown symbols, or decorative characters.
Separate paragraphs with a blank line for readability.
Ensure the summary is neatly formatted and easy to read.
Keep the headings in the same order as they appear in the document whenever possible.
Do not invent headings or information that are not supported by the document unless explicit headings are absent, in which case infer logical section names from the content.
Return only the final formatted output.

Document Text:

{text}'''

    )
    return response["response"]


def chunks_text(text,chunk_size=3000,overlap=200):
    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size

        if end >= len(text):
            chunks.append(text[start:].strip())
            break

        boundary = text.rfind("\n\n",start,end)

        if boundary <= start:
            matches = list(re.finditer(r'[.!?]\s+',text[start:end]))

            if matches:
                boundary = start + matches[-1].end()

        if boundary <= start:
            boundary = text.rfind(" ",start,end)

        if boundary <= start:
            boundary = end

        chunks.append(text[start:boundary].strip())

        start = boundary - overlap

    return chunks


def summarize_chunks(chunks):
    summaries = []

    for chunk in chunks:
        summary = summarize(chunk)
        summaries.append(summary)

    return summaries


def combine_summaries(summaries):
    response = ollama.generate(
        model="gemma3:4b",
        prompt=f"""
YCreate one complete final summary from the following summaries of different
parts of the same document.

Output exactly two sections:

SUMMARY

Write a coherent summary covering the important information from the entire
document, including the beginning, middle, and conclusion.

MAIN HEADINGS AND KEY POINTS

List the major headings in the order they appear and give concise key points
under each heading.
For each major heading, provide 2-3 key points maximum.
Do not include subheadings unless they are important.

Requirements:
- Use only information provided below.
- Remove repetition.
- Do not omit major sections.
- Do not add new information.
- Use clear professional language.
- Complete the response without stopping mid-sentence.
- Do not use markdown symbols such as #, *, or **.

Summaries:

{summaries}
""",
    options={
        "num_predict": 4000
    }
    )
    return response["response"]


def find_realted_documents(new_summary, previous_summaries):
    response = ollama.generate(
        model="gemma3:4b",
        prompt=f'''You are a document relationship analyzer.

A new document has been summarized below. You will also receive summaries
of documents that were uploaded previously.

Determine which previous documents are meaningfully related to the new document
based on their subject, topics, concepts, or purpose.

New document summary:
{new_summary}

Previous documents:
{previous_summaries}

For each previous document, return one of these classifications:

RELATED
NOT RELATED

Only classify a document as RELATED if there is a meaningful connection in
content or subject matter.

Return only the classifications and the corresponding document names.
Do not provide explanations.
'''
    )

    return response["response"]

def query(text_file,query):
    response = ollama.generate(
        model="gemma3:4b",
        prompt=f"""
Answer the user's question only using the document below.

Document:
{text_file}

Question:
{query}

If the answer is not present in the document, say so.
"""
    )
    return response["response"]