from shared.parsers.identity import parse_identity_payload_body
from shared.models.identity import Identity

def build_identity_from_kavli_payload(payload):
    identity = Identity(**parse_identity_payload_body(payload))

    return identity
