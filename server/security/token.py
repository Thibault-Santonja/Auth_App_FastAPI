from datetime import datetime, timedelta
from typing import Optional

import pyseto

from server.settings.variables import PASETO_PRIVATE_KEY, ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create a limited time PASETO access token.
    :param data:
    :param expires_delta:
    :return:
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = data.copy()
    to_encode.update({"exp": int((expire - datetime(1970, 1, 1)).total_seconds() * 1000)})

    return pyseto.encode(PASETO_PRIVATE_KEY, bytes(str(to_encode).replace("'", '"'), "UTF-8"))
