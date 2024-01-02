import openai
import re

openai.api_key = "OpenAi Key"  # Replace with your OpenAI API key

def chat_with_GJU(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Welcome to GJU! How can I help you?"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def format_email_hyperlink(response):
    # Find and replace email addresses with hyperlinks
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
    response_with_links = re.sub(email_pattern, lambda match: f'<a href="mailto:{match.group(0)}">{match.group(0)}</a>', response)
    return response_with_links

if __name__ == "__main__he":
    # Provide initial information about GJU and its programs
    initial_prompt = """The German Jordanian University (GJU) is a university located in Amman, Jordan. 
    it has 2 campuses, the main campus in Madaba Jordan and the Jabal Amman campus which has the Design & Architecture Majors
    It was established in 2005 as a public university. GJU offers various programs, including:

    - Industrial Engineering
    - Mechanical and Maintenance Engineering
    - Logistics Sciences
    - International Accounting
    - Management Sciences
    - Business Intelligence and Data Analytics
    - Architecture
    - Interior Architecture
    - Design and Visual Communication
    - Computer Sciences
    - Computer Engineering
    - Pharmaceutical and Chemical Engineering
    - Biomedical Engineering
    - German and English for Business Communication

    Tell me more about a specific program or area of interest, or ask about the campus, faculty, or reach us by Email: <a href="mailto:info@gju.edu.jo">info@gju.edu.jo</a> for any recent developments.
    """

    while True:
        user_input = input("you: ")
        user_input_with_email = user_input + " info@gju.edu.jo"

        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        # Combine the initial information with user input
        prompt = initial_prompt + "\nUser: " + user_input_with_email

        # Ask specific questions about GJU
        response = chat_with_GJU(prompt)

        # Format the response to include hyperlinks for email addresses
        response_with_links = format_email_hyperlink(response)

        print("GJUgpt : ", response_with_links)