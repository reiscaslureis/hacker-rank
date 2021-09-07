def email_parts(email):
    username = ''
    website = ''
    for i in email:
        if i == '@':
            break
        username = username + i

    aux = email[len(username) + 1:]

    for i in aux:
        if i == '.':
            break
        website = website + i

    extension = email[len(username) + len(website) + 2:]

    return username, website, extension

def fun(s):
    username, website, extension = email_parts(s)
    usernameI = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a',
                 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_']
    websiteI = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's',
                  'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    extensionI = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's',
                  'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    if len(username) == 0:
        username = False
    else:
        for i in username.lower():
            if i in usernameI:
                username = True
            else:
                username = False
                break

    for i in website.lower():
        if i in websiteI:
            website = True
        else:
            website = False
            break

    if len(extension) == 0 or len(extension) > 3:
        extension = False
    else:
        for i in extension.lower():
            if i in extensionI:
                extension = True
            else:
                extension = False
                break

    if username == False or website == False or extension == False:
        s = False
    else: s = True

    return s
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)