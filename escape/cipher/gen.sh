openssl genrsa -aes256 -out private.key -passout file:pass 8912
openssl rsa -in private.key -pubout -out public.key -passin file:pass
export PASS=$(cat "pass")
openssl req -x509 -days 100000 -new -keyout private.key -out certificate.pem -passin file:pass -passout env:PASS