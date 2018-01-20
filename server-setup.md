# Server Setup Notes

* Image: Amazon Linux 2
* Size: t2.micro
* Location: us-east-2 (Ohio)

## Packages

```
sudo amazon-linux-extras python3
sudo amazon-linux-extras nginx1.12

# sudo yum install -y yum-utils # already in base image?
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum install -y certbot python2-certbot-nginx
```

## Certificate

Apparently there's [an issue with certbot and nginx](https://community.letsencrypt.org/t/2018-01-11-update-regarding-acme-tls-sni-and-shared-hosting-infrastructure/50188) at the moment.

Done mostly manually via `certbot --authenticator webroot --installer nginx`. The nginx HTTPS conf points to where it drops the cert/key.

## Config

nginx stuff...directly in the global file. Changes something like:

```diff
 server {
     listen 80 default_server;
     ...
+    return 301 https://$host$request_uri;

 server {
     listen 443 ssl http2 default_server;
+    server_name nick.solutions;
     ...
     location / {
+        root /srv/staticsite;
     }
```

```sh
sudo mkdir /srv/staticsite
chown ec2-user:ec2-user /srv/staticsite
chmod 755 /srv/staticsite
```

Pushing built site: `rsync -av --delete pel/output/ me:/srv/staticsite/`

### Local Python 3 envs

```sh
python3 -m venv venv
source venv/bin/activate
python --version
```
