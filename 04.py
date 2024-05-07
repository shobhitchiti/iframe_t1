# with open("practice.txt",  'r') as f:
#     data = f.read()
#     if (data.find("learning")):
#         print("found")
#     else:
#         print("not found")


def check_for_line():
    with open('practice.txt', 'r') as f:
        word = "learning"
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
            else:
                line_no += 1