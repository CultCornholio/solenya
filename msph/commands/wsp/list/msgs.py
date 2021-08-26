def list_all(dict_):
    return (
        "\nAll avaliable key, value pairs.\n\n" +
        '\n'.join(f'{k}: {v}' for k,v in dict_.items()) +
        '\n'
    )

def list_file_key(key, value):
    return (
        f"\nFollowing {{{key}}} is registered:\n\n"
        f"{value}\n"
    )

def list_keys(keys):
    return (
        "All avaliable keys\n\n" + 
        "\n".join(keys) +
        '\n'
    )