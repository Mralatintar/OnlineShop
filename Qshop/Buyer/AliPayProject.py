from alipay import AliPay

alipay_public_key_string= """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqRsoGH+s/HJkAauRAvbAg9I5k7k9cl/AS84tz4h2OmbiTCSC7+wQzi6zC80zFrtLI6ULuxxJJ8oh28wewvsvcaqs9JcWShT0MgrtqAvXPuJ1TquRw9memOD4qT7uZBxrpra/bNu3LBjwIenkX3S2KyPW5KMHAy6qVObsqZdC6eOJkeqdPmsXsnxalYbOjnEtWIEWPDpMLThhMv/HeXp9SiszHFwS6McDgdbUZQIcbKDM63k2GKq8Q7m+TkozHiTlwEvzaiOas6+yTx8dLkfA+5ULTSgvabZ/bVTPpnaqkVcfiQFQmWrNWenqfdORAw3ApyaNs5XLCipPZXockJdCEQIDAQAB
-----END PUBLIC KEY-----"""

alipay_private_key_string="""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqRsoGH+s/HJkAauRAvbAg9I5k7k9cl/AS84tz4h2OmbiTCSC7+wQzi6zC80zFrtLI6ULuxxJJ8oh28wewvsvcaqs9JcWShT0MgrtqAvXPuJ1TquRw9memOD4qT7uZBxrpra/bNu3LBjwIenkX3S2KyPW5KMHAy6qVObsqZdC6eOJkeqdPmsXsnxalYbOjnEtWIEWPDpMLThhMv/HeXp9SiszHFwS6McDgdbUZQIcbKDM63k2GKq8Q7m+TkozHiTlwEvzaiOas6+yTx8dLkfA+5ULTSgvabZ/bVTPpnaqkVcfiQFQmWrNWenqfdORAw3ApyaNs5XLCipPZXockJdCEQIDAQABAoIBAGkYoZCoOMAj75dCIztuUzMZwgLXCyM78uyp1Lq4GpItQtMDlgS596/MQiZBf1DPUeFzP5kn+ScrbmOFtlCDf3brFdZk18tuvl0jgZQA1+MTJsifxFWtt+1XU/MLU2kQaK8RwGJNIsfbL9JD5FSW2mhxO6qYz1Dg/acKZWb4xPNKHArV6FS3AkTNs+dXt70WOmqV3HKrL7B8F3NULV4/CAbbAWXspH7mw47v8sCyJTQm/QWA5EQ9/gLmZMkHxyBmyfRnfga0SrD2YWXIfGtexl1HQsx9oHtddCZQ0ncPurOW+Hcy5Wby23afe8iU3zB08cgANIbn2RyxVAW3Sdpe06kCgYEA6IiaYDN4OiT3/C/JIDAH4gGEEgKg5P9HpvF5ew+vmsWucWRQKehm9NokQ+D0hPDaCeJWrd23NisysP56occmylbajRGj+mQtlqAQdwXpjjkYGkpbUHHlmfyZVi/dvSEM+pWPg5YhcOlQB6+kFbTV1HlcLlNBAi0pNBwAUe+aqE8CgYEAuivu4m4Y2Ppw/jaahueYJeMMTvQslvzKbOZz+pBBiXFsgFiV0cYdfjvFAexyOEwR4FWqSIpiF9Vl58Rcm9XK6ttWAXpjCCxniBqmTKGA0cCN9idj/QsP3Yjv6f7zBbqybfjxH+EOI3K0/4dfCaJKKTc38nH3IjYtY2XdTZD0d58CgYEAqLW7s8KEH0OFPM560USn430QEnUfwSXKGcCnT/bghJ2aZCDQ3KcGU+4VU75aCj4pI/S4yOrNK5sJ60qnNMsmRLXhWWqMG3YlcVxutbxvaMXZy/FY8TPBzwhrRBH0gm0BWqm6d1EssBxG+Vyg4zLR1Ze7nsy+pNKZS3ppbQk3n5cCgYB+dbtF+a1NLgk01RhwTL6v9aN1uizTvxEtmfjsGbM6zl36bLIQFXgROD5hSSBpF1sJPId30PBC6kTXgy24+SdmEulABcdhVPBapmeSJB5h3F9R9n3X8/yp6gu1seWYXbI4O2Jm2jQFZjSGYoju/VtM1eJeAIXzqkN4gkgqGS3GVwKBgAS61CykNpRwRlc1BK6IhyvPQJLBLbV9Wath/WJFxfRUDtr6EgaEszEIRLVi7tlEgVyKLr0JOSYuYVa2qEui8AldpVhLTPvOIEscU2zSeI2MRrr814GI8DnA95V4iF6tMaMxnpL+vGZQyPpt/UPRwOHLt49/x72VochUY4gxp7/D
-----END RSA PRIVATE KEY-----"""

alipay=AliPay(
    appid="2016101200667729",
    app_notify_url=None,
    app_private_key_string=alipay_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2"
)
order_string=alipay.api_alipay_trade_page_pay(
    out_trade_no="100000001",
    total_amount=str(100.05),
    subject="么有杀害",
    return_url=None,
    notify_url=None
)
result="https://openapi.alipaydev.com/gateway.do?"+order_string

print(result)