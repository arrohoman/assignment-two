import openai, os


def send_req_openai(prompt):
    import openai, os
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv('openai_api_key')

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    output = response.get('choices')[0].get('text').strip()
    wp_output = f'<!-- wp:paragraph --><p>{output}</p><!-- /wp:paragraph -->'
    return wp_output

def wph2(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code

def headers(username, passworod):
    import base64
    credential = f'{username}:{passworod}'
    code = {'Authorization': f'Basic {base64.b64encode(credential.encode()).decode("utf-8")}'}
    return code
