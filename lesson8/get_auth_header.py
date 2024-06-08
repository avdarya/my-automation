def get_auth_header(token: str) -> dict:
  return {'x-client-token': token}