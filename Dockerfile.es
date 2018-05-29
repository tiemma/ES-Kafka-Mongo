FROM elasticsearch:2.0.0

ENTRYPOINT ["plugin", "install", "cloud-aws"]