import requests
import os
from dotenv import load_dotenv
load_dotenv()
# from pprint import pprint
from all_functions import send_req_openai, wph2, headers


#user input - keyword
input_keyword = input('Enter 3 keywords in comma seperated value: ')
keywords = input_keyword.split(',')
file = open('keyword.txt', 'a+')
for kw in keywords:
    file.writelines(kw.strip()+'\n')
file.close()

#read keywords from file
file = open('keyword.txt', 'rt')
keyword_list = [list.rstrip() for list in file.readlines()]
file.close()
# print(keyword_list)
for kw in keyword_list:
    primary_keyword = kw
    striped_kw = kw.replace('best ', '').strip()
    intro_prompt = f'write an intro in 100 words about mistakes people make while buying {striped_kw}.'
    what_prompt = f'what is {striped_kw}?'
    whyimportant_prompt = f'why buying the right {striped_kw} is important?'
    howto_prompt = f'How to choose best {striped_kw}'
    keypoint_prompt = f'What are the 5 key points I should consider while buying {striped_kw}? Explain each key point in 100 words.'
    conclusion_prompt = f'write a conclustion in 100 words about {primary_keyword}.'

    prompt_list = [intro_prompt, what_prompt, whyimportant_prompt, howto_prompt, keypoint_prompt, conclusion_prompt]
    # print(primary_keyword)
    # print(striped_kw)
    openai_content = []
    for prompt in prompt_list:
        text = send_req_openai(prompt)
        openai_content.append(text)

    title = f'Buying Guide for {primary_keyword}'
    intro = openai_content[0]
    heading_one = wph2(what_prompt.title())
    whatis = openai_content[1]
    heading_two = wph2(whyimportant_prompt.title())
    whyis = openai_content[2]
    heading_three = wph2(howto_prompt.title())
    howto = openai_content[3]
    heading_four = wph2(f'What are some key points you should consider while buying {striped_kw}?')
    keypoint = openai_content[4]
    concheading = wph2('Conclusion')
    conc = openai_content[5]

    print(openai_content)

    content = f'{intro}{heading_one}{whatis}{heading_two}{whyis}{heading_three}{howto}{heading_four}{keypoint}{concheading}{conc}'

    data = {
        'title': title,
        'content': content,
        'status': 'publish',
        'slug': primary_keyword.replace(' ', '-')
    }
    
    header = headers('admin','mHMx drAq T9yc 6PUW 66dt BOJr')
    site_url = os.getenv('site_endpoint')
    r = requests.post(site_url, data=data, headers=header, verify=False)
    print(r)