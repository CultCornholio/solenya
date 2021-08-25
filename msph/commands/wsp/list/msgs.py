def create_list_all_msg(dict_):
    return (
        "\nAll avaliable key, value pairs.\n\n" +
        '\n'.join(f'{k}: {v}' for k,v in dict_.items()) +
        '\n'
    )

def create_list_file_key_msg(key, value):
    return (
        f"\nFollowing {{{key}}} is registered:\n\n"
        f"{value}\n"
    )

def create_list_keys_msg(keys):
    return (
        "All avaliable keys\n\n" + 
        "\n".join(keys) +
        '\n'
    )