# acmensse

ACME nosudo/secretenv is fork of [acmens][] that supports environment variable secrets
through openssl's `-passin env:VAR` idiom.
It uses ACMEv2 protocol and requires Python 3.

[acmens]: https://github.com/r5d/acmens

`acmensse` may be used for getting a new SSL certificate, renewing a SSL
certificate for a domain, and revoking a certificate for a domain.

It's meant to be run locally from your computer.

## prerequisites

* openssl or libressl
* python3
* pip
* virtualenv (if you want to use the repo version)

## installation

```sh
pip install git+ssh@github.com:aldocassola/acmens
```

Or, if you would like to use the repo version:

```sh
cd /path/to/acmens

# init virtual environment
make venv

# activate virtual environment
. .venv/bin/activate

# put acmens in your PATH
make develop
# note that any changes you make to acmens.py will be instantly reflected
# in the acmens in your PATH.
```

## getting/renewing a certificate

First, generate an user account key for Let's Encrypt:

```sh
openssl genrsa -aes256 -out user.key 4096
openssl rsa -in user.key -pubout -out user.pub
```

Next, generate the domain key and a certificate request:

```sh
# Generate domain key
openssl genrsa -aes256 -out domain.key 4096

# Generate CSR for a single domain
openssl req -new -sha256 -key domain.key -out domain.csr

# Or Generate CSR for multiple domains
openssl req -new -sha256 -key domain.key -subj "/" -addext "subjectAltName = DNS:example.com, DNS:www.example.com" -out domain.csr
```

Lastly, run `acmensse`:

```sh
ACMEPASS=$YOURUSERKEYPASSPHRASE acmensse --account-key user.key --email mail@example.com --csr domain.csr --out signed.crt
```
## dns challenge

If you want to use the DNS challenge type provide it using the `--challenge` flag.

```sh
acmensse--account-key user.key --email mail@example.com --challenge dns --csr domain.csr -out signed.crt
```

This will prompt you to update the DNS records to add a TXT record.

## revoking a certificate

This:

```sh
acmensse --revoke -k user.key --crt signed.crt
```

will revoke SSL certificate in `signed.crt`.
