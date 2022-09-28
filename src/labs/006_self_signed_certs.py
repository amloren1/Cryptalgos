from cryptography import x509
from cryptography.x509 import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


from datetime import datetime, timedelta
import ipaddress


SERVER_IP = "192.168.0.93"

HOST_NAME = "ca_server"  # alternate

key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)

# assign common name to the certificate
# user generic naming for now
name = x509.Name(
    [
        x509.NameAttribute(NameOID.COMMON_NAME, HOST_NAME),
    ]
)

# alternative names. Must have this for some browsers
alt_names = [
    x509.DNSName(SERVER_IP),
    x509.DNSName(HOST_NAME),
    x509.IPAddress(ipaddress.ip_address(SERVER_IP)),
]

# create a self signed certificate
# ca = True meaning that we are the certificate authority
basic_constraints = x509.BasicConstraints(ca=True, path_length=0)

now = datetime.utcnow()

cert = (
    x509.CertificateBuilder()
    .subject_name(name)
    .issuer_name(name)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(now)
    .not_valid_after(now + timedelta(days=365))
    .add_extension(basic_constraints, True)
    .add_extension(x509.SubjectAlternativeName(alt_names), False)
    .sign(key, hashes.SHA256(), default_backend())
)

# write the certificate to a file
my_cert_pem = cert.public_bytes(serialization.Encoding.PEM)
my_key_pem = key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

with open("test_ubuntu_new.crt", "wb") as f:
    f.write(my_cert_pem)

with open("test_ubuntu_new.key", "wb") as f:
    f.write(my_key_pem)
