import requests

def upload_file_to_disk(token, file_to_disk):

    response = requests.put(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": f'{file_to_disk}'},
        headers={"Authorization": f"OAuth {token}"}
    )
    return response

if __name__ == '__main__':
    upload_file_to_disk(' ', 'file_to_disk')