from perplexityai import Perplexity
import json
import logging
from colorlog import ColoredFormatter


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create formatter
formatter = ColoredFormatter(
    "%(log_color)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'red',
        'WARNING': 'yellow',
        'ERROR': 'green',
        'CRITICAL': 'red',
    },
    secondary_log_colors={},
    style='%'
)


handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


openai.api_key = 'your-api-key'

def read_json(file_path):
    logger.info("Reading Person Details")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def generate_personalized_email(person_details, ideas):
    # name = person_details['Name']
    # role = person_details['Headline']
    # company = person_details['Experience']['Experience_1']['Person Post']\
    logger.info("Genrating Prompt")

    prompt = json.dumps(person_details)
    prompt += "\n"
    prompt += "I have Providing some sample of emails which can be used to write email but don't use any name company name form mails except zenskar You can use zenskar name in mail\n"
    prompt += "Sample Emails:\n"
    prompt += "\n:"
    prompt += """### **Sample Emails**
    
    ## Email 1 - The Agile Monkeys
    
    Hey Francisco,
    
    I noticed that you’re responsible for finance at The Agile Monkeys and wanted to share some ideas I thought of that could help you reduce manual billing efforts and improve cash flow:
    
    - Automate event-driven billing for the full-stack software engineers to reduce manual work and streamline finance processes.
    - Improve cash flow by automating revenue recognition workflows tailored to serverless application development services.
    - Outsource billing for complex usage-based models without engineering resources, ensuring accurate and error-free billing.
    
    If you're interested, I'm from Zenskar, where we've built a cost effective AI solution that can help you implement these ideas.
    
    Best,
    Zenskar
    
    ## Email 2
    
    Hi Name,
    
    Many congratulations as you celebrate 10 years of Genomics England! It’s great to see how your 100000 Genomes Project has transformed the face of genomic healthcare in the UK :)
    
    That said, any chance you're looking for new ways to transform billing workflows? I thought  of a few tailored strategies that could help you:
    
    - Automate usage-based pricing & billing with unlimited flexibility for Genomic’s patient treatments division
    - Improve cash flows for your NHS patient diagnostics segment with automated payment reminders
    - Improve revenue forecasting with real-time visibility in revenue metrics
    
    If you're interested, we've built a billing tool that can help you implement these strategies. Can we schedule a quick call?
    
    Thanks,\n"""

    prompt += "See in sample Emails and JSON data I have provided you. Use sample mail as a reference and the information about the person to whom we are writing mail is present in the json data Now Write a personalized email don't add any unnecessary content like offering jobs to them use the sample email carefully and for regards and thanks just write Zenskar write a mail for me use the json data\n" 
    
    for idea in ideas:
        prompt += f"- {idea}\n"

    prompt += f"\nIf you're interested, I'm from Zenskar, where we've built a cost-effective AI solution that can help you implement these ideas.\n\nBest,\n\nZenskar"
    logger.info("Trying to generate the Email......................")
    answers_list = list(Perplexity().generate_answer(prompt))
    logger.info("_________________________EMAIL___________________________")
    if answers_list:
        last_answer = answers_list[-1]['answer']
        print(f"🤖: {last_answer}")
    else:
        print("No answers generated.")
    return last_answer

# Example usage
        
def Write_Email(file_path):
    json_file_path = file_path
    person_details = read_json(json_file_path)
    ideas = [
        "Automate event-driven billing for a seamless experience.",
        "Explore tailored solutions for revenue recognition workflows.",
        "Optimize billing for different usage models to ensure accuracy."
    ]

    personalized_email = generate_personalized_email(person_details, ideas)
    print(personalized_email)

    file_path = "Mail.txt"

    # Open the file in write mode and store the string
    with open(file_path, 'w') as file:
        file.write(personalized_email)

    print(f"String has been successfully stored in {file_path}")
