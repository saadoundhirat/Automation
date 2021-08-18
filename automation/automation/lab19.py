import re

def get_emails(filepath: str) -> str:
    ''' get the emails from the file '''
    with open(filepath, 'r') as file:
        data = file.read()
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', data)
    result = remove_duplicates(match)
    sorted_result = sorted(result)
    emails = ""
    for x in sorted_result:
        emails += str(x)+"\n"
    return emails

def get_phone(filepath: str) ->str:
    ''' get the phone numbers from the file '''
    with open(filepath, 'r') as file:
        data = file.read()
    match = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', data)
    print(match)
    result = remove_duplicates(match)
    sorted_result = sorted(result)
    phone = ""
    for x in sorted_result:
        phone += str(x)+"\n"
    return phone

def remove_duplicates(_list)-> list:
    ''' Check if given list contains any duplicates '''
    if len(_list) == len(set(_list)):
        return _list
    else:
        return set(_list)

def makefile(_filename:str , data:str)-> None:
    ''' make a file with the list of emails '''
    with open(_filename, 'w+') as file:
        file.write(data)


if __name__ == "__main__":
    filepath = "./assets/potential-contacts.txt"

    emails = get_emails(filepath)
    makefile("emails.txt", emails)

    phones = get_phone(filepath)
    makefile("phone_numbers.txt", phones)