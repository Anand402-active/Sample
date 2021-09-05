with open("sample_text_write_file", "a") as f:
    # By default its a or a+ will create file then write some content into file
    content = f.write("Hello How are you Anand!\n")
    print(content)

