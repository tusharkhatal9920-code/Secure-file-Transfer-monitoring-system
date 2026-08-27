import hashlib
import os


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:

                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except:
        return None


def is_sensitive(file_path):

    filename = os.path.basename(file_path).lower()

    sensitive_words = [
        "password",
        "confidential",
        "secret",
        "salary",
        "private"
    ]

    for word in sensitive_words:

        if word in filename:
            return True

    return False