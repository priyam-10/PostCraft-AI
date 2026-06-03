from config import get_model
from user_inputs import collect_inputs
from prompt_builder import generate_post

def save ( post, topic ):
    import re

    safe_name = re.sub(r'[^a-zA-Z0-9]', '_',topic.strip())
    file_name = f"LINKDIN_POST_{safe_name}.txt"

    with open ( file_name, 'w', encoding='utf-8') as file :
        file.write(post)

    return file_name


def run () :

    try :
        model = get_model()

    except Exception as e :
        print(e)


    inputs = collect_inputs()

    try :
        post = generate_post( model, inputs)

    except Exception as e :
        print(e)

    print("\n<-----:  Post has been generated  :----->\n")
    print(f"\nTopic : {inputs['topic']}\n")

    print( post )

    filename = save( post, inputs['topic'])
    print(f"File saved Successfully : {filename}")


if __name__ == "__main__" :
    run()

    